# SocialCops_Amnesia

It is a Django based web application where one can set his/her number and the app will Send an SMS every one hour except at night.

To run this project:
1. Clone this repository.
2. To create virtual environment write in terminal - <code>virtualenv venv</code>
3. To run virtual environment enter in terminal - <code>source venv/bin/activate</code>
4. Run the command <code>pip install -r requirements.txt</code> to install all dependencies
5. Set up Account_SID and auth_token from Twilio.
6. To run the local server <code>python manage.py runserver</code>
7. Add django crontab : <code>python manage.py crontab add</code>
8. Run django crontab : <code>python manage.py crontab run <enter hash value></code>
