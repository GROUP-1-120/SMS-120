Project Title:Send SMS Application


Description: Application created main features is to send a message in the phone using sms

Setup Instructions: Provide clear steps to run the application (e.g., requirements, commands to install dependencies, etc.).

First: create a virtualenv file
command: virtualenv <'name of the file'>

Second: activate the scripts to your virtual file
command: scripts\activate

Third: Install Django
command: python -m pip install Django (m = for module)

fourth: create a app name SMS it depends on you
command: django-admin startapp SMS

Intructions
1.add your SMS to settings.py 'sms' and put the key and secret key 
2.create utils.py inside in the sms created then put your code
In me I created two for sending sms and validation if the phone inputted is not in the format
3 in views.py import the class name sending sms and validation 
4 create a class name sending_sms_view put the sending_sms and validation inside 
5 Go to your urls.py import sending_sms_view then provide a path like /send/
6 create a folder named templates then add go to your settings.py put it in templates section
you can see DIRS then insert this 'DIRS': [BASE_DIR / "templates"],
7 last go to command prompt then make a command 
python manage.py runserver
8 go to your google then see it from this 127.0.0.1/8000/send/
9 then finish you can able to message

Usage Instructions: Explain how to use the app (e.g., steps to send an SMS).
first step: provide a destination or a receiver number like +639676595166
second step: write a message 
third step: click the button to send then wait until it provide a message that this message is successfully send

Author(s): Group 1.
Leader: Bernie Cherry Rante
Members:
    Niko Polistico
    Mark Ahron Taglucop
    Laurence Jay Perez
    Dave Jason Salte

GitHub Repository Link: (https://github.com/nikopolistico/Group1-SMS-.git)