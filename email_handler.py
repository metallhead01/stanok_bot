import imaplib
import email
import smtplib


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

# Just enable 2-step verification on your account.
# Then generate one App-Specific-Password and use that to connect instead of your original password.

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "jamies.italian.it" + ORG_EMAIL
FROM_PWD    = "zpjfzquiexnbnzau"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def get_first_text_block(email_message_instance):  # http://python-3.ru/page/imap-email-python
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload().split(', ')
    elif maintype == 'text':
        return email_message_instance.get_payload().split(', ')


def read_email_from_gmail():
    emails_list = []
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')   # Подключаемся к папке "Входящие"
        # Начнем с поиска входящих среди всех писем при помощи функции поиска
        result, data = mail.uid('search', None, "ALL")  # Выполняет поиск и возвращает UID писем.
        uid_list = data[0].split()  # видим список с одним элементом, но множеством значений в нем в одну строку.
                                    # разрежем первый элемент этого списка.

        for i in reversed(uid_list):  # обращаем список и начинаем идти с конца
            result, data = mail.uid('fetch', i,
                                    '(RFC822)')  # Получаем тело письма (RFC822) для данного ID, result возврящает OK
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email.decode('utf-8'))  # декодируем байты в строки
            get_first_text_block(email_message)  # вызываем функцию get_first_text_block()
            emails_list.append(get_first_text_block(email_message))

        return emails_list

    except Exception as e:
        print(str(e))

