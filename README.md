# Sprint_4 tests list:

1. [test_add_new_book_add_two_books] Данный пример теста осуществляет проверку метода добавления пары книг в словарь
   books_genre
2. [test_set_book_genre_set_for_existing_book_and_genre] Данный тест осуществляет проверку метода установки жанра книги,
   если она уже есть в словаре и её жанр входит в список существующих жанров
3. [test_get_book_genre_get_for_existing_book] Данный тест осуществляет проверку метода вывода жанра книги по ее имени
4. [test_get_books_with_specific_genre_for_several_books] Данный тест осуществляет проверку метода вывода списка книг с
   определенным жанром
5. [test_get_books_genre_for_several_books] Данный тест осуществляет проверку метода вывода словаря books_genre
6. [test_get_books_for_children_for_children_books] Данный тест осуществляет проверку метода возврата книг, которые
   подходят детям
7. [test_add_book_in_favorites_add_one_book] Данный тест осуществляет проверку метода добавления книги из словаря
   books_genre в избранное. В данном тесте используется параметризация
8. [test_delete_book_from_favorites_delete_two_books] Данный тест осуществляет проверку метода удаления пары книг из
   списка избранных
9. [test_get_list_of_favorites_books_for_one_book] Данный тест осуществляет проверку метода отображения списка избранных
   книг
10. [test_add_new_book_added_books_have_no_genre] Данный тест осуществляет проверку того, что у добавленных методом
    add_new_book книг нет жанра. Данный тест использует параметризацию