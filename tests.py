import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        books = collector.books_genre.keys()
        assert len(books) == 2

    def test_get_genres(self, collector):
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre == genres

    def test_get_genres_for_new_books(self, collector):
        collector.add_new_book('Я легенда')
        collector.set_book_genre('Я легенда', 'Ужасы')

        collector.add_new_book('99 франков')
        collector.set_book_genre('99 франков', 'Комедии')

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        expected_books_genres = {
            'Я легенда': 'Ужасы',
            '99 франков': 'Комедии',
            'Шерлок Холмс': 'Детективы'
        }

        assert collector.get_books_genre() == expected_books_genres

    def test_get_genre(self, collector):
        collector.add_new_book('Невероятная жизнь Евгения Петросяна')
        collector.set_book_genre('Невероятная жизнь Евгения Петросяна', 'Ужасы')
        assert collector.get_book_genre('Невероятная жизнь Евгения Петросяна') == 'Ужасы'

    def test_get_books_with_specific_genres(self, collector):
        collector.add_new_book('Сказ про Федота Стрельца')
        collector.genre.append('Сатира')
        collector.set_book_genre('Сказ про Федота Стрельца', 'Сатира')

        satiric_books_list = ['Сказ про Федота Стрельца']
        assert collector.get_books_with_specific_genre('Сатира') == satiric_books_list

    def test_get_books_for_children(self, collector_with_books):
        collector_with_books.set_book_genre('Гарри Поттер', 'Фантастика')
        collector_with_books.set_book_genre('Шерлок Холмс', 'Детективы')
        collector_with_books.set_book_genre('Я легенда', 'Ужасы')
        collector_with_books.set_book_genre('Гриффины', 'Комедии')

        expected_books_for_children = ['Гарри Поттер', 'Гриффины']
        assert collector_with_books.get_books_for_children() == expected_books_for_children

    def test_add_book_to_favorites_and_check_favorites_length(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        # проверяем, что список пуст
        assert len(collector.favorites) == 0
        collector.add_book_in_favorites('Гарри Поттер')
        assert len(collector.favorites) == 1

    def test_add_book_to_favorites_and_check_book_name_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.favorites == ['Гарри Поттер']

    def test_delete_book_from_favorites_and_check_favorites_length(self, collector):
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        assert len(collector.favorites) == 1
        collector.delete_book_from_favorites('Хоббит')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_and_check_favorites_list(self, collector):
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        assert collector.favorites == ['Хоббит']
        collector.delete_book_from_favorites('Хоббит')
        assert collector.favorites == []

    def test_added_book_has_no_genre(self, collector):
        collector.add_new_book('О мышах и людях')
        assert collector.get_book_genre('О мышах и людях') == ''

    @pytest.mark.parametrize('book', ['Бесприданница', 'Атака Титанов', 'Человек-Бензопила'])
    def test_add_many_to_favorites(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        result_str = ', '.join((collector.get_list_of_favorites_books()))
        assert result_str == book

    def test_add_copy_to_favorites(self, collector):
        collector.add_new_book('Баллады')
        collector.add_book_in_favorites('Баллады')
        collector.add_new_book('Баллады')
        collector.add_book_in_favorites('Баллады')
        assert len(collector.favorites) == 1
