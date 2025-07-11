python -m venv env  --  Создайте виртуальное окружение
source env/bin/activate  --  Linux/Mac
env\Scripts\activate  --   Windows

pip install django djangorestframework  --  Установите Django и Django REST Framework

django-admin startproject barter_platform  --  Создайте проект и приложение
cd barter_platform
python manage.py startapp ads

python manage.py makemigrations   --   Исполните миграции
python manage.py migrate  

python manage.py createsuperuser -- создаём суперпользователя
