from argparse import ArgumentParser, Namespace
from datetime import date, datetime
import os
import sys
from typing import List

from category import CategoryManager
from index import IndexManager, PostMeta
from navigation import Navigation
from util import POSTS, SLASH, TITLE


class PostManager:
    @staticmethod
    def __title(title: List[str]) -> str:
        """
        ## Input
        Title: list of unit words(title).
        ## Output
        Title: Title Case of unit words(title).
        """

        return TITLE.serialize(title)

    @staticmethod
    def __categories(path: str) -> List[str]:
        """
        ## Input
        Path: slash/case of snake_case words(category).
        ## Output
        Categories: list of snake_case words(category).
        """

        return SLASH.parse(path)

    @classmethod
    def create_post(cls, args: Namespace) -> None:
        """
        Create post.

        ## Inputs

        Title: list of unit words(title).
        Path: slash/case of snake_case words(category).
        Tags: list of list of unit words(tag).
        Date: ISO 8601 format.

        ## Outputs

        Categories: list of snake_case words(category).
        Title: Title Case of unit words(title).
        Tags: list of Title Case words(tag).
        """

        # Inputs
        title: List[str] = args.title
        path: str = args.path
        tags: List[List[str]] = args.tag
        date: str = args.date

        # Outputs
        categories = cls.__categories(path)
        title = cls.__title(title)
        tags = list(map(lambda tag: TITLE.serialize(tag), tags))

        # If title is not unique then prompt error and exit.
        manager = IndexManager.load()
        if manager.post_by_title(title) is not None:
            print('Post already exists.', file=sys.stderr)
            exit(1)

        # Create category and sync.
        try:
            CategoryManager.create_category(categories)
            Navigation.sync()
        except FileExistsError:
            pass

        # Create Index
        meta = manager.create_index(title, path, date)

        # Create file
        filepath = f'{POSTS}/{meta.filepath}/{meta.filename}'
        with open(filepath, 'w') as file:
            print(f'Create Post      {filepath}')
            content = [
                '---',
                f'title: {meta.title}',
                'layout: single',
                'categories:',
            ]
            content.extend(
                map(lambda category: f'  - {category}', meta.categories))
            if len(tags) > 0:
                content.append('tags:')
                content.extend(map(lambda tag: f'  - {tag}', tags))
            content.extend([
                f'permalink: {meta.permalink}',
                f'last_modified_at: {datetime.now().isoformat(timespec="seconds")}',
                '',
                '---',
                '',
                '<br>',
                '',
                f'[Back]({CategoryManager.permalink(categories)})',
            ])
            file.write('\n'.join(content))

        # Save Index
        manager.store()

    @classmethod
    def delete_post(cls, args: Namespace) -> None:
        """
        Delete post.

        ## Inputs

        Title: list of unit words(title).
        Sync: Whether to sync next_id.

        ## Outputs

        Categories: list of snake_case words(category).
        Title: Title Case of unit words(title).
        """

        # Inputs
        title: List[str] = args.title
        sync: bool = args.sync

        # Outputs
        title = cls.__title(title)

        # If file does not exist then prompt error and exit.
        manager = IndexManager.load()
        meta = manager.post_by_title(title)
        if meta is None:
            print('Post does not exist', file=sys.stderr)
            exit(1)

        categories = SLASH.parse(meta.filepath)

        # Delete file
        filepath = f'{POSTS}/{meta.filepath}/{meta.filename}'
        os.remove(filepath)
        print(f'Delete Post      {filepath}')

        # Delete Index
        manager.delete_index_by_title(title)
        if sync:
            manager.sync_id()

        # Delete category and sync.
        try:
            CategoryManager.delete_category(categories)
            Navigation.sync()
        except (FileNotFoundError, OSError):
            pass

        # Save Index
        manager.store()

    @staticmethod
    def __filepath(meta: PostMeta) -> str:
        return f'{POSTS}/{meta.filepath}/{meta.filename}'

    @classmethod
    def __update_post(cls, meta: PostMeta, date: str) -> None:
        # Old Data
        old_filepath = cls.__filepath(meta)
        # Update Index
        meta.date = date
        # Update File (mv)
        new_filepath = cls.__filepath(meta)
        os.rename(old_filepath, new_filepath)

    @classmethod
    def update_post(cls, args: Namespace) -> None:
        """
        Update post.

        ## Inputs

        Title: list of unit words(title).
        Date: ISO 8601 format.

        ## Outputs

        Title: Title Case of unit words(title).
        """

        # Inputs
        title: List[str] = args.title
        date: str = args.date

        # Outputs
        title = cls.__title(title)

        # If file does not exist then prompt error and exit.
        manager = IndexManager.load()
        meta = manager.post_by_title(title)
        if meta is None:
            print('Post does not exist', file=sys.stderr)
            exit(1)

        # Update
        cls.__update_post(meta, date)

        # Save Index
        manager.store()

    @classmethod
    def bulk_update_posts(cls, args: Namespace) -> None:
        """
        Bulk update posts.

        ## Inputs

        Path: slash/case of snake_case words(category).
        Date: ISO 8601 format.
        """

        # Inputs
        path: str = args.path
        date: str = args.date

        # Listup files
        files = os.listdir(f'{POSTS}/{path}')
        files = filter(lambda file: file.endswith('.md'), files)
        post_ids = sorted(map(lambda file: int(file.split('-')[3]), files))

        manager = IndexManager.load()
        metas = map(lambda post_id: manager.post_by_id(post_id), post_ids)
        for meta in metas:
            # Update
            cls.__update_post(meta, date)

        # Save Index
        manager.store()


parser = ArgumentParser(
    prog='post',
    description='Create or delete post'
)
subparser = parser.add_subparsers(required=True)


create_parser = subparser.add_parser('create', help='Create post')
create_parser.add_argument(
    'title',
    nargs='+',
    type=lambda word: word.lower(),
    help='Post title (no "\'._- included)'
)
create_parser.add_argument(
    '-p', '--path',
    required=True,
    help='Path (ex. foo/bar)'
)
create_parser.add_argument(
    '-t', '--tag',
    action='append',
    nargs='+',
    default=[],
    type=lambda word: word.lower(),
    help='Tags (no "\'._- included)'
)
create_parser.add_argument(
    '-d', '--date',
    default=date.today().isoformat(),
    help='Post date (ISO 8601)'
)
create_parser.set_defaults(func=lambda args: PostManager.create_post(args))


delete_parser = subparser.add_parser('delete', help='Delete post')
delete_parser.add_argument(
    'title',
    nargs='+',
    type=lambda word: word.lower(),
    help='Post title (no "\'._- included)'
)
delete_parser.add_argument(
    '--sync',
    action='store_true',
    default=False,
    help='Sync next_post_id (default: False)'
)
delete_parser.set_defaults(func=lambda args: PostManager.delete_post(args))


update_parser = subparser.add_parser('update', help='Update post date')
update_parser.add_argument(
    'title',
    nargs='+',
    type=lambda word: word.lower(),
    help='Post title (no "\'._- included)'
)
update_parser.add_argument(
    '-d', '--date',
    default=date.today().isoformat(),
    help='Post date (ISO 8601)'
)
update_parser.set_defaults(func=lambda args: PostManager.update_post(args))


bulk_update_parser = subparser.add_parser(
    'update-all', help='Update all post dates')
bulk_update_parser.add_argument(
    'path',
    help='Path (ex. foo/bar)'
)
bulk_update_parser.add_argument(
    '-d', '--date',
    default=date.today().isoformat(),
    help='Post date (ISO 8601)'
)
bulk_update_parser.set_defaults(
    func=lambda args: PostManager.bulk_update_posts(args))


if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
