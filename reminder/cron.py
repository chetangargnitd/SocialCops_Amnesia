from .models import Receiver
from twilio.rest import Client
from datetime import datetime
import time

def send_sms(): 
	f = open('log.txt' , 'a')   
	try:
	    receiver = Receiver.objects.all()
	except Receiver.DoesNotExist:
	    return
	for receivers in receiver:
		now = datetime.now()
		try:			
			client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
			response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())            
			f.write("%s Message successfully sent to %s. Application is running since %s.\n" % (now, receivers.phone, receivers.created_date))
		except:
			for i in range(0,5):
				client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
				response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())
				f.write("%s Message couldn't be sent to %s. Application is running since %s.\n" % (now, receivers.phone, receivers.created_date ))

