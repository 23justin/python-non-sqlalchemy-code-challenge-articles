class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str) or len(name) == 0 or len(category) == 0:
            raise ValueError("Magazine name and category must be non-empty strings.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(article.author for article in self._articles)
        return [author for author, count in author_count.items() if count > 2]


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise ValueError("Invalid author or magazine.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Invalid author.")
        self._author._articles.remove(self)
        new_author._articles.append(self)
        self._author = new_author

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Invalid magazine.")
        self._magazine._articles.remove(self)
        new_magazine._articles.append(self)
        self._magazine = new_magazine
