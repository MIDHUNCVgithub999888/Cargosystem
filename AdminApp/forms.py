from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import EmployeeRegisterTB,AdminBranchesTB,NotificationsTB
from  datetime import datetime,date 
from django.utils.timezone import utc
from django.forms.widgets import NumberInput



notf=(

       ("select your Status","Select your Status"),
       ("appoved","Approved"),
       ("cancelled",'cancelled'),
       ("on the way",'on the way'),
       ('packing','packing'),
       ('delivered','delivered'),
        )



cntry=(
  ("select a Country","Select a Country"),
  ("afghanistan","Afghanistan"),
  ("albania","Albania"),
  ("algeria","Algeria"),
  ("andorra","Andorra"),
  ("angola","Angola"), 
  ("Antigua", "Barbuda"),
  ("argentina","Argentina"), 
  ("armenia","Armenia"),
  ("australia","Australia"),
  ("india","India"),
  ("america","America"),
  ("unitedKingdom","UnitedKingdom"),
  ("france","France"),
  ("russia","Russia"),
  ("italy","Italy"),
  ("china","China"),
  ("nepal","Nepal"),
  ("brazil","Brazil"),
  ("germany","Germany"),
  ("argentina","Argentina"),
  ("poland","Poland"),
  ("wales","Wales"),
  ("norway","Norway"),
  ("srilanka","Srilanka"),
  ("uae","UAE"),
  ("australia","Australia"),
  ("japan","Japan"),
  ("newsland","Newsland"),
  ("southAfrica","SouthAfrica")
)

disct=(

	("select a District","Select a District"),
	("thiruvandapuram","Thiruvandapuram"),
	("ernakulam","Ernakulam"),
	("pathanamthitta","Pathanamthitta"),
	("palakkad","Palakkad"),
	("thrissur","Thrissur"),
	("idduki",'Idduki'),
	("malppuram","Malppuram"),
	("kozhikode","Kozhikode"),
	("wayanad","Wayanad"),
	 ("kannur","Kannur"),
	 ("kasaragod","Kasaragod"),
	 ("huston","Huston"),
	 ("manchister","Manchister"),
	 ("liverpool","LiverPool"),
	 ("bayerMunich","ByerMunich")
     

	   )

sta=(
          
		  ("select a State","Select a State"),
          ("kerela","Kerela"),
          ("newyork","NewYork"),
          ("tokiyo","Tokiyo"),
          ("bejeing","Bejeing"),
          ("berlin","Berlin"),
		)

stas=(


    ("select Status","Select Status"),
    ("active","Active"),
    ("inactive","Inactive"),



  )



class EmployeeForm(forms.ModelForm):
  class Meta():
    model=EmployeeRegisterTB
    fields="__all__"
    

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','password1','password2','email')


    
  
    # username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    # email = forms.EmailField(label='Enter Email')
    # password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    


    # def clean_username(self):
    #     username = self.cleaned_data['username'].lower()
    #     r = User.objects.filter(username=username)
    #     if r.count():
    #         raise ValidationError("Username already exists")
    #     return username


    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     r = User.objects.filter(email=email)
    #     if r.count():
    #         raise  ValidationError("Email already exists")
    #     return email
 
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
 
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password don't match")
 
    #     return password2
 
    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #     return user

class BranchForm(forms.Form):
  BranchName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchContactnumber=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchEmail=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchAddress=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchCity=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchState=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchPincode=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  BranchCountry=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

  class AdminProfile(forms.ModelForm):
    password=None
    class Meta:
        model=User
        fields='__all__'

class NotificationsForm(forms.Form):
  # class Meta:
  #   model=NotificationsTB
  #   fields='__all__'
  Shippername=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  Description=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'class':'form-control','row':'5'}))
  Status=forms.CharField(widget=forms.Select(choices=notf,attrs={'class':'form-control'}))
  DeliveryDate=forms.DateField(widget=NumberInput(attrs={'type': 'date','class':'form-control'}))

  





  

 

        