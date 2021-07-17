from django import forms



disct=(
	("select a One","Select a One"),
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

class LoginForm(forms.Form):
	Loginname=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Password=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
	BillNumber=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'BillNumber','class':'form-control'}))
	CustomerName=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Customer','class':'form-control'}))
	MobileNumber=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'MobileNumber','class':'form-control'}))
	EmailID=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'EmailID','class':'form-control'}))
	Address=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Address','class':'form-control'}))
	District=forms.CharField(label="Select One",widget=forms.Select(choices=disct,attrs={'placeholder':'Select one','class':'form-control'}))
	Destination=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Destination','class':'form-control'}))
	DeliveryAcceptDate=forms.DateField(label="DeliveryAcceptDate" ,widget=forms.SelectDateWidget(attrs={'class':'form-control'}))
	Weight=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Weight','class':'form-control'}))
	Status=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Status','class':'form-control'}))
	Amount=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'Amount','class':'form-control'}))
	choice=[("documents","Documents"),("clothes","Clothes"),("electronics","Electronics"),("households","Households"),("chemicals","Chemicals"),("liquids","Liquids")]
	PackageType=forms.ChoiceField(choices=choice,widget=forms.RadioSelect(attrs={'class':'form-check-inline'}))