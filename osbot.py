'''
Чат бот, который сразу после поступления отзыва обрабатывает его и на основе данных выдает задание на обработку в телеграмм канал, где находятся ответсвенные за качество сотрудники. 
'''
import requests
import telebot

# 1. Пассажир пишет отзыв, и его отзыв попадает на некоторый сервер аэропорта.
# 2. Чат бот, сразу после поступления отзыва, на вход получает отзыв с сервера куда поступают все отзывы. 
# 3. Чат бот выделяет ФИО и контактные данные пассажира в отдельную переменную. 
# 4. Чат бот выделяет проблему. 
# 5. Чат бот формирует задачу и отправляет ее в телеграмм канал с возможными ответам в виде кнопки "взять в работу"
# 6. Сотрудник выбирает отзыв и нажимает кнопку.
# 7. Когда сотрудник "Н" нажимает кнопку "взять в работу" отзыв дублируется ему в личные сообщения. 
# 8. Для других сотрудников задание становится более неактивным. 
# 9. После обработки запроса, сотрудником в чат боте отмечается "ответ дан" и прилагается скрин ответа по почте или комментарий если ответ по телефону. 
# 10. Добавить в бот счетчик для каждого сотрудника. 
# 11. После каждого данного ответа сотруднику добавляется балл за обработку.
# 12. В конце месяца начальнику отдела приходит сообщение от бота в котором прописано сколько отзывов обработал каждый сотрудник. 
# 13. В конце месяца счетчик сбрасывается


'''
Библиотеки: 
1. pytelegrambotAPI
2. Request ???
'''

import gspread
# Создал сервис аккаунт на гугл для доступа к таблице
gc = gspread.service_account()

sh = gc.open("Прототип канала ОС для теста (Ответы)")

print(sh.sheet1.get('A1'))

# Цикл для подсчёта количества строк в таблице, чтобы в дальнейшем отслкживать появилась ли новая строка
count = 0
i = 1
val = sh.sheet1.get('A' + str(i))
while val != list():
    
    i += 1
    count += 1
    val = sh.sheet1.get('A' + str(i))
    
print(count)
