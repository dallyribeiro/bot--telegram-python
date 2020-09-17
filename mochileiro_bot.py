import telebot

#Inserir sua chave aqui, quem tem acesso a esse token consegue controlar o bot, cuidado ao compartilhar
KEY = 'SEU TOkEN AQUI'

#Instanciando o bot
bot = telebot.TeleBot(KEY)

#Função que verifica as palavras inseridas e responde com 'Eae'
#Aqui verifica a palavra inserida com a '/' barra (ex: /oi)
@bot.message_handler(commands=['oi', 'Hello', 'Olá', 'Hi'])
def funcao_oi(session):
    print(session)
    bot.reply_to(session, 'Eae')

#Função que verifica a palavra enviada e manda um gif maroto
#Funciona com a barra '/' (ex: /fofo)
@bot.message_handler(commands=['thau', 'fofo', 'camarote', 'preguiça', 'Whow'])
def gatoArcoIres(session):
    if session.text == '/thau':
        gif = 'https://www.mailbiz.com.br/wp-content/uploads/2019/12/tenor.gif'
    elif session.text == '/camarote':
        gif = 'https://i.pinimg.com/originals/d9/69/8f/d9698fb311731c3f01b9f98a68bdcdba.gif'
    elif session.text == '/preguiça':
        gif = 'https://i.giphy.com/media/LTYT5GTIiAMBa/giphy.gif'
    elif session.text == '/Whow':
        gif = 'https://i.giphy.com/media/kKo2x2QSWMNfW/giphy.gif'
    else:
        gif = 'https://acegif.com/wp-content/gifs/rainbow-115.gif'
    print(session.text)
    bot.send_document(session.chat.id, gif)

#Função que envia um 'Olá Mundo!' para qualquer caractere inserido
@bot.message_handler(func=lambda a: True)
def olaMundo(session):
    #Printa no console o nome do seu bot e o texto enviado pelo usuário
    print('Mochileiro_bot:', session.text)
    bot.reply_to(session, 'Olá Mundo!')

bot.polling()