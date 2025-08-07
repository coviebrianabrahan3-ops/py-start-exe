import os
import webbrowser
import time

os.system("python manage.py runserver --noreload 127.0.0.1:8000")

time.sleep(2)
webbrowser.open("http://127.0.0.1:8000")
