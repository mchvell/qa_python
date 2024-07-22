import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def collector_with_books(collector):
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Шерлок Холмс')
    collector.add_new_book('Я легенда')
    collector.add_new_book('Гриффины')
    return collector