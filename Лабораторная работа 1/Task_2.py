# TODO Найдите количество книг, которое можно разместить на дискете
sizeall_in_megabytes = 1.44
pages = 100  # количество страниц
lines_in_page = 50  # количество строк
characters_in_line = 25  # количество символов
size_one_character = 4  # размер 1 символа
number_of_characters = pages * lines_in_page * characters_in_line
size_all_characters = size_one_character * number_of_characters
size_in_megabytes = size_all_characters / 1024 / 1024
number_of_books = sizeall_in_megabytes / size_in_megabytes
print("Количество книг, помещающихся на дискету:", int(number_of_books))
