from django.contrib import admin
from .models import ParcelDetail, ReceiverDetail, SenderDetail

# Register your models here.
admin.site.register(ParcelDetail)
admin.site.register(ReceiverDetail)
admin.site.register(SenderDetail)
