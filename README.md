# Announcement Channel API

**Студент:** Кухта Данило Ігорович  
**Група:** КВ-51мп  
**Лабораторна робота:** №1 - Розробка серверної частини Web-додатка  

## Опис завдання
Розробити серверну частину Web-додатку для системи коментарів з використанням Django та Django REST Framework.

## Посилання на звіт
[Звіт на Google Drive](https://docs.google.com/document/d/142VclMyO0cFKi8ZL7n6l71CryjKLeWyfit9AUIe8Mbg/edit?usp=sharing)

## Встановлення та запуск

1. Клонування репозиторію:
``` bash
git clone https://github.com/joe1i/WEBTECH-lab-1.git
cd WEBTECH-lab-1
``` 
2. Створення віртуального середовища:
``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
``` 
3. Встановлення залежностей:
``` bash
pip install -r requirements.txt
``` 
4. Міграції бази даних:
``` bash
python manage.py makemigrations users announcements reactions
python manage.py migrate
python manage.py createsuperuser
```
5. Запуск сервера:
``` bash
python manage.py runserver
```

6. (Опціонально) Наповнити базу тестовими даними:
``` bash
python manage.py populate_db
```
Дані тестового адміна для входу:
``` bash
email: admin@example.com
password: adminpass123
```