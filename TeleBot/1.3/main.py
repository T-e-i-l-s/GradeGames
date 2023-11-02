
import telebot
bot = telebot.TeleBot('2084681098:AAEq9uPlIvjsg5GKJ79xxGMCTNrm2OdZ4UY')

messages = 0



f = open("users.txt", "w")
f.write('')
f.close()
bm = telebot.types.ReplyKeyboardMarkup()
bm.add('Вы забанены!')
bm.add('Обновить')


menu = telebot.types.ReplyKeyboardMarkup()
menu.add('Расписание')
menu.add('ДЗ','Дежурство')
menu.add('Новости')
menu.add('Сообщить_о_болезни','Сообщить свой id')
menu.add('GradeGames')



dz = telebot.types.ReplyKeyboardMarkup()
dz.add('Биология')
dz.add('Турецкий')
dz.add('География')
dz.add('ИЗО')
dz.add('Английский(сред)')
dz.add('Английский(сил)')
dz.add('История')
dz.add('Лит-ра')
dz.add('Математика')
dz.add('Музыка')
dz.add('Общество')
dz.add('Род.лит(рус)')
dz.add('Родной(рус)')
dz.add('Род.лит(тат)')
dz.add('Родной(тат)')
dz.add('Рус.яз')
dz.add('Технология')
dz.add('Физ-культура')
dz.add('MENU')


week = telebot.types.ReplyKeyboardMarkup()
week.add('ПН','ВТ','СР')
week.add('ЧТ','ПТ','СБ')
week.add('MENU')


cust = ['','','','','',
        '','','','','',
        '','','','','',
        '','','','','',
        '','','','','']
custn = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    global cust
    global custn
    custn = custn + 1
    cust[custn - 1] = message.chat.id
    bot.send_message(message.chat.id, 'Привет,я обновился до версии 1.3.'
                                      'Теперь ты сможешь узнать у меня расписание.'
                                      'Так же теперь мы следим за тобой активнее))),но это не важно.'
                                      'К сожалению из-за многочисленного спама и указания ложной'
                                      'информации мы не смогли коректно собрать ваши telegram_id,'
                                      'поэтому просьба повторить авторизацию,нажав "сообщить_свой_id" и'
                                      'выполнив действия указанные там,'
                                      'ДЕЛАЙТЕ ЭТО ВНИМАТЕЛЬНЕЕ, за указание ложной информации БАН(1день).', reply_markup=menu)





nws1 = '-'
nws2 = '-'
nws3 = '-'
nws4 = '-'
nws5 = '-'


@bot.message_handler(commands=['nws1'])
def new(message):
    global nws1
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws1 = nws.replace('/nws1 ','')

@bot.message_handler(commands=['nws2'])
def new(message):
    global nws2
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws2 = nws.replace('/nws2 ','')

@bot.message_handler(commands=['nws3'])
def new(message):
    global nws3
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws3 = nws.replace('/nws3 ','')

@bot.message_handler(commands=['nws4'])
def new(message):
    global nws4
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws4 = nws.replace('/nws4 ','')

@bot.message_handler(commands=['nws5'])
def new(message):
    global nws5
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws5 = nws.replace('/nws5 ','')

stu = ['Аккмалутдинов','Бариев','Воробьев','Гашигулин','Димухаметов',
       'Загидулин','Закиров','Ильин','Исмагилов','Леухин',
       'Лукьянов','Мифтахов','МустафинК','МустафинС','Мухаметгалиев',
       'ПимурзинРусл','ПимурзинРуст','Сахабутдинов','Фаизов','Фазлиев',
       'Хамидулин','Шамсиев','Юсупов']
mrk = ['','','','','',
       '','','','','',
       '','','','','',
       '','','','','',
       '','','']
stuindex = 24
@bot.message_handler(commands=['nm'])
def games(message):
    global name
    global stuindex
    global stu
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    name = message.text
    name = name.replace('/nm ', '')
    if name in stu:
        stuindex = stu.index(name)
    else:
        bot.send_message(message.chat.id,'Ошибка ввода,ученик не найден!!!')

@bot.message_handler(commands=['lvl'])
def games(message):
    global lvl
    global mrk
    global stuindex
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    lvl = message.text
    lvl = lvl.replace('/lvl ', '')
    mrk[stuindex]=lvl


@bot.message_handler(commands=['mon'])
def mon(message):
    global mon
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    mon=message.text
    mon=mon.replace('/mon ','')


@bot.message_handler(commands=['tue'])
def tue(message):
    global tue
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    tue=message.text
    tue=tue.replace('/tue ','')


@bot.message_handler(commands=['wed'])
def wed(message):
    global wed
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    wed=message.text
    wed = wed.replace('/wed ', '')


@bot.message_handler(commands=['thu'])
def thu(message):
    global thu
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    thu=message.text
    thu=thu.replace('/thu ','')


@bot.message_handler(commands=['fri'])
def fri(message):
    global fri
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    fri=message.text
    fri=fri.replace('/fri ','')


@bot.message_handler(commands=['sat'])
def sat(message):
    global sat
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    sat=message.text
    sat=sat.replace('/sat ','')


@bot.message_handler(commands=['ill'])
def otsut(message):
    bot.send_message(message.chat.id, 'Обработка...')
    ill = message.text
    ill=ill.replace('/ill','')
    if ill == '':
        bot.send_message(message.chat.id,'Неверное заполнение, попробуйте еще раз.')
    else:
        f = open("ills.txt", "a")
        f.write('name: ' + ill + ' id: ' + str(message.chat.id) + ' .                             ')
        f.close()
        bot.send_message(1202390893, 'Сообщает об отсутствии ' + ill + ' .' + 'id отправителя: ' + str(message.chat.id)  )


hw = ['','','','','',
       '','','','','',
       '','','','','',
       '','','','','','','',
       '','','','','',
       '','','','','','','']
@bot.message_handler(commands=['bio'])
def hw0(message):
    s = message.text
    s = s.replace('/bio ','')
    hw[0] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['tur'])
def hw0(message):
    s = message.text
    s = s.replace('/tur ','')
    hw[1] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['geo'])
def hw0(message):
    s = message.text
    s = s.replace('/geo ','')
    hw[2] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['art'])
def hw0(message):
    s = message.text
    s = s.replace('/art ','')
    hw[3] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['eng1'])
def hw0(message):
    s = message.text
    s = s.replace('/eng1 ','')
    hw[4] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['eng2'])
def hw0(message):
    s = message.text
    s = s.replace('/eng2 ','')
    hw[5] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['his'])
def hw0(message):
    s = message.text
    s = s.replace('/his ','')
    hw[6] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['lit'])
def hw0(message):
    s = message.text
    s = s.replace('/lit ','')
    hw[7] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['math'])
def hw0(message):
    s = message.text
    s = s.replace('/math ','')
    hw[8] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['mus'])
def hw0(message):
    s = message.text
    s = s.replace('/mus ','')
    hw[9] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['obs'])
def hw0(message):
    s = message.text
    s = s.replace('/obs ','')
    hw[10] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['rl1'])
def hw0(message):
    s = message.text
    s = s.replace('/rl1 ','')
    hw[11] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['r1'])
def hw0(message):
    s = message.text
    s = s.replace('/r1 ','')
    hw[12] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['rl2'])
def hw0(message):
    s = message.text
    s = s.replace('/rl2 ','')
    hw[13] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['r2'])
def hw0(message):
    s = message.text
    s = s.replace('/r2 ','')
    hw[14] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['rus'])
def hw0(message):
    s = message.text
    s = s.replace('/rus ','')
    hw[15] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['tech'])
def hw0(message):
    s = message.text
    s = s.replace('/tech ','')
    hw[16] = s
    bot.send_message(message.chat.id,'Записано')

@bot.message_handler(commands=['pe'])
def hw0(message):
    s = message.text
    s = s.replace('/pe ','')
    hw[17] = s
    bot.send_message(message.chat.id,'Записано')


ban = ['','','','','','','','','','','','']
@bot.message_handler(commands=['ban1'])
def hw0(message):
    s = message.text
    s = s.replace('/ban1 ','')
    ban[1] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban2'])
def hw0(message):
    s = message.text
    s = s.replace('/ban2 ','')
    ban[2] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban3'])
def hw0(message):
    s = message.text
    s = s.replace('/ban3 ','')
    ban[3] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban4'])
def hw0(message):
    s = message.text
    s = s.replace('/ban4 ','')
    ban[4] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban5'])
def hw0(message):
    s = message.text
    s = s.replace('/ban5 ','')
    ban[5] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban6'])
def hw0(message):
    s = message.text
    s = s.replace('/ban6 ','')
    ban[6] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban7'])
def hw0(message):
    s = message.text
    s = s.replace('/ban7 ','')
    ban[7] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban8'])
def hw0(message):
    s = message.text
    s = s.replace('/ban8 ','')
    ban[8] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban9'])
def hw0(message):
    s = message.text
    s = s.replace('/ban9 ','')
    ban[9] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['ban10'])
def hw0(message):
    s = message.text
    s = s.replace('/ban10 ','')
    ban[10] = int(s)
    bot.send_message(message.chat.id,'BAN')

@bot.message_handler(commands=['myname'])
def username(message):
    s = message.text
    s = s.replace('/myname','')
    if s == '':
        bot.send_message(message.chat.id,'Неверное заполнение, попробуйте еще раз.')
    else:
        f = open("id.txt", "a")
        f.write('name: ' + s + ' id: ' + str(message.chat.id) + ' .                             ')
        f.close()
        bot.send_message(message.chat.id,'Чел харош,теперь мы следим за тобой. Если '
                                         'заполнение будет неверным вас могут забанить, но не сразу.')


@bot.message_handler(commands=['users'])
def users(message):
    bot.send_message(message.chat.id,'Сначала работы нашим ботом воспользывались ' + str(custn) + ' id.')


mon = '-'
tue = '-'
wed = '-'
thu = '-'
fri = '-'
sat = '-'




mn = ['Рус.яз','Био','Рус.яз','Гео','Физ-ра','Англ.яз/Техн','Англ.яз/Техн','Род/Тур .яз']
tu = ['Род.яз','Матем','Алго/Матем','Алго/Матем','Матем/Алго','Матем.Алго','Тур.яз/Род.лит','Лит-ра']
wd = ['Рус.яз','ИЗО','Истор','Род.лит/Тур.яз','Техн/Англ.яз','Техн/Англ.яз','Рус.яз','Физ-ра']
th = ['Физ-ра','Англ.яз','Матем','Алго/Инф','Алго/Инф','Матем/Алго','Матем.Алго','Физ-ра']
fr = ['Тур/Род .яз','Англ','Англ','Матем','КЧ','Истор','Рус.яз','Лит-ра']
st = ['Муз','Общество','Матем','Рус.яз','Лит-ра','Матем']

@bot.message_handler(content_types=['text'])
def ans(message):
    global messages
    messages = messages + 1
    global nws1
    global nws2
    global nws3
    global nws4
    global nws5
    global user
    global stu
    global mon
    global tue
    global wed
    global thu
    global fri
    global sat
    global stu
    global mrk
    global ban
    global cust
    global custn

    if message.chat.id in cust:
        custn = custn

    else:
        custn = custn + 1
        cust[custn-1] = message.chat.id
        bot.send_message(message.chat.id, 'Привет, я обновился до версии 1.3. '
                                          'Теперь ты сможешь узнать у меня расписание. '
                                          'Так же теперь мы следим за тобой активнее))), но это не важно. '
                                          'К сожалению из-за многочисленного спама и указания ложной '
                                          'информации мы не смогли коректно собрать ваши telegram_id, '
                                          'поэтому просьба повторить авторизацию, нажав "сообщить_свой_id" и '
                                          'выполнив действия указанные там, '
                                          'ДЕЛАЙТЕ ЭТО ВНИМАТЕЛЬНЕЕ, за указание ложной информации БАН(1день)!!!',reply_markup=menu)


    if message.chat.id == ban[1] or message.chat.id == ban[2] or message.chat.id == ban[3] or message.chat.id == ban[4]or message.chat.id == ban[5] or message.chat.id == ban[6] or message.chat.id == ban[7] or message.chat.id == ban[8] or message.chat.id == ban[9] or message.chat.id == ban[10]:
        bot.send_message(message.chat.id,'Вы забанены',reply_markup=bm)
    else:
        f = open("users.txt", "a")
        f.write('id: ' + str(message.chat.id) + '.                             ')
        f.close()
        f = open("mes.txt", "a")
        f.write('id: ' + str(message.chat.id) + ' mes: ' + message.text +'.                             ')
        f.close()

        print('Отправлено сообщение пользователем с id: ' + str(message.chat.id) + '.  ')
        if message.text == 'Новости':
            bot.send_message(message.chat.id,'1. ' + nws1)
            bot.send_message(message.chat.id, '2. ' + nws2)
            bot.send_message(message.chat.id, '3. ' + nws3)
            bot.send_message(message.chat.id, '4. ' + nws4)
            bot.send_message(message.chat.id, '5. ' + nws5)
        if message.text == 'Дежурство':
            bot.send_message(message.chat.id, 'ДЕЖУРНЫЕ НА ЭТОЙ НЕДЕЛЕ:')
            bot.send_message(message.chat.id, 'ПН.' + mon)
            bot.send_message(message.chat.id, 'ВТ.' + tue)
            bot.send_message(message.chat.id, 'СР.' + wed)
            bot.send_message(message.chat.id, 'ЧТ.' + thu)
            bot.send_message(message.chat.id, 'ПТ.' + fri)
            bot.send_message(message.chat.id, 'СБ.' + sat)
        if message.text == 'GradeGames':
            for i in range(23):
                bot.send_message(message.chat.id,'Ученик: ' + stu[i] + ';  Количество пятерок: ' + mrk[i] + ';')
        if message.text == 'Сообщить_о_болезни':
            bot.send_message(message.chat.id,'Напишите в чат:"/ill + ваше ФИ(через пробел)"')
        if message.text == 'Расписание':
            bot.send_message(message.chat.id, 'Выберите день.',reply_markup=week)


        if message.text == 'ПН':
            sub = 0
            for i in range(8):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' + mn[sub-1])
        elif message.text == 'ВТ':
            sub = 0
            for i in range(8):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' +  tu[sub-1])
        elif message.text == 'СР':
            sub = 0
            for i in range(8):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' +  wd[sub-1])
        elif message.text == 'ЧТ':
            sub = 0
            for i in range(8):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' +  th[sub-1])
        elif message.text == 'ПТ':
            sub = 0
            for i in range(8):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' +  fr[sub-1])
        elif message.text == 'СБ':
            sub = 0
            for i in range(6):
                sub = sub + 1
                bot.send_message(message.chat.id,str(i+1) + '.' +  st[sub-1])



        if message.text == 'ДЗ':
            bot.send_message(message.chat.id,'Выберите предмет',reply_markup=dz)
        if message.text == 'MENU':
            bot.send_message(message.chat.id,'Выполняю',reply_markup=menu)


        if message.text == 'Биология':
            bot.send_message(message.chat.id,'По биологии задали: ' + hw[0])
        elif message.text == 'Турецкий':
            bot.send_message(message.chat.id,'По турецкому задали: ' + hw[1])
        elif message.text == 'География':
            bot.send_message(message.chat.id,'По географии задали: ' + hw[2])
        elif message.text == 'ИЗО':
                bot.send_message(message.chat.id,'По ИЗО задали: ' + hw[3])
        elif message.text == 'Английский(сред)':
            bot.send_message(message.chat.id,'По английскому(ср.группы) задали: ' + hw[4])
        elif message.text == 'Английский(сил)':
            bot.send_message(message.chat.id,'По английскому(сил.группы) задали: ' + hw[5])
        elif message.text == 'История':
            bot.send_message(message.chat.id,'По истории задали: ' + hw[6])
        elif message.text == 'Лит-ра':
            bot.send_message(message.chat.id,'По лит-ре задали: ' + hw[7])
        elif message.text == 'Математика':
            bot.send_message(message.chat.id,'По математике задали: ' + hw[8])
        elif message.text == 'Музыка':
            bot.send_message(message.chat.id,'По музыке задали: ' + hw[9])
        elif message.text == 'Общество':
            bot.send_message(message.chat.id,'По обществу задали: ' + hw[10])
        elif message.text == 'Род.лит(рус)':
            bot.send_message(message.chat.id,'По род.лит(рус) задали: ' + hw[11])
        elif message.text == 'Родной(рус)':
            bot.send_message(message.chat.id,'По родной(рус) задали: ' + hw[12])
        elif message.text == 'Род.лит(тат)':
            bot.send_message(message.chat.id,'По род.лит(тат) задали: ' + hw[13])
        elif message.text == 'Родной(тат)':
            bot.send_message(message.chat.id,'По родной(тат) задали: ' + hw[14])
        elif message.text == 'Рус.яз':
            bot.send_message(message.chat.id,'По рус.яз задали: ' + hw[15])
        elif message.text == 'Технология':
            bot.send_message(message.chat.id,'По технологии задали: ' + hw[16])
        elif message.text == 'Физ-культура':
            bot.send_message(message.chat.id,'По физ-культуре задали: ' + hw[17])

        if message.text == 'Обновить':
            bot.send_message(message.chat.id, 'Вас разбанили',reply_markup=menu)

        if message.text == 'msg':
            bot.send_message(message.chat.id,'С начала работы обработанно ' + str(messages) + ' сообщений.')

        if message.text == 'Сообщить свой id':
            bot.send_message(message.chat.id,'Напиши в чат /myname (тут ваше имя,через пробел).'
                                             'ВНИМАНИЕ!!! За указание ложной инфы-БАН(1день)!'
                                             'Перед баном сообщение проверяют админы,если это было неумышленно '
                                             'бан отменяют!')

bot.polling()