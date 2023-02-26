import random
import telebot
import requests

# Crea un objeto de bot con el token de acceso
bot = telebot.TeleBot('5860485494:AAEZ_m44r2pisAow_YSGxlm6XZBejFORqlo')

# Crea una lista de botones
boton_opcion_1 = telebot.types.KeyboardButton('¿Por qué me gustas? 🥰')
boton_opcion_2 = telebot.types.KeyboardButton('Palabras bonitas 💖')
boton_opcion_3 = telebot.types.KeyboardButton('Recuerdos 🧠❣')

# Agrega los botones a una lista
lista_botones = [boton_opcion_1, boton_opcion_2, boton_opcion_3]

# Crea el teclado personalizado con los botones
teclado_personalizado = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teclado_personalizado.add(*lista_botones)

# Crea una función de devolución de llamada para manejar los mensajes entrantes
@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    if message.text == '¿Por qué me gustas? 🥰':
        id = random.randint(1, 100)
        url = f'https://andypoquis.me/reasons-to-loves/{id}'
        response = requests.get(url)
        reasons = response.json()['reasons']
        bot.reply_to(message, reasons)
    elif message.text == 'Palabras bonitas 💖':
        id = random.randint(15, 35)
        url = f'https://andypoquis.me/menssages-loves/{id}'
        response = requests.get(url)
        reasons = response.json()['menssage']
        bot.reply_to(message, reasons)

    elif message.text == 'Recuerdos 🧠❣':
        # Genera un número aleatorio del 1 al 6
        id = random.randint(1, 6)
        # Hace una solicitud a la URL con el número aleatorio como parámetro
        url = f'https://andypoquis.me/memories-to-loves/{id}'
        response = requests.get(url)
        # Obtiene el campo 'menssage' y 'image' del JSON devuelto
        data = response.json()
        menssage = data['menssage']
        image_url = f"https://andypoquis.me{data['image']['url']}"
        # Descarga la imagen
        image_response = requests.get(image_url)
        with open('image.jpg', 'wb') as f:
            f.write(image_response.content)
        # Envía el mensaje con la imagen al chat
        bot.send_photo(message.chat.id, open('image.jpg', 'rb'), caption=menssage)
    else:
        bot.reply_to(message, 'Selecciona una opción del teclado personalizado', reply_markup=teclado_personalizado)

# Ejecuta el bot
bot.polling(none_stop=True)
