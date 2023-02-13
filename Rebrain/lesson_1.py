#'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
###################################################################
#1.1. Выделите и выведите на экран дату и время.
# test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# print(test_str[:15])

###################################################################
#1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
# test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# print(test_str[24:35])

###################################################################
#1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
# test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# print(test_str.replace('ideapad','PC-12092' ))

###################################################################
#1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
# test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# print(test_str.find('failed'))

###################################################################
#1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
# test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# lower_str = test_str.lower()
# print(lower_str.count('s'))

###################################################################
#1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
num1 = test_str[5]
print(num1)