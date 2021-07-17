from django import forms
from.models import Cargotb,BookingTB,OrderTb,PaymentTB
from django.forms.widgets  import NumberInput



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

shiptype=(  
	
       ("select type","Select atype"),
       ("airPlane","Airplane"),
       ("ship","Ship"),
       ("truck","Truck"),
	     

)
Type=(

        
        ("select type","Select type"),
        ("documents","Documents"),
        ("clothes","Clothes"),
        ("electronics","Electronics"),
        ("households","Households"),
        ("chemicals","Chemicals"),
        ("liquids","Liquids"),

	)

Em=(

       ("01","01"),
       ("02","02"),
       ("03","03"),
       ("04","04"),
       ("05","05"),
       ("06","06"),
       ("07","07"),
       ("08","08"),
       ("09","09"),
       ("10","11"),
       ("12","12"),

	         )

Ey=(

       ("2021","2021"),
       ("2022","2022"),
       ("2023","2023"),
       ("2024","2024"),
     

	         )

class RegisterForm(forms.Form):
	Firstname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	Lastname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	DateOfBirth=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control'}))   
	choice=[('Male','male'),('Female','female')]
	Gender=forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
	Age=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Country=forms.CharField(label='Select Country',widget=forms.Select(choices=cntry,attrs={'class':'form-control'}))
	State=forms.CharField(label="Select State",widget=forms.Select(choices=sta,attrs={'class':'form-control'}))
	District=forms.CharField(label="Select District",widget=forms.Select(choices=disct,attrs={'class':'form-control'}))
	Address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':'5'}),required=True)
	ContactNumber=forms.CharField(max_length = 100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
	Email=forms.EmailField(max_length = 100,required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
	Photo=forms.ImageField()
	Username=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	ConfirmPassword=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))




class LoginForm(forms.Form):
	Username=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Please Enter Your Username'}))
	Password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Please Enter Your Password'}))

class BookingForm(forms.Form):
	Origin=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Shippername=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Email=forms.EmailField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	ContactNumber=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	ShipperAddress=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':'3'}),required=True)
	Destination=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	DeliveryDate=forms.DateField(widget=forms.NumberInput(attrs={'type':'date','class':'form-control'}))
	Recivername=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	ReciverEmail=forms.EmailField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	ReciverContact=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	ReciverAddresss=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':'3'}),required=True)
	ReciverPin=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	ReciverDistrict=forms.CharField(label="Select District",widget=forms.Select(choices=disct,attrs={'class':'form-control'}))
	ReciverState=forms.CharField(label="Select State",widget=forms.Select(choices=sta,attrs={'class':'form-control'}))	
	ReciverCountry=forms.CharField(label='Select Country',widget=forms.Select(choices=cntry,attrs={'class':'form-control'}))
	CargoWeigth=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	CargoQuantity=forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	ShipmentType=forms.CharField(label="Select type",widget=forms.Select(choices=shiptype,attrs={'class':'form-control'}))
	NetRate=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Type=forms.CharField(label="Select Type",widget=forms.Select(choices=Type,attrs={'class':'form-control'}))
    

class ProfileForm(forms.ModelForm):
	class Meta():
		model=Cargotb
		fields=('Firstname','Lastname','DateOfBirth','Gender','Age','Country','State','District','Address','ContactNumber','Email','Photo','Username','Password','ConfirmPassword')
             

class ChangePasswordForm(forms.Form):
	OldPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	NewPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	ConfirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))




class FeedbackForm(forms.Form):
	Comments=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':'3'}),required=True)

class OrderForm(forms.Form):
	class Meta():
		model=BookingTB
		fields='__all__'


class PaymentForm(forms.Form):
	CardholdersName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CardholdersName'}))
	CardNumber=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CardNumber'}))
	CVV=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'CVVCode'}))
	ExpiryMonth=forms.CharField(widget=forms.Select(choices=Em,attrs={'class':'form-control'}))
	ExpiryYear=forms.CharField(widget=forms.Select(choices=Ey,attrs={'class':'form-control'}))
	Amount=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'0.00'}))