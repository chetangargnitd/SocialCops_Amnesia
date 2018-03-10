# user - chetan
# pwd - chetan1234
from django.contrib import admin
from reminder.models import Receiver

class ReceiverAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'created_date')

admin.site.register(Receiver,ReceiverAdmin)
