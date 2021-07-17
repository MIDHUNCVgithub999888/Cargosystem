from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from.models import EmployeeRegisterTB,AdminBranchesTB,NotificationsTB
from CargoApp.models import BookingTB,PaymentTB,Cargotb,FeedbackTb
from .forms import BranchForm,NotificationsForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from AdminApp.forms import CustomUserCreationForm

# Create your views here.

def AdminIndex(request):
	return render(request,'AdminApp/base.html')


def AdminRegister(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/AdminRegister')
    else:
        f = CustomUserCreationForm()
    return render(request, 'AdminApp/Register.html', {'form':f})

def Home(request,id):
	if request.session.has_key:
		uid=request.session["id"]
		user=auth_user.objects.get(id=id)
		return render(request,'AdminApp/index.html',{'user':user})

def AddEmployee(request):
    saved=False
    if request.method=='POST':
        EmployeeRegister=EmployeeForm(request.POST,request.FILES)
        if EmployeeRegister.is_valid():
            Emptb=EmployeeRegisterTB()
            Emptb.Name=EmployeeRegister.cleaned_data["Name"]
            Emptb.Dateofjoin=EmployeeRegister.cleaned_data["Dateofjoin"]
            Emptb.Age=EmployeeRegister.cleaned_data["Age"]
            Emptb.Gender=EmployeeRegister.cleaned_data["Gender"]
            Emptb.Address=EmployeeRegister.cleaned_data["Address"]
            Emptb.City=EmployeeRegister.cleaned_data["City"]
            Emptb.State=EmployeeRegister.cleaned_data["State"]
            Emptb.Country=EmployeeRegister.cleaned_data["Country"]
            Emptb.Photo=EmployeeRegister.cleaned_data["Photo"]
            Emptb.EmailID=EmployeeRegister.cleaned_data["EmailID"]
            Emptb.Phonenumber=EmployeeRegister.cleaned_data["Phonenumber"]
            Emptb.Loginname=EmployeeRegister.cleaned_data["Loginname"]
            Emptb.Password=EmployeeRegister.cleaned_data["Password"]
            Emptb.ConfirmPassword=EmployeeRegister.cleaned_data["ConfirmPassword"]
            Emptb.Status=EmployeeRegister.cleaned_data["Status"]
            Emptb.save()
            return HttpResponse('success')
        else:
            
            print(EmployeeRegister.errors)
            return render(request,'AdminApp/EmployeeRegister.html',{'data':EmployeeRegister})
    else:
        EmployeeRegister=EmployeeForm()
        return render(request,'AdminApp/EmployeeRegister.html',{'data':EmployeeRegister})


def ViewEmployee(request):
    user=EmployeeRegisterTB.objects.all()
    return render(request,'AdminApp/ViewEmployee.html',{'user':user})

def OrderDetails(request):
    user=BookingTB.objects.all()
    return render(request,'AdminApp/OrderDetails.html',{'user':user})

def PaymentDetails(request):
 user=PaymentTB.objects.all()
 return render(request,'AdminApp/Payment.html',{'user':user})


# @login_required
def AdminProfile(request):
    if request.user.is_authenticated:
        return render(request,'AdminApp/Profile.html',{'name':request.user})
    else:
        return redirect('/AdminProfile/')



def AdminBranches(request):
    saved=False
    if request.method=='POST':
        Branches=BranchForm(request.POST,request.FILES)
        if Branches.is_valid():
            Btb=AdminBranchesTB()
            Btb.BranchName=Branches.cleaned_data['BranchName']
            Btb.BranchContactnumber=Branches.cleaned_data['BranchContactnumber']
            Btb.BranchEmail=Branches.cleaned_data['BranchEmail']
            Btb.BranchAddress=Branches.cleaned_data['BranchAddress']
            Btb.BranchCity=Branches.cleaned_data['BranchCity']
            Btb.BranchState=Branches.cleaned_data['BranchState']
            Btb.BranchCountry=Branches.cleaned_data['BranchCountry']
            Btb.BranchPincode=Branches.cleaned_data['BranchPincode']
            Btb.save()
            messages.info(request,'Saved successfully...')
            return redirect('/AdminBranches')
        else:
            print(Branches.errors)
            return render(request,'AdminApp/Branches.html',{'data':Branches})
    else:
        Branches=BranchForm()
        return render(request,'AdminApp/Branches.html',{'data':Branches})

def user_change_pass(request):
    if request.method =="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'ChangePassword Succesfully...')
            return redirect('/user_change_pass')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'Registration/Password.html',{'form':fm})

def ManageBranch(request):
    if request.session.has_key:
        user=AdminBranchesTB.objects.all()
        return render(request,'AdminApp/BranchList.html',{'user':user})

def AdminDelete(request,id):
    user=AdminBranchesTB.objects.filter(id=id)
    user.delete()
    return redirect('/ManageBranch')

def Notifications(request,id):
    if request.method == 'POST':
        form=NotificationsForm(request.POST,request.FILES)
        if form.is_valid():
            ntb=NotificationsTB()
            ntb.Cargotb_id=request.session['id']
            ntb.Shippername=form.cleaned_data['Shippername']
            ntb.Description=form.cleaned_data['Description']
            ntb.Status=form.cleaned_data['Status']
            ntb.DeliveryDate=form.cleaned_data['DeliveryDate']
            ntb.save()
            messages.success(request,'Notifications send successfully...')
            return redirect('/AdminIndex')
        else:
            print(form.errors)
        return render(request,'AdminApp/Notifications.html',{'form':form})
    else:
        form=NotificationsForm()
        return render(request,'AdminApp/Notifications.html',{'form':form})

# def NotificationsSend(request,id):
#     user=OrderTB.objects.get(id=id)
#     return render(request,'AdminApp/Notifications.html',{'user':user})

            
def OrderDelete(request,id):
    user=BookingTB.objects.filter(id=id)
    user.delete()
    return render(request,'AdminApp/OrderDetails.html',{'user':user})

def ViewCustomers(request):
    user=Cargotb.objects.all()
    return render(request,'AdminApp/customer.html',{'user':user})

def Feedback(request):
    user=FeedbackTb.objects.all()
    return render(request,'AdminApp/feedback.html',{'user':user})

    

    








