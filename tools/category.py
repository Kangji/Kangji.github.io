import os
from typing import List

from util import DOT, SLASH, SNAKE, TITLE, CATEGORY, POSTS


class CategoryManager:
    """
    Manages category files and post directory.

    Categories: list of snake_case words(category).
    Filename: dot.case of snake_case words(category) plus trailing file extension ".md".
    Title(Category Name): Title Case of last word(category).
    Permalink: slash/case of snake_case words(category) plus leading&trailing slash.
    Post directory: slash/case of snake_case words(category).
    """

    @classmethod
    def create_category(cls, categories: List[str]) -> None:
        """
        Recursively create category files and corresponding post directory.
        If the post directory already exists, it raises error.
        If the category file already exists, it does nothing.
        Categories must not be empty.
        Each category should not include any of "'.-

        Categories(input): [category_one, category_two, category_three]

        Filename: category_one.category_two.category_three.md
        Title(Category Name): Category Three
        Permalink: /category_one/category_two/category_three/
        Post directory: category_one/category_two/category_three
        """

        cls.__create_category_files(categories)
        dir = cls.postdir(categories)
        os.makedirs(dir)
        print(f'Create Directory {dir}')

    @classmethod
    def delete_category(cls, categories: List[str]) -> None:
        """
        Recursively delete category files and corresponding post directory.
        If the category does not exist or post exist, raises error.
        Categories must not be empty.
        Each category should not include any of "'.-

        Categories(input): [category_one, category_two, category_three]

        Filename: category_one.category_two.category_three.md
        """

        dir = cls.postdir(categories)
        os.removedirs(dir)
        print(f'Delete Directory {dir}')
        cls.__delete_category_files(categories)

    @staticmethod
    def postdir(categories: List[str]) -> str:
        """Post directory."""

        return f'{POSTS}/{SLASH.serialize(categories)}'

    @staticmethod
    def permalink(categories: List[str]) -> str:
        """Permalink of category."""

        return f'/{SLASH.serialize(categories)}/'

    @staticmethod
    def title(categories: List[str]) -> str:
        return TITLE.serialize(SNAKE.parse(categories[-1]))

    @classmethod
    def __create_category_files(cls, categories: List[str]) -> None:
        """
        Recursively create category files.
        If the category file already exists, it does nothing.
        Each category should not include any of "'.-

        Categories(input): [category_one, category_two, category_three]

        Filename: category_one.category_two.category_three.md
        Title(Category Name): Category Three
        Permalink: /category_one/category_two/category_three/
        """

        if len(categories) == 0:
            return

        filepath = cls.__filepath(categories)
        if os.path.exists(filepath) is False:
            title = cls.title(categories)
            permalink = cls.permalink(categories)
            content = cls.__content(title, permalink)

            with open(filepath, 'w') as file:
                file.write(content)
                print(f'Create Category  {filepath}')

        cls.__create_category_files(categories[:-1])

    @classmethod
    def __delete_category_files(cls, categories: List[str]) -> None:
        """
        Recursively delete category files based on post directory.
        Categories must not be empty.
        Each category should not include any of "'.-

        Categories(input): [category_one, category_two, category_three]

        Filename: category_one.category_two.category_three.md
        """

        if len(categories) == 0:
            return

        if os.path.exists(cls.postdir(categories)) is False:
            filepath = cls.__filepath(categories)
            os.remove(filepath)
            print(f'Delete Category  {filepath}')

        cls.__delete_category_files(categories[:-1])

    @staticmethod
    def __filepath(categories: List[str]) -> str:
        return f'{CATEGORY}/{DOT.serialize(categories)}.md'

    @staticmethod
    def __content(title: str, permalink: str) -> str:
        return '\n'.join([
            '---',
            f'title: {title}',
            'layout: archive',
            f'permalink: {permalink}',
            'author_profile: true',
            'sidebar:',
            '  title: All Posts',
            '  nav: side',
            '',
            '---',
            '',
            "{% assign entries_layout = page.entries_layout | default: 'list' %}",
            f"{{% assign posts = site.categories['{title}'] %}}",
            "{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}",
        ])


# Test
if __name__ == "__main__":
    print(CategoryManager.create_category(['blog', 'gsoc']))
    print(CategoryManager.create_category(['blog', 'gsoc']))
    CategoryManager.delete_category(['blog', 'gsoc'])
