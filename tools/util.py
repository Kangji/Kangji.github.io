from abc import ABC, abstractmethod
import os
from typing import List


CWD = os.getcwd()
NAVIGATION = f'{CWD}/_data/navigation.yml'
CATEGORY = f'{CWD}/_pages/categories'
POSTS = f'{CWD}/_posts'
INDEX = f'{CWD}/tools/index.json'


class Naming(ABC):
    @abstractmethod
    def parse(self, string: str) -> List[str]:
        """Parse the string into words(lowercase)"""

    @abstractmethod
    def serialize(self, words: List[str]) -> str:
        """Serialize into string of specific convention"""


class _LowerCase(Naming):
    def __init__(self, sep: str):
        self._sep = sep

    @property
    def sep(self) -> str:
        """Separator"""

        return self._sep

    def parse(self, string: str) -> List[str]:
        return list(map(lambda word: word.lower(), string.split(self._sep)))

    def serialize(self, words: List[str]) -> str:
        return self.sep.join(words)


class __DotCase(_LowerCase):
    """dot.case"""

    def __init__(self):
        super().__init__('.')


class __SnakeCase(_LowerCase):
    """snake_case"""

    def __init__(self):
        super().__init__('_')


class __SlashCase(_LowerCase):
    """slash/case"""

    def __init__(self):
        super().__init__('/')


class __TitleCase(Naming):
    """Title Case"""

    def parse(self, string: str) -> List[str]:
        return list(map(lambda word: word.lower(), string.split(' ')))

    def serialize(self, words: List[str]) -> str:
        return ' '.join(map(lambda word: word.capitalize(), words))


DOT = __DotCase()
SNAKE = __SnakeCase()
SLASH = __SlashCase()
TITLE = __TitleCase()
