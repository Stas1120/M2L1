import telebot
import os
import random
import requests
images = os.listdir('images')


bot = telebot.TeleBot('')

@bot.message_handler(commands=['meme'])
def send_meme(massege):
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        bot.send_photo(massege.chat.id, f)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['dog'])
def dog(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)

bot.polling()
