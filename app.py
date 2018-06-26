from flask import Flask


app = Flask(__name__)  # Исходя из этого имени Flask будет выстраивать все свои зависимости к шаблонам, файлам и т.д.



if __name__ == "__main__":
    app.run()  # Запустили сервер.
