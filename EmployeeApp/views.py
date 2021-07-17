from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import EmployeeRegisterTB
from EmployeeApp.models import CustomerDetailsTB
from django.contrib import messages
from.forms import LoginForm,RegisterForm
from AdminApp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def EmployeeIndex(request,id):
	if request.session.has_key:
		uid=request.session["id"]
		user=EmployeeRegisterTB.objects.get(id=id)	
	return render(request,'EmployeeApp/index.html',{'user':user})

def EmployeeLogin(request):
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			Loginname=form.cleaned_data['Loginname']
			Password=form.cleaned_data['Password']
			a=EmployeeRegisterTB.objects.all().filter(Loginname=Loginname,Password=Password)
			for x in a:
				request.session["id"]=x.id
				return redirect('/EmployeeIndex/%s' % x.id,{'a':x.Name})
			else:
				return HttpResponse('Invalid Credentials')
		else:
			print(form.errors)
			return render(request,'EmployeeApp/Login.html',{'data':form})
	else:
		form=LoginForm()
		return render(request,'EmployeeApp/Login.html',{'data':form})

def EmployeeProfile(request,id):
	Eid=request.session['id']
	user=EmployeeRegisterTB.objects.get(id=Eid)
	form=EmployeeForm(request.POST or None,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		return redirect('/EmployeeProfile/%s' % user.id)
	return render(request,'EmployeeApp/Profile.html',{'form':form,'user':user})


def EmployeeLogOut(request,id):
	messages.info(request,'LogOut Successfully...')
	return redirect('/EmployeeLogin')

def EmployeeRegister(request,id):
	Eid=request.session['id']
	user=EmployeeRegisterTB.objects.get(id=Eid)

	if request.method=='POST':
		Register=RegisterForm(request.POST,request.FILES)
		if Register.is_valid():
			table=CustomerDetailsTB()
			table.BillNumber=Register.cleaned_data['BillNumber']
			table.CustomerName=Register.cleaned_data['CustomerName']
			table.MobileNumber=Register.cleaned_data['MobileNumber']
			table.EmailID=Register.cleaned_data['EmailID']
			table.Address=Register.cleaned_data['Address']
			table.District=Register.cleaned_data['District']
			table.Destination=Register.cleaned_data['Destination']
			table.DeliveryAcceptDate=Register.cleaned_data['DeliveryAcceptDate']
			table.Weight=Register.cleaned_data['Weight']
			table.PackageType=Register.cleaned_data['PackageType']
			table.Amount=Register.cleaned_data['Amount']
			table.Status=Register.cleaned_data['Status']
			table.save()
			messages.success(request,'success')
			return render(request,'EmployeeApp/EmployeeRegister.html',{'user':user})
		else:
			print(Register.errors)
			return render(request,'EmployeeApp/EmployeeRegister.html',{'data':Register,'user':user})
	else:
		Register=RegisterForm()
		return render(request,'EmployeeApp/EmployeeRegister.html',{'data':Register,'user':user})


def ViewTransaction(request,id):
	ui=request.session['id']
	user=CustomerDetailsTB.objects.get(id=ui)
	return render(request,'EmployeeApp/Transaction.html',{'user':user,'ui':ui})

	

