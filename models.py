from django.db import models
from django.forms import ModelForm


class RegInfo(models.Model):
    sponsor_name = models.CharField(max_length=200)
    sponsor_address = models.CharField(max_length=500)
    sponsor_phone = models.IntegerField()
    sponsor_email = models.EmailField()
    next_of_kin = models.CharField(max_length=50)
    next_of_kin_phone = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=11)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    lga = models.CharField(max_length=30)
    id_number = models.CharField(max_length=11)
    date_of_birth = models.DateTimeField()
    biography = models.CharField(max_length=500)
    date_of_registration = models.DateTimeField()


class Myform(ModelForm):
    class Meta:
        model = RegInfo
        exclude = ('id_number', 'date_of_registration')
