
import time
from datetime import datetime
import telebot
bot = telebot.TeleBot('6286862624:AAHsj9VDyFFoCI6mKfAkVubIKgqvSQODi0c')

messages = 0
nms = ['Аккмалутдинов','Бариев','Воробьев','Галаутдинов','Гашигулин','Димухаметов','Загидулин','Закиров','Замалиев','Ильин',
         'Исмагилов','Леухин','Лукьянов','Мифтахов','МустафинК','МустафинС','Мухаметгалиев','ПимурзинРусл',
         'ПимурзинРуст','Сахабутдинов','Фаизов','Фазлиев','Хамидулин','Шамсиев','Юсупов']
ind = [1303460009,1735288618,1153400878,1668851054,1203352160,1082861746,2049380647,1612294989,1196509690,
       0,1202390893,1118648643,1463862718,1388947413,761831397,1958898376,1644355420,
       1433174395,1349375141,1332512027,1310469611,1298983887,1200998361,1351307952,0,0,0,0,0,0,0]



bot.send_message(1388947413,'Я работаю!')






f = open("users.txt", "w")
f.write('')
f.close()


send = telebot.types.ReplyKeyboardMarkup()
send.add('Отправить')


bm = telebot.types.ReplyKeyboardMarkup()
bm.add('Вы забанены!')
bm.add('Обновить','Протествовать!')

bm2 = telebot.types.ReplyKeyboardMarkup()
bm2.add('Вы забанены!')
bm2.add('Обновить')



p = telebot.types.ReplyKeyboardMarkup()
p.add('Вам пришло push уведомление,вы его прочитали?')
p .add('Я прочитал!')

menu = telebot.types.ReplyKeyboardMarkup()
menu.add('Расписание')
menu.add('ДЗ','Дежурство')
menu.add('Новости','События')
menu.add('Сообщить_о_болезни')


sign = telebot.types.ReplyKeyboardMarkup()
sign.add('Подтверждаю','Отмена')


dev = telebot.types.ReplyKeyboardMarkup()
dev.add('CheckData','CheckErr')
dev.add('users','msg')
dev.add('SendStartMes','StopSendStartMes')
dev.add('Reset','MENU')


dz = telebot.types.ReplyKeyboardMarkup()
dz.add('Биология')
dz.add('Турецкий(рус)')
dz.add('Турецкий(тат)')
dz.add('География')
dz.add('ИЗО')
dz.add('Английский(сред)')
dz.add('Английский(сил)')
dz.add('История')
dz.add('Лит-ра')
dz.add('Алгебра')
dz.add('Геометрия')
dz.add('Музыка')
dz.add('Общество')
dz.add('Род.лит(рус)')
dz.add('Родной(рус)')
dz.add('Род.лит(тат)')
dz.add('Родной(тат)')
dz.add('Рус.яз')
dz.add('Технология')
dz.add('Физ-культура')
dz.add('Физика')
dz.add('Информатика')
dz.add('MENU')


names = telebot.types.ReplyKeyboardMarkup()
names.add('Аккмалутдинов')
names.add('Бариев')
names.add('Воробьев')
names.add('Галаутдинов')
names.add('Гашигулин')
names.add('Димухаметов')
names.add('Загидулин')
names.add('Закиров')
names.add('Ильин')
names.add('Исмагилов')
names.add('Леухин')
names.add('Лукьянов')
names.add('Мифтахов')
names.add('МустафинК')
names.add('МустафинС')
names.add('Мухаметгалиев')
names.add('ПимурзинРусл')
names.add('ПимурзинРуст')
names.add('Сахабутдинов')
names.add('Фаизов')
names.add('Фазлиев')
names.add('Хамидулин')
names.add('Шамсиев')
names.add('Юсупов')
names.add('MENU')



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
    bot.send_message(message.chat.id, 'Привет,это EvoBot', reply_markup=menu)





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
    f = open("nws1.txt", "w")
    f.write(nws1)
    f.close()

@bot.message_handler(commands=['nws2'])
def new(message):
    global nws2
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws2 = nws.replace('/nws2 ','')
    f = open("nws2.txt", "w")
    f.write(nws2)
    f.close()

@bot.message_handler(commands=['nws3'])
def new(message):
    global nws3
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws3 = nws.replace('/nws3 ','')
    f = open("nws3.txt", "w")
    f.write(nws3)
    f.close()

@bot.message_handler(commands=['nws4'])
def new(message):
    global nws4
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws4 = nws.replace('/nws4 ','')
    f = open("nws4.txt", "w")
    f.write(nws4)
    f.close()

@bot.message_handler(commands=['nws5'])
def new(message):
    global nws5
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    nws = message.text
    nws5 = nws.replace('/nws5 ','')
    f = open("nws5.txt", "w")
    f.write(nws5)
    f.close()


@bot.message_handler(commands=['event'])
def new(message):
    global ev
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    ev = message.text
    ev = ev.replace('/event ','')
    f = open("event.txt", "w")
    f.write(ev)
    f.close()



@bot.message_handler(commands=['push'])
def new(message):
    global nws5
    bot.send_message(message.chat.id, 'Милисекунду,мне нужно обработать ваше сообщение')
    pushs = message.text
    pushs = pushs.replace('/push ','')
    bot.send_message(message.chat.id, 'Начинается рассылка')
    for i in range(25):
        if ind[i-1] > 0:
            bot.send_message(ind[i-1], "Вам пришло новое push уведомление:",reply_markup = p)
            bot.send_message(ind[i-1], pushs)
            bot.send_message(message.chat.id, "Отправленно")
            print(ind[i-1])
        else:
            bot.send_message(message.chat.id,"Не указан id")
    bot.send_message(message.chat.id, 'Рассылка окончена')


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
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[0] = 0
    senddez2[0] = 0
    dez[0] = ''
    dn = 0
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


@bot.message_handler(commands=['tue'])
def tue(message):
    global tue
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[1] = 0
    senddez2[1] = 0
    dez[1] = ''
    dn = 1
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


@bot.message_handler(commands=['wed'])
def wed(message):
    global wed
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[2] = 0
    senddez2[2] = 0
    dez[2] = ''
    dn = 2
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


@bot.message_handler(commands=['thu'])
def thu(message):
    global thu
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[3] = 0
    senddez2[3] = 0
    dez[3] = ''
    dn = 3
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


@bot.message_handler(commands=['fri'])
def fri(message):
    global fri
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[4] = 0
    senddez2[4] = 0
    dez[4] = ''
    dn = 4
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


@bot.message_handler(commands=['sat'])
def sat(message):
    global sat
    global dn
    global dez
    global senddez1
    global senddez2
    senddez1[5] = 0
    senddez2[5] = 0
    dez[5] = ''
    dn = 5
    senddez1[dn] = 0
    senddez2[dn] = 0
    bot.send_message(message.chat.id, 'Выберите дежурного',reply_markup=names)


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
    f = open("bio.txt", "w")
    f.write(hw[0])
    f.close()

@bot.message_handler(commands=['tur1'])
def hw0(message):
    s = message.text
    s = s.replace('/tur1 ','')
    hw[1] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("tur1.txt", "w")
    f.write(hw[1])
    f.close()

@bot.message_handler(commands=['tur2'])
def hw0(message):
    s = message.text
    s = s.replace('/tur2 ','')
    hw[2] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("tur2.txt", "w")
    f.write(hw[2])
    f.close()

@bot.message_handler(commands=['geo'])
def hw0(message):
    s = message.text
    s = s.replace('/geo ','')
    hw[3] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("geo.txt", "w")
    f.write(hw[3])
    f.close()

@bot.message_handler(commands=['art'])
def hw0(message):
    s = message.text
    s = s.replace('/art ','')
    hw[4] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("art2.txt", "w")
    f.write(hw[4])
    f.close()

@bot.message_handler(commands=['eng1'])
def hw0(message):
    s = message.text
    s = s.replace('/eng1 ','')
    hw[5] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("eng2.txt", "w")
    f.write(hw[5])
    f.close()

@bot.message_handler(commands=['eng2'])
def hw0(message):
    s = message.text
    s = s.replace('/eng2 ','')
    hw[6] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("eng2.txt", "w")
    f.write(hw[6])
    f.close()

@bot.message_handler(commands=['his'])
def hw0(message):
    s = message.text
    s = s.replace('/his ','')
    hw[7] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("his.txt", "w")
    f.write(hw[7])
    f.close()

@bot.message_handler(commands=['lit'])
def hw0(message):
    s = message.text
    s = s.replace('/lit ','')
    hw[8] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("lit.txt", "w")
    f.write(hw[8])
    f.close()

@bot.message_handler(commands=['alge'])
def hw0(message):
    s = message.text
    s = s.replace('/alge ','')
    hw[29] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("algeb.txt", "w")
    f.write(hw[29])
    f.close()

@bot.message_handler(commands=['geom'])
def hw0(message):
    s = message.text
    s = s.replace('/geom ', '')
    hw[30] = s
    bot.send_message(message.chat.id, 'Записано')
    f = open("geom.txt", "w")
    f.write(hw[30])
    f.close()

@bot.message_handler(commands=['mus'])
def hw0(message):
    s = message.text
    s = s.replace('/mus ','')
    hw[10] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("mus.txt", "w")
    f.write(hw[10])
    f.close()

@bot.message_handler(commands=['obs'])
def hw0(message):
    s = message.text
    s = s.replace('/obs ','')
    hw[11] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("obs.txt", "w")
    f.write(hw[11])
    f.close()

@bot.message_handler(commands=['rl1'])
def hw0(message):
    s = message.text
    s = s.replace('/rl1 ','')
    hw[12] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("rl1.txt", "w")
    f.write(hw[12])
    f.close()

@bot.message_handler(commands=['r1'])
def hw0(message):
    s = message.text
    s = s.replace('/r1 ','')
    hw[13] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("r1.txt", "w")
    f.write(hw[13])
    f.close()

@bot.message_handler(commands=['rl2'])
def hw0(message):
    s = message.text
    s = s.replace('/rl2 ','')
    hw[14] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("rl2.txt", "w")
    f.write(hw[14])
    f.close()

@bot.message_handler(commands=['r2'])
def hw0(message):
    s = message.text
    s = s.replace('/r2 ','')
    hw[15] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("r2.txt", "w")
    f.write(hw[15])
    f.close()

@bot.message_handler(commands=['rus'])
def hw0(message):
    s = message.text
    s = s.replace('/rus ','')
    hw[16] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("rus.txt", "w")
    f.write(hw[16])
    f.close()

@bot.message_handler(commands=['tech'])
def hw0(message):
    s = message.text
    s = s.replace('/tech ','')
    hw[17] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("tech.txt", "w")
    f.write(hw[17])
    f.close()

@bot.message_handler(commands=['pe'])
def hw0(message):
    s = message.text
    s = s.replace('/pe ','')
    hw[18] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("pe.txt", "w")
    f.write(hw[18])
    f.close()


@bot.message_handler(commands=['info'])
def hw0(message):
    s = message.text
    s = s.replace('/info ','')
    hw[20] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("inform.txt", "w")
    f.write(hw[20])
    f.close()


@bot.message_handler(commands=['phys'])
def hw0(message):
    s = message.text
    s = s.replace('/phys ','')
    hw[19] = s
    bot.send_message(message.chat.id,'Записано')
    f = open("phys.txt", "w")
    f.write(hw[19])
    f.close()

ban = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
@bot.message_handler(commands=['ban1'])
def hw0(message):
    s = message.text
    s = s.replace('/ban1 ','')
    ban[1] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban1.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban2'])
def hw0(message):
    s = message.text
    s = s.replace('/ban2 ','')
    ban[2] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban2.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban3'])
def hw0(message):
    s = message.text
    s = s.replace('/ban3 ','')
    ban[3] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban3.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban4'])
def hw0(message):
    s = message.text
    s = s.replace('/ban4 ','')
    ban[4] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban4.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban5'])
def hw0(message):
    s = message.text
    s = s.replace('/ban5 ','')
    ban[5] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban5.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban6'])
def hw0(message):
    s = message.text
    s = s.replace('/ban6 ','')
    ban[6] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban6.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban7'])
def hw0(message):
    s = message.text
    s = s.replace('/ban7 ','')
    ban[7] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban7.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban8'])
def hw0(message):
    s = message.text
    s = s.replace('/ban8 ','')
    ban[8] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban8.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban9'])
def hw0(message):
    s = message.text
    s = s.replace('/ban9 ','')
    ban[9] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban9.txt", "w")
    f.write(s)
    f.close()

@bot.message_handler(commands=['ban10'])
def hw0(message):
    s = message.text
    s = s.replace('/ban10 ','')
    ban[10] = int(s)
    bot.send_message(message.chat.id,'BAN')
    f = open("ban10.txt", "w")
    f.write(s)
    f.close()


#@bot.message_handler(commands=['myname'])
#def username(message):
#    s = message.text
#    s = s.replace('/myname','')
#    if s == '':
#        bot.send_message(message.chat.id,'Неверное заполнение, попробуйте еще раз.')
#    else:
#        f = open("id.txt", "a")
#        f.write('name: ' + s + ' id: ' + str(message.chat.id) + ' .                             ')
#        f.close()
#        bot.send_message(message.chat.id,'Чел харош,теперь мы следим за тобой. Если '
#                                         'заполнение будет неверным вас могут забанить, но не сразу.')



@bot.message_handler(commands=['dev'])
def otsut(message):
    if message.chat.id == 1388947413:
        bot.send_message(message.chat.id,'Developer keyboard open',reply_markup=dev)

@bot.message_handler(commands=['bantime'])
def otsut(message):
    global bntm
    bntm = message.text
    bntm = bntm.replace('/bantime ', '')
    bntm = float(bntm)
    print(bntm)
    bot.send_message(message.chat.id,'Установленно!')



def reset():
    global dez
    global senddez1
    global senddez2
    global x
    global msid
    global mstm

    dez = ['', '', '', '', '', '']
    senddez1 = [0, 0, 0, 0, 0, 0, 0, 0]
    senddez2 = [0, 0, 0, 0, 0, 0]
    msid = ['','','','','']
    mstm = ['', '', '', '', '']
    x = ['', '', '', '', '']


    f = open("event.txt", "w")
    f.write('')
    f.close()

    f = open("bio.txt", "w")
    f.write('')
    f.close()

    f = open("tur1.txt", "w")
    f.write('')
    f.close()

    f = open("tur2.txt", "w")
    f.write('')
    f.close()
    f = open("geo.txt", "w")
    f.write('')
    f.close()

    f = open("art.txt", "w")
    f.write('')
    f.close()

    f = open("eng1.txt", "w")
    f.write('')
    f.close()

    f = open("eng2.txt", "w")
    f.write('')
    f.close()

    f = open("his.txt", "w")
    f.write('')
    f.close()

    f = open("his.txt", "w")
    f.write('')
    f.close()

    f = open("math.txt", "w")
    f.write('')
    f.close()

    f = open("mus.txt", "w")
    f.write('')
    f.close()

    f = open("obs.txt", "w")
    f.write('')
    f.close()

    f = open("rl1.txt", "w")
    f.write('')
    f.close()

    f = open("r1.txt", "w")
    f.write('')
    f.close()

    f = open("rl2.txt", "w")
    f.write('')
    f.close()

    f = open("r2.txt", "w")
    f.write('')
    f.close()

    f = open("rus.txt", "w")
    f.write('')
    f.close()

    f = open("tech.txt", "w")
    f.write('')
    f.close()

    f = open("pe.txt", "w")
    f.write('')
    f.close()


    f = open("mon.txt", "w")
    f.write('')
    f.close()

    f = open("tue.txt", "w")
    f.write('')
    f.close()

    f = open("wed.txt", "w")
    f.write('')
    f.close()

    f = open("thu.txt", "w")
    f.write('')
    f.close()

    f = open("fri.txt", "w")
    f.write('')
    f.close()

    f = open("sat.txt", "w")
    f.write('')
    f.close()


    f = open("nws1.txt", "w")
    f.write('')
    f.close()

    f = open("nws2.txt", "w")
    f.write('')
    f.close()

    f = open("nws3.txt", "w")
    f.write('')
    f.close()

    f = open("nws4.txt", "w")
    f.write('')
    f.close()

    f = open("nws5.txt", "w")
    f.write('')
    f.close()


    f = open("StartMSG.txt", "w")
    f.write('0')
    f.close()


    f = open("bio.txt", "r")
    hw[0] = f.read()
    f.close()
    f = open("tur1.txt", "r")
    hw[1] = f.read()
    f.close()
    f = open("tur2.txt", "r")
    hw[2] = f.read()
    f.close()
    f = open("geo.txt", "r")
    hw[3] = f.read()
    f.close()
    f = open("art.txt", "r")
    hw[4] = f.read()
    f.close()
    f = open("eng1.txt", "r")
    hw[5] = f.read()
    f.close()
    f = open("eng2.txt", "r")
    hw[6] = f.read()
    f.close()
    f = open("his.txt", "r")
    hw[7] = f.read()
    f.close()
    f = open("his.txt", "r")
    hw[8] = f.read()
    f.close()
    f = open("math.txt", "r")
    hw[9] = f.read()
    f.close()
    f = open("mus.txt", "r")
    hw[10] = f.read()
    f.close()
    f = open("obs.txt", "r")
    hw[11] = f.read()
    f.close()
    f = open("rl1.txt", "r")
    hw[12] = f.read()
    f.close()
    f = open("r1.txt", "r")
    hw[13] = f.read()
    f.close()
    f = open("rl2.txt", "r")
    hw[14] = f.read()
    f.close()
    f = open("r2.txt", "r")
    hw[15] = f.read()
    f.close()
    f = open("rus.txt", "r")
    hw[16] = f.read()
    f.close()
    f = open("tech.txt", "r")
    hw[17] = f.read()
    f.close()
    f = open("pe.txt", "r")
    hw[18] = f.read()
    f.close()


    f = open("mon.txt", "r")
    mon = f.read()
    f.close()
    f = open("tue.txt", "r")
    tue = f.read()
    f.close()
    f = open("wed.txt", "r")
    wed = f.read()
    f.close()
    f = open("thu.txt", "r")
    thu = f.read()
    f.close()
    f = open("fri.txt", "r")
    fri = f.read()
    f.close()
    f = open("sat.txt", "r")
    sat = f.read()
    f.close()


    f = open("nws1.txt", "r")
    nws1 = f.read()
    f.close()
    f = open("nws2.txt", "r")
    nws2 = f.read()
    f.close()
    f = open("nws3.txt", "r")
    nws3 = f.read()
    f.close()
    f = open("nws4.txt", "r")
    nws4 = f.read()
    f.close()
    f = open("nws5.txt", "r")
    nws5 = f.read()
    f.close()

    f = open("StartMSG.txt", "r")
    StartMSG = f.read()
    f.close()



def data(message):
    global messages
    global nws1
    global nws2
    global nws3
    global nws4
    global nws5
    global ev
    global user
    global stu
    global stu
    global mrk
    global ban
    global cust
    global custn
    global StartMSG
    global dez
    global starttm
    global senddez1
    global senddez2
    global dn
    global msid
    global mstm
    global x
    global bmid
    global bans
    global bntm
    bot.send_message(1388947413,"DATA:")
    time.sleep(0.2)
    bot.send_message(1388947413, "messages = " + str(messages))
    time.sleep(0.2)
    bot.send_message(1388947413, "nws1 = " + nws1)
    time.sleep(0.2)
    bot.send_message(1388947413, "nws2 = " + nws2)
    time.sleep(0.2)
    bot.send_message(1388947413, "nws3 = " + nws3)
    time.sleep(0.2)
    bot.send_message(1388947413, "nws4 = " + nws4)
    time.sleep(0.2)
    bot.send_message(1388947413, "nws5 = " + nws5)
    time.sleep(0.2)
    bot.send_message(1388947413, "stu = " + str(stu))
    time.sleep(0.2)
    bot.send_message(1388947413, "dez = " + str(dez))
    time.sleep(0.2)
    bot.send_message(1388947413, "mrk = " + str(mrk))
    time.sleep(0.2)
    bot.send_message(1388947413, "ban = " + str(ban))
    time.sleep(0.2)
    bot.send_message(1388947413, "cust = " +    str(cust))
    time.sleep(0.2)
    bot.send_message(1388947413, "custn = " + str(custn))
    time.sleep(0.2)
    bot.send_message(1388947413, "StartMSG = " + str(StartMSG))
    time.sleep(0.2)
    bot.send_message(1388947413, "hw = " + str(hw))
    time.sleep(0.2)
    bot.send_message(1388947413, "x = " + str(x))
    time.sleep(0.2)
    bot.send_message(1388947413, "mstm = " + str(mstm))
    time.sleep(0.2)
    bot.send_message(1388947413, "msid = " + str(msid))
    time.sleep(0.2)
    bot.send_message(1388947413, "dn = " + str(dn))
    time.sleep(0.2)
    bot.send_message(1388947413, "senddez1 = " + str(senddez1))
    time.sleep(0.2)
    bot.send_message(1388947413, "senddez2 = " + str(senddez2))
    time.sleep(0.2)
    bot.send_message(1388947413, "starttm = " +  str(starttm))
    time.sleep(0.2)
    bot.send_message(1388947413, "sending finished",reply_markup=dev)


dez = ['','','','','','']
senddez1 = [0,0,0,0,0,0,0,0]
senddez2 = [0,0,0,0,0,0]


mon = '-'
tue = '-'
wed = '-'
thu = '-'
fri = '-'
sat = '-'
bntm = 0.6


mn = ['Рус.яз','Био','Рус.яз','Гео','Физ-ра','Англ.яз/Техн','Англ.яз/Техн','Род/Тур .яз']
tu = ['Род.яз','Матем','Алго/Матем','Алго/Матем','Матем/Алго','Матем/Алго','Тур.яз/Род.лит','Лит-ра']
wd = ['Рус.яз','ИЗО','Истор','Род.лит/Тур.яз','Техн/Англ.яз','Техн/Англ.яз','Рус.яз','Физ-ра']
th = ['Физ-ра','Англ.яз','Матем','Алго/Инф','Алго/Инф','Матем/Алго','Матем/Алго','Физ-ра']
fr = ['Тур/Род .яз','Англ','Англ','Матем','КЧ','Истор','Рус.яз','Лит-ра']
st = ['Муз','Общество','Матем','Рус.яз','Лит-ра','Матем']



f = open("bio.txt", "r")
hw[0] = f.read()
f.close()
f = open("tur1.txt", "r")
hw[1] = f.read()
f.close()
f = open("tur2.txt", "r")
hw[2] = f.read()
f.close()
f = open("geo.txt", "r")
hw[3] = f.read()
f.close()
f = open("art.txt", "r")
hw[4] = f.read()
f.close()
f = open("eng1.txt", "r")
hw[5] = f.read()
f.close()
f = open("eng2.txt", "r")
hw[6] = f.read()
f.close()
f = open("his.txt", "r")
hw[7] = f.read()
f.close()
f = open("his.txt", "r")
hw[8] = f.read()
f.close()
f = open("algeb.txt", "r")
hw[29] = f.read()
f.close()
f = open("geom.txt", "r")
hw[30] = f.read()
f.close()
f = open("mus.txt", "r")
hw[10] = f.read()
f.close()
f = open("obs.txt", "r")
hw[11] = f.read()
f.close()
f = open("rl1.txt", "r")
hw[12] = f.read()
f.close()
f = open("r1.txt", "r")
hw[13] = f.read()
f.close()
f = open("rl2.txt", "r")
hw[14] = f.read()
f.close()
f = open("r2.txt", "r")
hw[15] = f.read()
f.close()
f = open("rus.txt", "r")
hw[16] = f.read()
f.close()
f = open("tech.txt", "r")
hw[17] = f.read()
f.close()
f = open("pe.txt", "r")
hw[18] = f.read()
f.close()
f = open("phys.txt", "r")
hw[19] = f.read()
f.close()
f = open("inform.txt", "r")
hw[20] = f.read()
f.close()


f = open("dn0.txt", "r")
dez[0] = f.read()
f.close()
f = open("dn1.txt", "r")
dez[1] = f.read()
f.close()
f = open("dn2.txt", "r")
dez[2] = f.read()
f.close()
f = open("dn3.txt", "r")
dez[3] = f.read()
f.close()
f = open("dn4.txt", "r")
dez[4] = f.read()
f.close()
f = open("dn5.txt", "r")
dez[5] = f.read()
f.close()


f = open("nws1.txt", "r")
nws1 = f.read()
f.close()
f = open("nws2.txt", "r")
nws2 = f.read()
f.close()
f = open("nws3.txt", "r")
nws3 = f.read()
f.close()
f = open("nws4.txt", "r")
nws4 = f.read()
f.close()
f = open("nws5.txt", "r")
nws5 = f.read()
f.close()

f = open("ban1.txt", "r")
ban[1] = f.read()
f.close()
f = open("ban2.txt", "r")
ban[2] = f.read()
f.close()
f = open("ban3.txt", "r")
ban[3] = f.read()
f.close()
f = open("ban4.txt", "r")
ban[4] = f.read()
f.close()
f = open("ban5.txt", "r")
ban[5] = f.read()
f.close()
f = open("ban6.txt", "r")
ban[6] = f.read()
f.close()
f = open("ban7.txt", "r")
ban[7] = f.read()
f.close()
f = open("ban8.txt", "r")
ban[8] = f.read()
f.close()
f = open("ban9.txt", "r")
ban[9] = f.read()
f.close()
f = open("ban10.txt", "r")
ban[10] = f.read()
f.close()

f = open("event.txt", "r")
ev = f.read()
f.close()

f = open("StartMSG.txt", "r")
StartMSG = f.read()
f.close()

msid = [0,0,0,0,0,0,0,0,0,0]
mstm = [0,0,0,0,0,0,0,0,0,0]
bans = 10
dn = 0
now = datetime.now()
starttm = now.timestamp()



@bot.message_handler(content_types=['text'])
def ans(message):
    global messages
    messages = messages + 1
    global nws1
    global nws2
    global nws3
    global nws4
    global nws5
    global ev
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
    global StartMSG
    global dez
    global starttm
    global senddez1
    global senddez2
    global dn
    global msid
    global mstm
    global x
    global bmid
    global bans
    global bntm

    now = datetime.now()

    if message.text == 'Протествовать!':
        bmid = message.chat.id
        bot.send_message(message.chat.id, "Ваш протест отправлен и будет рассмотрен через некоторое время!",
                         reply_markup=bm2)
        if bmid in ind:
            indx = ind.index(bmid)
            indx = nms[indx]
        else:
            indx = "Неизвестный"
        bot.send_message(1388947413, indx + " просит рассмотреть верность его бана!")  # 1202390893



    msid[5] = msid[4]
    msid[4] = msid[3]
    msid[3] = msid[2]
    msid[2] = msid[1]
    msid[1] = msid[0]
    msid[0] = message.chat.id

    mstm[5] = mstm[4]
    mstm[4] = mstm[3]
    mstm[3] = mstm[2]
    mstm[2] = mstm[1]
    mstm[1] = mstm[0]
    mstm[0] = now.timestamp()
    x = [i for i, ltr in enumerate(msid) if ltr == msid[0]]
    if len(x) > 2 and mstm[0]-starttm > 60:
        n1 = x[0]
        n2 = x[1]
        n3 = x[2]
        min = mstm[n1] - mstm[n2]
        min2 = mstm[n2] - mstm[n3]
        if min < bntm and min2 < bntm and min > 0.2:
            bans = bans + 1
            if bans == 11:
                bans = 1
            ban[bans] = message.chat.id



   # d = now.weekday()
   # if d == 6:
   #     dez = ['', '', '', '', '', '']
   #     senddez1 = [0, 0, 0, 0, 0, 0,0,0]
   #     senddez2 = [0, 0, 0, 0, 0, 0]
   # else:
   #     if senddez1[d+1] == 0:
   #         if dez[d+1] in nms:
   #             ix = nms.index(dez[d+1])
   #             mid = ind[ix]
   #             senddez1[d+1] = 1
   #             id = 0
   #             if id != 0 :
   #                 bot.send_message(mid,"Привет,завтра ты дежурный!)")
   #             else:
   #                 bot.send_message(1202390893,dez[d+1] + ' не указал свой id, пожалуйста'
   #                                                'сообщите ему о том, что он завтра дежурный!')
#
   #
   #     if senddez2[d] == 0:
   #         if dez[d] in nms:
   #             ix = nms.index(dez[d])
   #             mid = ind[ix]
   #             senddez2[d] = 1
   #             mid = 0
   #             if mid != 0 :
   #                 bot.send_message(mid,"Привет,сегодня ты дежурный!)")
   #             else:
   #                 bot.send_message(1202390893,dez[d+1] + ' не указал свой id, пожалуйста'
   #                                                'сообщите ему о том, что он сегодня дежурный!')



    f = open("StartMSG.txt", "r")
    StartMSG = f.read()
    f.close()

    if message.text != "Протествовать!" and (message.chat.id == ban[1] or message.chat.id == ban[2] or message.chat.id == ban[3] or message.chat.id == ban[4]or message.chat.id == ban[5] or message.chat.id == ban[6] or message.chat.id == ban[7] or message.chat.id == ban[8] or message.chat.id == ban[9] or message.chat.id == ban[10]):
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
        if message.text == 'События':
            bot.send_message(message.chat.id,ev)
        if message.text == 'Дежурство':
            bot.send_message(message.chat.id, 'ДЕЖУРНЫЕ НА ЭТОЙ НЕДЕЛЕ:')
            bot.send_message(message.chat.id, 'ПН.' + dez[0])
            bot.send_message(message.chat.id, 'ВТ.' + dez[1])
            bot.send_message(message.chat.id, 'СР.' + dez[2])
            bot.send_message(message.chat.id, 'ЧТ.' + dez[3])
            bot.send_message(message.chat.id, 'ПТ.' + dez[4])
            bot.send_message(message.chat.id, 'СБ.' + dez[5])
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
        if message.text == 'MENU' or message.text == 'Я прочитал!':
            bot.send_message(message.chat.id,'Выполняю',reply_markup=menu)


        if message.text == 'Биология':
            bot.send_message(message.chat.id,'По биологии задали: ' + hw[0])
        elif message.text == 'Турецкий(рус)':
            bot.send_message(message.chat.id,'По турецкому задали: ' + hw[1])
        elif message.text == 'Турецкий(тат)':
            bot.send_message(message.chat.id, 'По турецкому задали: ' + hw[2])
        elif message.text == 'География':
            bot.send_message(message.chat.id,'По географии задали: ' + hw[3])
        elif message.text == 'ИЗО':
                bot.send_message(message.chat.id,'По ИЗО задали: ' + hw[4])
        elif message.text == 'Английский(сред)':
            bot.send_message(message.chat.id,'По английскому(ср.группы) задали: ' + hw[5])
        elif message.text == 'Английский(сил)':
            bot.send_message(message.chat.id,'По английскому(сил.группы) задали: ' + hw[6])
        elif message.text == 'История':
            bot.send_message(message.chat.id,'По истории задали: ' + hw[7])
        elif message.text == 'Лит-ра':
            bot.send_message(message.chat.id,'По лит-ре задали: ' + hw[8])
        elif message.text == 'Алгебра':
            bot.send_message(message.chat.id,'По алгебре задали: ' + hw[29])
        elif message.text == 'Геометрия':
            bot.send_message(message.chat.id, 'По геометрии задали: ' + hw[30])
        elif message.text == 'Музыка':
            bot.send_message(message.chat.id,'По музыке задали: ' + hw[10])
        elif message.text == 'Общество':
            bot.send_message(message.chat.id,'По обществу задали: ' + hw[11])
        elif message.text == 'Род.лит(рус)':
            bot.send_message(message.chat.id,'По род.лит(рус) задали: ' + hw[12])
        elif message.text == 'Родной(рус)':
            bot.send_message(message.chat.id,'По родной(рус) задали: ' + hw[13])
        elif message.text == 'Род.лит(тат)':
            bot.send_message(message.chat.id,'По род.лит(тат) задали: ' + hw[14])
        elif message.text == 'Родной(тат)':
            bot.send_message(message.chat.id,'По родной(тат) задали: ' + hw[15])
        elif message.text == 'Рус.яз':
            bot.send_message(message.chat.id,'По рус.яз задали: ' + hw[16])
        elif message.text == 'Технология':
            bot.send_message(message.chat.id,'По технологии задали: ' + hw[17])
        elif message.text == 'Физ-культура':
            bot.send_message(message.chat.id,'По физ-культуре задали: ' + hw[18])
        elif message.text == 'Физика':
            bot.send_message(message.chat.id, 'По физике задали: ' + hw[19])
        elif message.text == 'Информатика':
            bot.send_message(message.chat.id, 'По информатике задали: ' + hw[20])

        if message.text == 'Обновить':
            bot.send_message(message.chat.id, 'Вас разбанили',reply_markup=menu)
        elif message.text == 'Отправить':
            if message.chat.id == 1388947413:
                bot.send_message(message.chat.id,'Отправлено',reply_markup=dev)
            else:
                bot.send_message(message.chat.id,'Отправлено',reply_markup=menu)
        elif message.text == 'users':
            bot.send_message(message.chat.id, 'Сначала работы нашим ботом воспользывались ' + str(custn) + ' id.')
        elif message.text == 'StopSendStartMes':
            StartMSG = 1
            f = open("StartMSG.txt", "w")
            f.write(str(1))
            f.close()
            bot.send_message(message.chat.id, 'No start messages!')
        elif message.text == 'SendStartMes':
            StartMSG = 0
            f = open("StartMSG.txt", "w")
            f.write(str(0))
            f.close()
            bot.send_message(message.chat.id, 'Ok!')
        elif message.text == 'Отмена':
            bot.send_message(message.chat.id, 'Операция отменена', reply_markup=dev)
        elif message.text == 'Подтверждаю':
            bot.send_message(message.chat.id, 'Данные сбрасываются', reply_markup=dev)
            reset()
            cust = ['', '', '', '', '',
                    '', '', '', '', '',
                    '', '', '', '', '',
                    '', '', '', '', '',
                    '', '', '', '', '']
            custn = 0
        elif message.text == 'CheckData':
            data(message.chat.id)
        elif message.text == 'CheckErr':
            bot.send_message(message.chat.id, '!!!Function not found!!!')
        elif message.text == 'Reset':
            bot.send_message(message.chat.id, 'Подтвердите действие!', reply_markup=sign)


        if message.text == 'Аккмалутдинов':
            dez[dn] = 'Аккмалутдинов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Бариев':
            dez[dn] ='Бариев'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Воробьев':
            dez[dn] ='Воробьев'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Галаутдинов ':
            dez[dn] ='Галаутдинов '
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Гашигулин':
            dez[dn] ='Гашигулин'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Димухаметов':
            dez[dn] ='Димухаметов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Загидулин':
            dez[dn] ='Загидулин'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Закиров':
            dez[dn] ='Закиров'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Замалиев':
            dez[dn] ='Замалиев'
            bot.send_message(message.chat.id, 'Замалиев', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Ильин':
            dez[dn] ='Ильин'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Исмагилов':
            dez[dn] ='Исмагилов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()



        elif message.text == 'Леухин':
            dez[dn] ='Леухин'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Лукьянов':
            dez[dn] ='Лукьянов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Мифтахов':
            dez[dn] ='Мифтахов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'МустафинК':
            dez[dn] ='МустафинК'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'МустафинС':
            dez[dn] ='МустафинС'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Мухаметгалиев':
            dez[dn] ='Мухаметгалиев'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'ПимурзинРусл':
            dez[dn] ='ПимурзинРусл'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'ПимурзинРуст':
            dez[dn] ='ПимурзинРуст'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Сахабутдинов':
            dez[dn] ='Сахабутдинов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Фаизов':
            dez[dn] ='Фаизов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Фазлиев':
            dez[dn] ='Фазлиев'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Хамидулин':
            dez[dn] ='Хамидулин'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Шамсиев':
            dez[dn] ='Шамсиев'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()

        elif message.text == 'Юсупов':
            dez[dn] ='Юсупов'
            bot.send_message(message.chat.id, 'Записано', reply_markup = send)
            f = open("dn" + str(dn) + ".txt", "w")
            f.write(dez[dn])
            f.close()








bot.polling()
