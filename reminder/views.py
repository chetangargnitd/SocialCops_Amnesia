from django.shortcuts import render
from reminder.forms import RegisterForm
from datetime import datetime
from twilio.rest import Client

def index(request):
	form_class = RegisterForm
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			name = request.POST.get('name', '')          
			phone = request.POST.get('contact_no', '')				
			user.save()                        
			matter = {
				'message': 'You have been successfully subscribed !',
				'form': form_class
			}			

			return render(request, 'reminder/index.html', matter)      
	matter = {
		'message': 'Enter a Valid Number !',
		'form': form_class
	}
	return render(request, 'reminder/index.html', matter) 
	return render(request, 'reminder/index.html', {'form': form_class})

def logs(request):
	failed_msgs = []
	client = Client("AC75ae5236e00d65f7b83b89e7b398c02f", "fa76bf71b4b78b138e269cb71110c662")
	for message in client.messages.list():
		if str(message.status)=='failed' or str(message.status)=='undelivered':
			failed_msgs.append({'status' : message.status, 'to' :message.to, 'date' : message.date_sent.date(), 'time' : message.date_sent.time()}) 
	return render(request, 'reminder/logs.html', {'failed_msgs' :failed_msgs})