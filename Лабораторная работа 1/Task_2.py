# TODO Найдите количество книг, которое можно разместить на дискете
sizeall= 1.44
sta = 100 #количество страниц
stra = 50 #количество строк
sim = 25 #количество символов
sizesim = 4 #размер 1 символа
kolsim = sta * stra * sim
sizesimvolov = sizesim * kolsim
amb = sizesimvolov / 1024 / 1024
v = sizeall / amb
print("Количество книг, помещающихся на дискету:", round(v))
