# qa_python

### 1. Переписал ваш тест, который ```test_add_new_book_add_two_books```.
Он бай дизайн был сломанный и проверял что-то странное.

### 2. Добавил базовый тест ```test_get_genres```
Данный тест проверяет переменную жанров, которая установлена по умолчанию
в конструкторе класса.

### 3. Добавил тест ```test_get_genres_for_new_books```
Данный тест проверяет создание книг со стандартными данными
с заданным словарем.

### 4. Добавил тест ```test_get_genre```
Данный тест проверяет создание книги со стандартным жанром и 
получение жанра по созданной книге.

### 5. Добавил тест ```test_get_books_with_specific_genres```
Данный тест провеяет создание книги с новым жанром и проверка.
наличия жанра по названию книги.

### 6. Добавил тест ```test_get_books_for_children```
Данный тест добавляет жанры для созданных фикстурой книг.
Получает список книг по жанрам и сравниваем с ожидаемым результатом.

### 7. Добавил тест ```shell
test_add_book_to_favorites_and_check_favorites_length```
Данный тест проверяет длинну списка избранных с ожидаемым значением.

### 8. Добавил тест ```shell
test_add_book_to_favorites_and_check_book_name_in_favorites```
Данный тест проверяет добавление книги в список избранного.
И проверяет элемент списка с ожидаемым.

### 9. Добавил тест ```test_delete_book_from_favorites_and_check_favorites_length```
Добавляет элемент в список избранного.
Проверяет его наличие в избранном.
Удаляет из избранного и проверяет длинну списка.

### 10. Добавил тест ```test_delete_book_from_favorites_and_check_favorites_list```
Добавляет элемент в список избранного.
Проверяет его наличие в избранном.

### 11. Добавил тест ```shell
test_added_book_has_no_genre```
Добавляет книгу в список книг. Проверяет, что у книги отсутвует жанр

### 12. Добавил тест ```test_add_many_to_favorites```
Добавляет множество книг в избранное и проверяет их наличии в списке

### 13. Добавил тест ```shell
test_add_copy_to_favorites```
Добавляет 2 одинаковые книги в список избранных и проверяет, 
что длинна списка не увеличилась