def send_sms(): 
    f = open('log.txt' , 'a')   
    try:
        receiver = Receiver.objects.all()
    except Receiver.DoesNotExist:
        return
    for receivers in receiver:
        now = datetime.now()
        diff_time = now - receiver.created_date
        try:
            print('%s %s' %(receivers.phone, receivers.name))
            client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
            response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())            
            f.write("%s Message successfully sent to %s. Application is running for %s \n" % (now, receivers.phone, diff_time ))
        except:
            for i in range(0,5):
                client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
                response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())
                f.write("%s Message couldn't be sent to %s. Application is running for %s \n" % (now, receivers.phone, diff_time ))

        now = datetime.now()
        diff_time = now - receiver.created_date                


from .models import Receiver
from twilio.rest import Client
from datetime import datetime

def send_sms():
    f = open('log.txt' , 'a')
    now = datetime.now()    
    try:
        receiver = Receiver.objects.all()
    except Receiver.DoesNotExist:
        return
    for receivers in receiver:
        print('1')      
        print('%s %s' %(receivers.phone, receivers.name))
        client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
        response = client.messages.create(to="%s" %receivers.phone , from_="+18564215845 ", body="Hello, your name is %s !" %receivers.name.title())
        f.write("%s Message successfully sent to %s. Application is running for\n" % (now, receivers.phone ))
        print (str(response))
        for message in client.messages.list():
            print(message.status, message.date_sent)
        