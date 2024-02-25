import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_set_for_existing_book_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Имя розы')
        collector.set_book_genre('Имя розы', 'Детективы')

        assert collector.get_book_genre('Имя розы') == 'Детективы'

    def test_get_book_genre_get_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на Ниле')
        collector.set_book_genre('Смерть на Ниле', 'Детективы')
        assert collector.get_book_genre('Смерть на Ниле') == 'Детективы'

    def test_get_books_with_specific_genre_for_several_books(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.add_new_book('Тело в библиотеке')
        collector.set_book_genre('Тело в библиотеке', 'Детективы')
        collector.add_new_book('Скрюченный домишко')
        collector.set_book_genre('Скрюченный домишко', 'Детективы')
        books_list = collector.get_books_with_specific_genre('Детективы')
        assert books_list == ['Тело в библиотеке', 'Скрюченный домишко']

    def test_get_books_genre_for_several_books(self):
        collector = BooksCollector()
        collector.add_new_book('Непобедимый')
        collector.set_book_genre('Непобедимый', 'Фантастика')
        collector.add_new_book('Кристина')
        collector.set_book_genre('Кристина', 'Ужасы')
        assert collector.get_books_genre() == {'Непобедимый': 'Фантастика',
                                               'Кристина': 'Ужасы'}

    def test_get_books_for_children_for_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collector.add_new_book('Загадочное происшествие в Стайлзе')
        collector.set_book_genre('Загадочное происшествие в Стайлзе', 'Детективы')
        collector.add_new_book('Русалочка')
        collector.set_book_genre('Русалочка', 'Мультфильмы')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        books_list = collector.get_books_for_children()
        assert books_list == ['Автостопом по Галактике', 'Русалочка', 'Горе от ума']

    @pytest.mark.parametrize('name, genre', [['Солярис', 'Фантастика'], ['Скрюченный домишко', 'Детективы']])
    def test_add_book_in_favorites_add_one_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_delete_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collector.add_new_book('Загадочное происшествие в Стайлзе')
        collector.set_book_genre('Загадочное происшествие в Стайлзе', 'Детективы')
        collector.add_new_book('Русалочка')
        collector.set_book_genre('Русалочка', 'Мультфильмы')
        collector.add_book_in_favorites('Автостопом по Галактике')
        collector.add_book_in_favorites('Кладбище домашних животных')
        collector.add_book_in_favorites('Загадочное происшествие в Стайлзе')
        collector.add_book_in_favorites('Русалочка')
        collector.delete_book_from_favorites('Кладбище домашних животных')
        collector.delete_book_from_favorites('Загадочное происшествие в Стайлзе')
        assert collector.get_list_of_favorites_books() == ['Автостопом по Галактике', 'Русалочка']

    def test_get_list_of_favorites_books_for_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')
        collector.add_new_book('Загадочное происшествие в Стайлзе')
        collector.set_book_genre('Загадочное происшествие в Стайлзе', 'Детективы')
        collector.add_book_in_favorites('Автостопом по Галактике')
        assert collector.get_list_of_favorites_books() == ['Автостопом по Галактике']

    @pytest.mark.parametrize('name', ['Солярис', 'Скрюченный домишко', 'Имя розы'])
    def test_add_new_book_added_books_have_no_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''
