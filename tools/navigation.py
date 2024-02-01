from __future__ import annotations
import os
from typing import Dict, List

import yaml

from category import CategoryManager
from util import CATEGORY, NAVIGATION, DOT


def to_dict(nodes: List[Node]) -> List[Dict]:
    return list(map(lambda node: node.to_dict(), nodes))


class Node:
    """Tree node. Initially it is a leaf node."""

    def __init__(self, title: str, url: str):
        self._title = title
        self._url = url
        # category -> Node
        self._children: Dict[str, Node] = {}

    @property
    def title(self) -> str:
        return self._title

    @property
    def url(self) -> str:
        return self._url

    def children(self, category: str) -> Node | None:
        return self._children.get(category)

    def add_child(self, category: str, child: Node) -> None:
        self._children[category] = child

    def to_dict(self) -> Dict:
        """Convert the tree into dictionary."""

        this = {'title': self.title, 'url': self.url}
        if len(self._children) > 0:
            this['children'] = to_dict(
                sorted(self._children.values(), key=lambda node: node.title))

        return this


class Navigation:
    @staticmethod
    def main() -> List[Node]:
        """Main navigation bar."""

        home = Node('Home', '/')
        about = Node('About', '/about/')
        category = Node('Category', '/categories/')
        tags = Node('Tags', '/tags/')

        return [home, about, category, tags]

    @classmethod
    def side(cls, files: List[str]) -> List[Node]:
        """
        Side navigation bar.

        Categories: list of snake_case words(category).
        Filename: dot.case of snake_case words(category).
        Title(Category Name): Title Case of last word(category).
        Url: slash/case of snake_case words(category) plus leading&trailing slash.
        """

        # category -> Node
        side: Dict[str, Node] = {}
        for file in sorted(map(lambda file: file[:-3], files)):
            categories = DOT.parse(file)
            title = CategoryManager.title(categories)
            url = CategoryManager.permalink(categories)
            node = Node(title, url)
            if len(categories) > 1:
                ptr = side[categories[0]]
                for category in categories[1:-1]:
                    ptr = ptr.children(category)
                ptr.add_child(categories[-1], node)
            else:
                side[categories[0]] = node

        return sorted(side.values(), key=lambda node: node.title)

    @classmethod
    def sync(cls) -> None:
        """Sync the navigation with categories."""

        files = list(filter(lambda file: file !=
                     'categories.md', os.listdir(CATEGORY)))

        navigation = {'main': to_dict(cls.main())}
        side = cls.side(files)
        if len(side) > 0:
            navigation['side'] = to_dict(side)

        with open(NAVIGATION, 'w') as file:
            yaml.dump(navigation, file)


# Test
if __name__ == '__main__':
    Navigation.sync()
