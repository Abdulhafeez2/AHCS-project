from hospital_admin.models import ReceptionistInfo
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django import forms
from . import utils
import random
from django.conf import settings
from django.core.mail import send_mail

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']
        
class ReceptionistCreationForm(forms.Form):
    firstname=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name here... '}))
    middlename=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Middle Name here... '}))
    lastname=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name here... '}))
    sex=forms.CharField(required=True,max_length=1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Sex here... '}))
    age=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Age here... '}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email here... '}))
    region=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Region here.. '}))
    zone=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Zone here... '}))
    woreda=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Woreda here... '}))
    kebele=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Kebele here... '}))
    house_no=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'House No here...'}))
    phone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone number here..'}))
    
    def save(self):
        
        password=User.objects.make_random_password()
        username1=utils.generate_random_username()
        

        new_receptionist_basic=User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            email=self.cleaned_data.get('email'),
            username=username1
        )
        group=Group.objects.get(name="Receptionist")
        new_receptionist_basic.groups.add(group)
        new_receptionist_info=ReceptionistInfo.objects.create(
            user_id=new_receptionist_basic.id,
            middle_name=self.cleaned_data.get('middlename'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
            phone=self.cleaned_data.get('phone'),
        )
        '''
        subject="User Name and Password"
        message= username1,password
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[new_receptionist_basic.email]
        send_mail(subject,message,email_from,recipient_list)'''
        new_receptionist_basic.set_password(password)
        new_receptionist_basic.save()
        new_receptionist_info.save()
        context={'username':username1,"password":password}
        return context

class NurseCreationForm(forms.Form):
    firstname=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name here... '}))
    middlename=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Middle Name here... '}))
    lastname=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name here... '}))
    sex=forms.CharField(required=True,max_length=1,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Sex here... '}))
    age=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Age here... '}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email here... '}))
    region=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Region here.. '}))
    zone=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Zone here... '}))
    woreda=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Woreda here... '}))
    kebele=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Kebele here... '}))
    house_no=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'House No here...'}))
    phone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone number here..'}))
    
    def save(self):
        
        password=User.objects.make_random_password()
        username1=utils.generate_random_username()
        

        new_receptionist_basic=User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            email=self.cleaned_data.get('email'),
            username=username1
        )
        group=Group.objects.get(name="Nurse")
        new_receptionist_basic.groups.add(group)
        new_receptionist_info=ReceptionistInfo.objects.create(
            user_id=new_receptionist_basic.id,
            middle_name=self.cleaned_data.get('middlename'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
            phone=self.cleaned_data.get('phone'),
        )
        
        new_receptionist_basic.set_password(password)
        new_receptionist_basic.save()
        new_receptionist_info.save()
        context={'username':username1,"password":password}
        return context
    