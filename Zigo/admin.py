from django.contrib import admin
from .models import ParcelDetails, ReceiverDetails, SenderDetails

# Register your models here.
admin.site.register(ParcelDetails)
admin.site.register(ReceiverDetails)
admin.site.register(SenderDetails)
