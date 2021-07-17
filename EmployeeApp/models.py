from django.db import models

# Create your models here.

class CustomerDetailsTB(models.Model):
	BillNumber=models.CharField(max_length=100,default='')
	CustomerName=models.CharField(max_length=100,default='')
	MobileNumber=models.CharField(max_length=100,default='')
	EmailID=models.CharField(max_length=100,default='')
	Address=models.CharField(max_length=100,default='')
	District=models.CharField(max_length=100,default='')
	Destination=models.CharField(max_length=100,default='')
	DeliveryAcceptDate=models.CharField(max_length=100,default='')
	Weight=models.CharField(max_length=100,default='')
	PackageType=models.CharField(max_length=100,default='')
	Amount=models.CharField(max_length=100,default='')
	Status=models.CharField(max_length=100,default='')

