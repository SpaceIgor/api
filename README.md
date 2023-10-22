1.Pull my project in your local pc

2.Create and activate your virtual env(for Macos):
- python(python3) -m venv <name_your_virtualenv>
- source <name_your_virtualenv>/bin/activate

3.Install file requirements.txt:
- pip install requirements.txt

4.Run migrations for db(need run in dir with file manage.py) and run project:
- python or python3 manage.py makemigrations
- python or python3 manage.py migrate
- python or python3 manage.py runserver

5.Endpoint (http://127.0.0.1:8000/api/):
 - person
 - person/<int:pk>/
 - team
 - team/<int:pk>/
