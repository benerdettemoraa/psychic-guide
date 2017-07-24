from django.db import models


# Create your models here.
class ParcelDetail(models.Model):
    parcel_id = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    destination = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    parcel_arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)


class ReceiverDetail(models.Model):
    parcel_id = models.ForeignKey(ParcelDetail, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)  # town being sent to
    national_id_number = models.CharField(max_length=200)


class SenderDetail(models.Model):
    parcel_id = models.ForeignKey(ParcelDetail, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)  # town being sent from
    national_id_number = models.CharField(max_length=200)
