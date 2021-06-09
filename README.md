## Favourite Books
Django demo application as part of  "Intro to Progamming" course at AAB College (Pristina, Kosovo).

Aplikacioni Favourite Books eshte krijuar si pjese e lendes "Bazat e Programimit 2" ne Kolgjin AAB, Kosove. 
Ky app pershfine:
    - Authentication (login/register) & authorization
    - Registrimin e te dhenave per Books
    - Te dhenat per Books ne nje faqe te vetme 
    - Logout

Wireframe dhe ERD e projektit:
[Project wireframe](https://github.com/tringakrasniqi/favourite-books-aab/blob/main/Projec.PNG)

Per egzekutimin e applikacionit:
 - Clone projektin ne lokalisht
 - file: requirements.txt permban te gjitha librarite qe i perdore
    - (cmd command) `pip install` per instalimin e tyre
 - Ne root te projektit (folderi main):
    (cmd commands):
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
