# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_disc = 1.44
pages = 100
letters = 23
line = 50
volume_of_symbol = 4
volume_of_book = volume_of_symbol * line * letters * pages
volume_of_disc_in_B = volume_of_disc * 1024 * 1024
print("Количество книг, помещающихся на дискету:", int(volume_of_disc_in_B // volume_of_book))
