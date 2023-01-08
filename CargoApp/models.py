from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone

# Create your models here.
class Cargotb(models.Model):
	
	Contact_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$',message="ContactNumber must be entered in the format:'+999999999'. up to 15 digits allowed")
	Firstname=models.CharField(max_length=100,default='')
	Lastname=models.CharField(max_length=100,default='')
	DateOfBirth=models.CharField(max_length=30,default='')
	# Tracking=models.CharField(max_length=30,default='')
	Gender=models.CharField(max_length=100,default='')
	Age=models.IntegerField(null=True)
	ContactNumber=models.CharField(validators=[Contact_regex],max_length=17,blank=True)
	Country=models.CharField(max_length=30,default='')
	State=models.CharField(max_length=30,default='') 
	District=models.CharField(max_length=100,default='')
	Address=models.CharField(max_length=100,default='')
	Email=models.EmailField()
	Photo=models.ImageField(upload_to="media/",default='')
	Username=models.CharField(max_length=100,default='')
	Password=models.CharField(max_length=8,default='')
	ConfirmPassword=models.CharField(max_length=8,default='')

def __str__(self):
	return self.Firstname

class BookingTB(models.Model):
	Contact_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$',message="ContactNumber must be entered in the format:'+999999999'. up to 15 digits allowed")
	Cargotb=models.ForeignKey(Cargotb,on_delete=models.CASCADE,null=True)
	# Tracking=models.CharField(max_length=100,default='')
	Origin=models.CharField(max_length=100,default='')
	Shippername=models.CharField(max_length=100,default='')
	OrderDate= models.DateTimeField(blank=True,auto_now_add=True,null=True)
	Email=models.EmailField()
	ContactNumber=models.CharField(validators=[Contact_regex],max_length=17,blank=True,default='')
	Destination=models.CharField(max_length=100,default='')
	DeliveryDate=models.CharField(max_length=100,default='')
	ShipperAddress=models.CharField(max_length=100,default='')
	Recivername=models.CharField(max_length=100,default='')
	ReciverEmail=models.EmailField()
	ReciverContact=models.CharField(max_length=100,default=True)
	ReciverAddresss=models.CharField(max_length=100,default=True)
	ReciverPin=models.IntegerField()
	ReciverDistrict=models.CharField(max_length=100,default=True)
	ReciverState=models.CharField(max_length=100,default=True)
	ReciverCountry=models.CharField(max_length=100,default=True)
	CargoWeigth=models.CharField(max_length=100,default=True)
	CargoQuantity=models.CharField(max_length=100,default=True)
	ShipmentType=models.CharField(max_length=100,default=True)
	NetRate=models.CharField(max_length=100,default=True)
	Type=models.CharField(max_length=100,default=True)
	Status=models.CharField(max_length=100,default=True)
def __str__(self):
	return self.Shippername



class PaymentTB(models.Model):
	Cargotb=models.ForeignKey(Cargotb,on_delete=models.CASCADE,null=True)
	CardholdersName=models.CharField(max_length=100,default=True)
	CardNumber=models.CharField(max_length=100,default=True)
	ExpiryMonth=models.CharField(max_length=100,default=True)
	ExpiryYear=models.CharField(max_length=100,default=True)
	CVV=models.CharField(max_length=100,default=True)
	Amount=models.CharField(max_length=100,default=True)


class FeedbackTb(models.Model):
	Shippername=models.CharField(max_length=100,default='')
	Cargotb=models.ForeignKey(Cargotb,on_delete=models.CASCADE,null=True)
	Booking=models.ForeignKey(BookingTB,on_delete=models.CASCADE,null=True)
	Comments=models.CharField(max_length=100,default='')
	Date=models.DateTimeField(blank=True,auto_now_add=True,null=True)


class OrderTb(models.Model):
	Shippername=models.CharField(max_length=100,default=True)
	Origin=models.CharField(max_length=100,default=True)
	Destination=models.CharField(max_length=100,default=True)
	Type=models.CharField(max_length=100,default=True)
	DeliveryCharge=models.CharField(max_length=100,default=True)
	ReciverAddresss=models.CharField(max_length=100,default=True)
	CargoWeigth=models.CharField(max_length=100,default=True)
	PaymentType=models.CharField(max_length=100,default=True)
	TotalPayment=models.CharField(max_length=100,default=True)

