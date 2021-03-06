from django.conf import settings
from django.contrib.auth import get_user_model
import datetime
from django.db import models
from django.urls import reverse


class Client(models.Model):

    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    address = models.CharField(max_length=50, blank=True, null=True,default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    email = models.EmailField(max_length=100, default=' ')
    cell_phone = models.CharField(max_length=50,default='(402)000-0000')
    acct_number = models.CharField(max_length=50,blank=True, null=True, default='00000')
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])

class Comment(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('Client_list')

class vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicle',)
    vehicle_model = models.CharField(max_length=100)
    VIN = models.IntegerField()
    vehicle = models.CharField(max_length=140,null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,default="", editable=False,null=True)

    def get_absolute_url(self):
        return reverse('Client_list')

    def __str__(self):
        return self.vehicle_model