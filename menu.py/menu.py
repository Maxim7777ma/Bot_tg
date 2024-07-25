import telebot
from telebot import types


bot = telebot.TeleBot('5806987298:AAG22rV5C1QJ_nik-XaIo1FxBPdVE06MW0I')

menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

menu_keyboard.row("Кальяни", "Безалкогольні напої")
menu_keyboard.row("Шоти","Коктелі")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id=message.chat.id
    first_name=message.chat.first_name
    bot.send_message(chat_id, f"¸„.-•~¹°”ˆ˜¨ 🎀 𝒱𝒮𝐸 𝒮𝒱🍑𝐼 🎀 ¨˜ˆ”°¹~•-.„¸\n¸„.•¹°”ˆ 😶‍🌫️вітаємо, ми з України!💨°¹~•.„¸\n   (っ◔◡◔)っ 🎀 ♛🐉 {first_name} 🐉 ♛ 🎀 , \n ♪♫ будь ласка ознайомтесь з меню! ♫♪",reply_markup=menu_keyboard)
    


@bot.message_handler(content_types=["text"])
def send_menu(message):
    if message.text == "Кальяни":
        bot.send_photo(message.chat.id, photo=open(
            "Tabak-420-Light-Line-Yagodnaya-Ghvachka-100-gr.jpg", "rb"), caption="Легкий: 4.20 Light-230 UA ")
        bot.send_photo(message.chat.id, photo=open(
            "Ð±ÑÐ°Ð·Ð¸Ð»ÑÑÐºÐ¸Ð¹_ÑÐ°Ð¹.png", "rb"), caption="Середній: UNITY-290UA")
        bot.send_photo(message.chat.id, photo=open(
            "tabak-dead-horse-Watermelongum-50-gram-306x306.jpg", "rb"), caption="Тяжкий:DEAD HORSE-330UA ")
    
    
    elif message.text == "Коктелі":
            bot.send_photo(message.chat.id, photo=open(
            "long-island-main.jpg", "rb"), caption="Лонг Айленд-180UA ")
            bot.send_photo(message.chat.id, photo=open(
            "олд. феш.webp", "rb"), caption="Олд фешен-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "мохитьо1.jpeg", "rb"), caption="Мохіто-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "маргарита.jpeg", "rb"), caption="Маргарита-130UA ")
            bot.send_photo(message.chat.id, photo=open(
            "krovavaya-meri-retsept.jpg", "rb"), caption="Кровава Мері-130UA ")
            bot.send_photo(message.chat.id, photo=open(
            "голуба.jpeg", "rb"), caption="Голубая лагуна-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "tequila-boom.jpg", "rb"), caption="Текіла Бум-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "pylayuschii-lambordjini-e1572117493189.jpg", "rb"), caption="Палаючий ламборджіні-150UA ")
            bot.send_photo(message.chat.id, photo=open(
            "koktejl-jager-bomb.jpg", "rb"), caption="Ягер бомб-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "хулиган.png", "rb"), caption="Хуліган-120UA ")
           








    elif message.text == "Шоти":
            bot.send_photo(message.chat.id, photo=open(
            "укр.jpeg", "rb"), caption="Український  прапор-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "правий .jpeg", "rb"), caption="Кров руського-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "сос.jpeg", "rb"), caption="Слизькі соски-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "мексиканец.jpeg", "rb"), caption="Зелений мексиканець -120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "б-52.jpeg", "rb"), caption="Б-52-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "хира.jpeg", "rb"), caption="Хіросіма-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "куля.jpeg", "rb"), caption="Срібла куля-120UA ")
            bot.send_photo(message.chat.id, photo=open(
            "вопрос.png", "rb"), caption="Шот від бармена 'Кокосова насолода'-120UA ")
    
    
    elif message.text == "Безалкогольні напої":
            bot.send_photo(message.chat.id, photo=open(
            "cola.jpeg", "rb"), caption="Кола-35UA \n Спрайт-35UA \n Фанта-35UA ")
            bot.send_photo(message.chat.id, photo=open(
            "2023-02-21 00.27.01.jpg", "rb"), caption="Енергетик-40 ")
    
    
    else:
        bot.reply_to(message, "Я не понимаю, что вы хотите сделать. Пожалуйста, выберите опцию из меню.",
                     reply_markup=menu_keyboard)


bot.polling(none_stop=True)

        