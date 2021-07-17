from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from.models import Cargotb,BookingTB,FeedbackTb,PaymentTB,OrderTb
from AdminApp.models import AdminBranchesTB
from django.contrib import messages
from .forms import RegisterForm,LoginForm,BookingForm,ProfileForm,ChangePasswordForm,PaymentForm,FeedbackForm,OrderForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from AdminApp.models import NotificationsTB
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def index(request):
	return render(request,'CargoApp/index.html')

def login(request):
	return render(request,'Registration/login.html')
	

def Register(request):
 	saved=False
 	if request.method=='POST':
 		CustomerRegister=RegisterForm(request.POST,request.FILES)
 		if CustomerRegister.is_valid():
 			Ctb=Cargotb()
 			Ctb.Firstname=CustomerRegister.cleaned_data['Firstname']
 			Ctb.Lastname=CustomerRegister.cleaned_data['Lastname']
 			Ctb.DateOfBirth=CustomerRegister.cleaned_data['DateOfBirth']
 			Ctb.Gender=CustomerRegister.cleaned_data['Gender']
 			Ctb.Age=CustomerRegister.cleaned_data['Age']
 			Ctb.ContactNumber=CustomerRegister.cleaned_data['ContactNumber']
 			Ctb.Country=CustomerRegister.cleaned_data['Country']
 			Ctb.State=CustomerRegister.cleaned_data['State']
 			Ctb.District=CustomerRegister.cleaned_data['District']
 			Ctb.Address=CustomerRegister.cleaned_data['Address']
 			Ctb.Email=CustomerRegister.cleaned_data['Email']
 			Ctb.Photo=CustomerRegister.cleaned_data['Photo']
 			Ctb.Username=CustomerRegister.cleaned_data['Username']
 			Ctb.Password=CustomerRegister.cleaned_data['Password']
 			Ctb.ConfirmPassword=CustomerRegister.cleaned_data['ConfirmPassword']
 			Ctb.save()

 			messages.success(request,"Your Registration is Succesfull")
 			return redirect('/')
 		else:
 			print(CustomerRegister.errors)
 			return render(request,'CargoApp/Registration.html',{'data':CustomerRegister})
 	else:
 		CustomerRegister=RegisterForm()
 		return render(request,'CargoApp/Registration.html',{'data':CustomerRegister})
def Login(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			Username=form.cleaned_data["Username"]
			Password=form.cleaned_data["Password"]
			a=Cargotb.objects.all().filter(Username=Username,Password=Password)
			for x in a:
				request.session['id']=x.id
				return redirect('/Home/%s' % x.id,{'a':x.Firstname})
			else:

				msg=messages.info(request,'Invalid Credential')
				return redirect('/Login',{'msg':messages})
				
				
		else:
			print(form.errors)
			return render(request,'CargoApp/Login.html',{'data':form})
	else:
		form=LoginForm()
		return render(request,'CargoApp/Login.html',{'data':form})

def Booking(request,id):
	saved=False
	# fid=request.session['id']
	if request.session.has_key:
		user=Cargotb.objects.get(id=id)
	if request.method=='POST':
		UserBooking=BookingForm(request.POST,request.FILES)
		if UserBooking.is_valid():
			Btb=BookingTB()
			Btb.Cargotb_id=request.session['id']
			Btb.Status='Booked'
			Btb.Origin=UserBooking.cleaned_data['Origin']
			# Btb.OrderDate=UserBooking.cleaned_data['OrderDate']
			Btb.Shippername=UserBooking.cleaned_data['Shippername']
			Btb.Email=UserBooking.cleaned_data['Email']
			Btb.ContactNumber=UserBooking.cleaned_data['ContactNumber']
			Btb.ShipperAddress=UserBooking.cleaned_data['ShipperAddress']
			Btb.Destination=UserBooking.cleaned_data['Destination']
			Btb.DeliveryDate=UserBooking.cleaned_data['DeliveryDate']
			Btb.Recivername=UserBooking.cleaned_data['Recivername']
			Btb.ReciverEmail=UserBooking.cleaned_data['ReciverEmail']
			Btb.ReciverContact=UserBooking.cleaned_data['ReciverContact']
			Btb.ReciverAddresss=UserBooking.cleaned_data['ReciverAddresss']
			Btb.ReciverPin=UserBooking.cleaned_data['ReciverPin']
			Btb.ReciverDistrict=UserBooking.cleaned_data['ReciverDistrict']
			Btb.ReciverState=UserBooking.cleaned_data['ReciverState']
			Btb.ReciverCountry=UserBooking.cleaned_data['ReciverCountry']
			Btb.CargoWeigth=UserBooking.cleaned_data['CargoWeigth']
			Btb.CargoQuantity=UserBooking.cleaned_data['CargoQuantity']
			Btb.ShipmentType=UserBooking.cleaned_data['ShipmentType']
			Btb.NetRate=UserBooking.cleaned_data['NetRate']
			Btb.Type=UserBooking.cleaned_data['Type']
			Btb.save()
			messages.success(request,'Succesfully Booked....')
			return redirect('/OnlinePayment/%s' % user.id)
		else:
			print(UserBooking.errors)
			return render(request,'CargoApp/Booking.html',{'data':UserBooking})
	else:
		UserBooking=BookingForm()
		return render(request,'CargoApp/Booking.html',{'data':UserBooking,'user':user})
		

def Home(request,id):
	if request.session.has_key:
		user=Cargotb.objects.get(id=id)
	return render(request,'CargoApp/Home.html',{'user':user})



def OnlinePayment(request,id):
	uid=request.session['id']
	if request.session.has_key:
		user=BookingTB.objects.latest('id')
		# return redirect('/FinalPayment/%s'  % user.id)
	return render(request,'CargoApp/OnlinePayment.html',{'user':user,'uid':uid})
		
  

def FinalPayment(request,id):
	uid=request.session['id']
	if request.session.has_key:
		user=BookingTB.objects.get(id=id)
		if request.method=='POST':
			payment=PaymentForm(request.POST,request.FILES)
			if payment.is_valid():
				ptb=PaymentTB()
				ptb.Cargotb_id=request.session['id']
				ptb.CardholdersName=payment.cleaned_data['CardholdersName']
				ptb.CardNumber=payment.cleaned_data['CardNumber']
				ptb.ExpiryMonth=payment.cleaned_data['ExpiryMonth']
				ptb.ExpiryYear=payment.cleaned_data['ExpiryYear']
				ptb.CVV=payment.cleaned_data['CVV']
				ptb.Amount=payment.cleaned_data['Amount']
				ptb.save()
				messages.success(request,'Your payment is Succesfull...')
				return redirect('/Home/%s' % uid)
			else:
				print(payment.errors)
				return render(request,'CargoApp/FinalPayment.html',{'data':payment})
		else:
			payment=PaymentForm()
	return render(request,'CargoApp/FinalPayment.html',{'data':payment,'user':user,'uid':uid})
	

def UserProfile(request,id):
	uid=request.session['id']
	user=Cargotb.objects.get(id=id)
	form=ProfileForm(request.POST or None ,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		messages.success(request,'Updated Succesfully....')
		return redirect('/Edit/%s' % user.id)
	return render(request,'CargoApp/Profile.html',{'form':form,'user':user,'uid':uid})



def Edit(request,id):
	user=Cargotb.objects.get(id=id)
	form=ProfileForm(request.POST or None ,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		messages.success(request,'Updated Succesfully....')
		return redirect('/UserProfile/%s' % user.id)
	return render(request,'CargoApp/Edit.html',{'form':form,'user':user})


def UserDelete(request,id):
	user=Cargotb.objects.get(id=id)
	user.delete()
	return redirect('/')


def UserLogout(request,id):
	messages.info(request,'loggedOut Succesfully......')
	return redirect('/')

def ChangePassword(request,id):
	uid=request.session['id']
	user=Cargotb.objects.get(id=id)
	if request.method=='POST':
		form= ChangePasswordForm(request.POST)
		if form.is_valid():
			oldpassword=form.cleaned_data['OldPassword']
			newpassword=form.cleaned_data['NewPassword']
			confirmpassword=form.cleaned_data['ConfirmPassword']
			if oldpassword!=user.Password:
				msg="enter the correct Password"
				return render(request,'CargoApp/CustomerChangePassword.html',{'form':form,'error':msg,'user':user})
			elif newpassword!=confirmpassword:
				msg="Password does not match"
				return render(request,'ChangePassword.html',{'form':form,'error':msg,'user':user})
			else:
				user.Password=newpassword
				user.ConfirmPassword=confirmPassword
				user.save()
				msg="ChangePassword Succesfully..."
				return redirect("Home/%s" %id)
				return render(request,'CargoApp/CustomerChangePassword.html',{'form':form,'error':msg,'user':user})
	else:
		form=ChangePasswordForm()
	return render(request,'CargoApp/CustomerChangePassword.html',{'form':form,'user':user})

def UserFeedback(request,id):
	if request.session.has_key:
		user=Cargotb.objects.get(id=id)
	if request.method == 'POST':
		form=FeedbackForm(request.POST,request.FILES)
		if form.is_valid():
			ftb=FeedbackTb()
			ftb.Shippername=BookingTB.Shippername
			ftb.Cargotb_id=request.session['id']
			ftb.Comments=form.cleaned_data["Comments"]
			ftb.save()
			messages.success(request,'Feedback send successfully....')

		else:
			print(form.errors)
			return render(request,'CargoApp/Feedback.html',{'form':form,'user':user})
	else:
		form=FeedbackForm()
	return render(request,'CargoApp/Feedback.html',{'form':form,'user':user})


def UserOrder(request,Cargotb_id):
	uid=request.session['id']
	print('uid',uid)
	user=BookingTB.objects.filter(Cargotb_id=uid)
	print('user',user)
	return render(request,'CargoApp/Orders.html',{'user':user,'uid':uid})

def AdminDelete(request,id):
    user=BookingTB.objects.filter(id=id)
    user.delete()
    return redirect('/Orders')

def UserNotifications(request,Cargotb_id):
	uid=request.session['id']
	user=NotificationsTB.objects.filter(Cargotb_id=uid)
	return render(request,'CargoApp/UserNotifications.html',{'user':user,'uid':uid})
	
	
	
		
def service(request):
	return render(request,'CargoApp/service.html')


def Pricing(request):
	return render(request,'CargoApp/Pricing.html')

def contact(request):
	return render(request,'CargoApp/contact.html')

def About(request):
	return render(request,'CargoApp/about.html')

def Branches(request):
	user=AdminBranchesTB.objects.all()
	return render(request,'CargoApp/Branches.html',{'user':user})

def NotificationsDelete(request,Cargotb_id):
	uid=request.session['id']
	user=NotificationsTB.objects.filter(Cargotb_id=uid)
	user.delete()
	return render(request,'CargoApp/UserNotifications.html',{'user':user,'uid':uid})

def OrderDelete(request,Cargotb_id):
    uid=request.session['id']
    user=BookingTB.objects.filter(Cargotb_id=uid)
    user.delete()
    return render(request,'CargoApp/Orders.html',{'user':user})