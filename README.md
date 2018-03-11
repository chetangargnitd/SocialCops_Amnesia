# SocialCops_Amnesia

It is a Django based web application where one can set his/her number and the app will Send an SMS every one hour except at night.

To run this :
1. Clone this repository.
2. To run virtual environment enter in terminal - source venv/bin/activate
3. Run the command pip install -r requirements.txt to install all dependencies
4. Set up Account_SID and auth_token from Twilio.
5. To run the local server python manage.py runserver
6. Add django crontab : python manage.py crontab add
7. Run django crontab : python manage.py crontab run <enter hash value>
