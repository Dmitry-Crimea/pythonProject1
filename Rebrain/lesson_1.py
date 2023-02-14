
#'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
###################################################################
#1.1. Выделите и выведите на экран дату и время.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(test_str[:15])

###################################################################
#1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(test_str[24:31])

###################################################################
#1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(test_str.replace('ideapad','PC-12092' ))

###################################################################
# 1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(test_str.find('failed'))

###################################################################
#1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
print(test_str.lower().count('s'))

###################################################################
#1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
test_str = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
num1 = test_str[7:9]
num2 = test_str[10:12]
num3 = test_str[13:15]
sum_1 = int(num1) + int(num2) + int(num3)
print(sum_1)

#2.'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
#2.1 Нужно сформировать и вывести сообщение в таком формате:
# The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>"
# at <дата, время>
log_message = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
PC_name = log_message[16:23]
service_name = log_message[24:35]
message = log_message[36:-22]
reason = log_message[-20:]
date = log_message[:16]
print(f'The PC {PC_name} receive message from service {service_name}: what says {message}: because \"{reason}\" at {date}')