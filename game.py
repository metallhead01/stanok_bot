#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a simple echo bot using decorators and webhook with BaseHTTPServer
# It echoes any incoming text messages and does not use the polling method.

import http.server
import ssl
import telebot
import logging


with open('telegram.token', 'r') as f:
    token = f.read()
API_TOKEN = token

WEBHOOK_HOST = 'www.alextelebot.tk'
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '80.240.30.130'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = 'cert1.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = 'privkey1.pem'  # Path to the ssl private key


WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)


# WebhookHandler, process webhook calls
class WebhookHandler(http.server.BaseHTTPRequestHandler):
    server_version = "WebhookHandler/1.0"

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == WEBHOOK_URL_PATH and \
           'content-type' in self.headers and \
           'content-length' in self.headers and \
           self.headers['content-type'] == 'application/json':
            json_string = self.rfile.read(int(self.headers['content-length']))

            self.send_response(200)
            self.end_headers()

            update = telebot.types.Update.de_json(json_string)
            bot.process_new_messages([update.message])
        else:
            self.send_error(403)
            self.end_headers()


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))


# Handle all other messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Start server
httpd = http.server.HTTPServer((WEBHOOK_LISTEN, WEBHOOK_PORT),
                                  WebhookHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile=WEBHOOK_SSL_CERT,
                               keyfile=WEBHOOK_SSL_PRIV,
                               server_side=True)

httpd.serve_forever()
