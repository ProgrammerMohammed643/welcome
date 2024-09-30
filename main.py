import os
import requests 
import telebot 
from telebot import types
import datetime
from user_agent import generate_user_agent
#تسرق اذكر المصدر @f_r_3_a_o_n
user_agent = generate_user_agent()[0]
id = '6264668799' #Replace This
tok = '7696110235:AAGfHSLfVvH3VUMLahzHNWhHATYuKmxgNkE' #Replace This
zzk = 0
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start(message):
    global zzk
    zzk += 1
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    zxu = datetime.datetime.now()
    tt = f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـ @KOK0KK'''

    key = types.InlineKeyboardMarkup()
    bot.send_message(id, f"<strong>{tt}</strong>", parse_mode="html", reply_markup=key)
    but1 = types.InlineKeyboardButton(text='᥉᥆ᥙᖇᥴᥱ', url='https://t.me/Your_uncle_Muhammad')
    but2 = types.InlineKeyboardButton(text='𝒎𝒐𝒉𝒂𝒎𝒎𝒆𝒅', url='https://t.me/KOK0KK')
    add = types.InlineKeyboardButton(text="💌انشـاء ايميل جديد", callback_data='ansh')
    A = types.InlineKeyboardButton(text="💬البـريد الـوارد ", callback_data='A')
    K = types.InlineKeyboardButton(text="💣حـذف حـسابي", callback_data='AK')
    
    
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(but1, but2, A, K, add)
    bot.send_message(message.chat.id, f"<strong>اهلا بك : | {nm} | في بـوت انشـاء بريد وهمي لاستقبال الاكواد والرسائل للحصول على معلوماتك [ /info ]</strong>", parse_mode="html", reply_markup=maac)

@bot.callback_query_handler(func=lambda call:True)
def st(call):
    if call.data == 'ansh':
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        Az = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اضغط على كلمه [ /gen ]', reply_markup=nc1)
        bot.register_next_step_handler(Az, zd2)
    elif call.data == "A":
        nc1 = types.InlineKeyboardMarkup()
        zd1 = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='اضغط على كلمه [ /get ]', reply_markup=nc1)
        bot.register_next_step_handler(zd1, OZ)
    elif call.data == "AK":
        nc1 = types.InlineKeyboardMarkup(row_width=2)
        MC = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='هل تريد حذف حسابك [ /yes ]', reply_markup=nc1)
        bot.register_next_step_handler(MC, k3)

def zd2(message):
    id2 = str(message.from_user.id)
    ms = message.text
    if '/gen' in ms:
        try:
            os.system(f'rm -rf token{id2}.txt')
            bot.send_message(message.chat.id, f"<strong>جـاري انـشاء ايـميل</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            url = 'https://api.internal.temp-mail.io/api/v3/email/new'
            data = {'name': 'ahmed', 'domain': 'greencafe24.com'}
            headers = {'User-Agent': user_agent}
            response = requests.post(url, data=data, headers=headers)
            result = response.json()
            email = result['email']
            with open(f'token{id2}.txt', 'a') as zaidno:
                zaidno.write(f'{email}')
            z = f"""
 تـم انشـاء بريـد بنـجاح
 ـــــــــــــــــــــــــــــــــــــــ
 الايميل : {email}
 ـــــــــــــــــــــــــــــــــــــــ
 يمكـن الان ارسال كود على البريد واستلامه من قسم الاستلام 
 للرجوع اضغط على
 /start""" 
            bot.send_message(message.chat.id, f"<strong>{z}</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
      
        except Exception as e:
            bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ماا</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    else:
        bot.send_message(message.chat.id, f"<strong> ❗ارسـلت الكـلمه بشـكل خـطأ</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())

def OZ(message):
    try:
        id2 = message.chat.id
        tx = message.text
        if '/get' in tx:
            token = open(f"token{id2}.txt", "r").read()  
            url = f'https://api.internal.temp-mail.io/api/v3/email/{token}/messages'
            messages = requests.get(url).json()
            if messages:
                for msg in messages:
                    bot.send_message(message.chat.id, f"•<strong> الرسالة: {msg['body_text']} لديك \n {msg['subject']}:</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
            else:
                bot.send_message(message.chat.id, "لا يوجد رسائل حاليا")
        else:
            bot.send_message(message.chat.id, f"<strong> ارسـلت الـكلمة بشـكل خطـأ</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
    except Exception as e:
        bot.send_message(message.chat.id, f"<strong>❗ليـس لـديك حسـاب بالـبوت</strong>", parse_mode="html", reply_markup=types.InlineKeyboardMarkup())
        print(e)

def k3(message):
    mg = message.chat.id
    try:
        os.system(f'rm -rf token{mg}.txt')
        key = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, f"<strong>تـم حـذف حسـابك القديم</strong>", parse_mode="html", reply_markup=key)
    except:
        key = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, f"<strong>ليس لديك حساب اساساً</strong>", parse_mode="html", reply_markup=key)    

@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk += 1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـ @KOK0KK''' 
    
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>", parse_mode="html", reply_markup=key) 

while True:
    try:
        bot.infinity_polling()
    except:
        pass
