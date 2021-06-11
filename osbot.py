import time
import telebot
import gspread

def do_work():
    from secret import TOKEN, ID

    bot = telebot.TeleBot(TOKEN)

    f = open('obr.txt')
    kol = f.read()
    f.close()
    kol = int(kol)

    gc = gspread.service_account()

    sh = gc.open("Прототип канала ОС для теста (Ответы)")

    new = 0
# Цикл для подсчёта количества строк в таблице, чтобы в дальнейшем отслeживать появилась ли новая строка
    count = 0
    i = 1
    val = ''
    while val != list():    
        count += 1
        i += 1
        val = sh.sheet1.get('A' + str(i))
    new_count = count
# Цикл для определения добавился ли новый отзыв. 
    if count > kol:
        new = count - kol   # вычислсяем сколько строк(отзывов) добавилось
        for j in range(new):       # цикл по вытаскиванию информации из ячеек
            count = new_count - j
            name = sh.sheet1.get('B' + str(count))
            contact = str(sh.sheet1.get('E' + str(count)) + sh.sheet1.get('J' + str(count)))
            message = str(sh.sheet1.get('G' + str(count)) + sh.sheet1.get('H' + str(count)) + sh.sheet1.get('I' + str(count)))
            
        # отправка сообщения в групповой чат
            sms = str('Имя клиента: ' + str(name) + '\nКонтакт: ' + str(contact) + '\nОбращение: ' + str(message))
            bot.send_message(ID, str(sms))
            time.sleep(45)

    if new_count > kol:
        f = open('obr.txt', 'w')
        f.writelines(str(new_count))
        f.close()
        

time.sleep(5)  
while True:
    do_work()
    time.sleep(120)