# SocialCops_Amnesia

It is a Django based web application where one can set his/her number and the app will Send an SMS every one hour except at night.

To run this :
1. Clone this repository.
2. Run the command pip install -r requirements.txt to install all dependencies
3. Set up Account_SID and auth_token from Twilio.
4. To run the local server python manage.py runserver
5. Add django crontab : python manage.py crontab add
6. Run django crontab : python manage.py crontab run <enter hash value>
