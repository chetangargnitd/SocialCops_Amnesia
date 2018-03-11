from .models import Receiver
from twilio.rest import Client
from datetime import datetime
import time
import pytz

def send_sms(): 
	f = open('log.txt' , 'a')   
	try:
	    receiver = Receiver.objects.all()
	except Receiver.DoesNotExist:
	    return
	for receivers in receiver:
		now = datetime.now().replace(tzinfo=None)
		try:
			time = receivers.created_date.replace(tzinfo=None)
			run_time = now - time
			run_hours = run_time.total_seconds()/3600
			client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
			response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())            
			f.write("%s Message successfully sent to %s. Application is running for %s or %s hours.\n" % (now, receivers.phone, str(run_time), str(round(run_hours, 2)) ))
		except:
			for i in range(0,5):
				client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
				response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())
				f.write("%s Message couldn't be sent to %s. Application is running for %s or %s hours.\n" % (now, receivers.phone, str(run_time), str(round(run_hours, 2)) ))

