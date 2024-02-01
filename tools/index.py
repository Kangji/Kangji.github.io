from __future__ import annotations
import json
from typing import Dict, List

from util import INDEX, SLASH, SNAKE, TITLE


class PostMeta(dict):
    """
    Post metadata.

    Post ID: uniquely assigned integer.
    Title: Title Case of unit words(title).
    Date: ISO 8601 format.
    Filepath: slash/case of snake_case words(category).
    """

    @property
    def post_id(self) -> int:
        """Uniquely assigned integer."""

        return self["id"]

    @property
    def title(self) -> str:
        """Title Case of unit words(title)."""

        return self["title"]

    @property
    def date(self) -> str:
        """ISO 8601 format."""

        return self["date"]

    @date.setter
    def date(self, date: str) -> None:
        self["date"] = date

    @property
    def filepath(self) -> str:
        """slash/case of snake_case words(category)."""

        return self["filepath"]

    @property
    def filename(self) -> str:
        """<today>-<id(5 digit)>-<title_snake_case>.md"""

        return f'{self.date}-{self.post_id:0>5}-{SNAKE.serialize(TITLE.parse(self.title))}.md'

    @property
    def permalink(self) -> str:
        """/<filepath>/<id>/"""

        return f'/{self.filepath}/{self.post_id}/'

    @property
    def categories(self) -> List[str]:
        """list of Title Case words(category)."""

        return list(map(lambda word: TITLE.serialize(SNAKE.parse(word)), SLASH.parse(self.filepath)))


class IndexManager(dict):
    """
    Manages index file.
    Supports indexing by title and id.
    Consistent index file must contain both title and id index per each metadata.

    Index consists of:
    * `next_seq`: next sequence number
    * `post_by_title`: mapping from title to PostMeta
    * `post_by_id`: mapping from id to PostMeta
    """

    NEXT_SEQ = 'next_seq'
    POST_BY_TITLE = 'post_by_title'
    POST_BY_ID = 'post_by_id'

    @property
    def new_id(self) -> int:
        seq = self[self.NEXT_SEQ]
        self[self.NEXT_SEQ] += 1
        return seq

    def sync_id(self) -> None:
        """Sync id."""

        self[self.NEXT_SEQ] = max(
            map(lambda value: int(value), self[self.POST_BY_ID])) + 1

    def post_by_title(self, title: str) -> PostMeta | None:
        """
        Search post by title.

        Title: Title Case of unit words(title).
        """

        return self[self.POST_BY_TITLE].get(title)

    def __add_post_by_title(self, meta: PostMeta) -> None:
        self[self.POST_BY_TITLE][meta.title] = meta

    def __pop_post_by_title(self, title: str) -> None:
        self[self.POST_BY_TITLE].pop(title)

    def post_by_id(self, post_id: int) -> PostMeta | None:
        """
        Search post by id.

        Post ID: uniquely assigned integer.
        """

        return self[self.POST_BY_ID].get(str(post_id))

    def __add_post_by_id(self, meta: PostMeta) -> None:
        self[self.POST_BY_ID][str(meta.post_id)] = meta

    def __pop_post_by_id(self, post_id: int) -> None:
        self[self.POST_BY_ID].pop(str(post_id))

    @staticmethod
    def load() -> IndexManager:
        """Load index from file."""

        with open(INDEX, "r") as index:
            data: Dict[str, Dict[str, Dict]] = json.load(index)
            this = IndexManager(
                {IndexManager.NEXT_SEQ: data[IndexManager.NEXT_SEQ], IndexManager.POST_BY_TITLE: {}, IndexManager.POST_BY_ID: {}})
            for meta in data[IndexManager.POST_BY_TITLE].values():
                meta = PostMeta(**meta)
                this.__add_post_by_title(meta)
                this.__add_post_by_id(meta)

            return this

    def store(self) -> None:
        """Store index to file."""

        with open(INDEX, "w") as index:
            json.dump(self, index)

    def create_index(self, title: str, filepath: str, date: str) -> PostMeta | None:
        """
        Create index of new post.
        If the post title already exists, nothing is created.

        Title: Title Case of unit words(title).
        Date: ISO 8601 format.
        Filepath: slash/case of snake_case words(category).
        """

        if self.post_by_title(title) is not None:
            return

        post_id = self.new_id
        meta = PostMeta(id=post_id, title=title, date=date, filepath=filepath)

        self.__add_post_by_title(meta)
        self.__add_post_by_id(meta)

        return meta

    def __delete_index(self, title: str, post_id: int) -> None:
        self.__pop_post_by_title(title)
        self.__pop_post_by_id(post_id)

    def delete_index_by_title(self, title: str) -> None:
        """
        Delete index of the post if exists.

        Title: Title Case of unit words(title).
        """

        meta = self.post_by_title(title)
        if meta is not None:
            self.__delete_index(meta.title, meta.post_id)

    def delete_index_by_id(self, post_id: int) -> None:
        """
        Delete index of the post if exists.

        Post ID: uniquely assigned integer.
        """

        meta = self.post_by_id(post_id)
        if meta is not None:
            self.__delete_index(meta.title, meta.post_id)


if __name__ == '__main__':
    manager = IndexManager.load()
    meta = manager.create_index('Bar', 'foo/bar', '2024-01-01')
    print(meta.categories)
    print(meta.filename)
    manager.delete_index_by_title('Bar')
    manager.store()
