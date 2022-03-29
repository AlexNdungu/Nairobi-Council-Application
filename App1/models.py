from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.

#The Table Gender

class Gender(models.Model):

    gender = models.CharField(max_length=100, primary_key=True)      

    #Method str for rendering
    def __str__(self):
        return self.gender


#Location County

class County(models.Model):

    county = models.CharField(max_length=100, primary_key=True)

    #Method str for rendering
    def __str__(self):
        return self.county

   

#This is the Application info model

class Application(models.Model):

    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    nat_id = models.IntegerField(unique=True, verbose_name='National ID',blank=True,null=True)
    #School id Will Be unique
    #sc_id = models.CharField(max_length=100, blank=True, null=True,unique=True, verbose_name='School ID')

    full_name = models.CharField(max_length=200, blank=True, null=True,verbose_name='Full Name')   
    age = models.IntegerField(blank=True, null=True, verbose_name='Age')
    email = models.EmailField(blank=True, null=True,max_length=254, verbose_name='Email')
    phone = models.CharField(blank=True, null=True,max_length=100, verbose_name='Phone Number')
    #pp_Image = models.ImageField(blank=True, null=True, verbose_name='Passport Image')
    #Gender From Gender Models
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Gender',default='Unspecified')
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name='County',default='Nairobi')

    address = models.CharField(blank=True, null=True,max_length=100, verbose_name='Address')
    postal_code = models.CharField(blank=True, null=True,max_length=100, verbose_name='Postal Code')

    date_register = models.DateTimeField(auto_now_add=True, verbose_name='Register Date')


    #Method str for rendering
    def __str__(self):
        return self.user.username  


#Next Of Kin model

class Next(models.Model):

    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #The rest of the attributes
    kin_nat_id = models.IntegerField(unique=True, verbose_name='Next Of National ID',blank=True,null=True)
    kin_name = models.CharField(null=True, blank=True, max_length=200, verbose_name='Kin Full Name')
    kin_phone = models.CharField(blank=True, null=True,max_length=100, verbose_name='Kin Phone Number')
    kin_email = models.EmailField(blank=True, null=True,max_length=254, verbose_name='Kin Email')


    #Method str for rendering
    def __str__(self):
        return  str(self.user)


#Level of education model

class Edu_Level(models.Model):

    level = models.CharField(primary_key=True, max_length=100, verbose_name='Education Level')

    def __str__(self):
        return self.level


#University Level Model

class Higher(models.Model):

    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    institution = models.CharField(max_length=100, null=True, blank=True,verbose_name='Institution Name')
    course = models.CharField(max_length=100,null=True, blank=True,verbose_name='Course')
    level = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, verbose_name='Education Level',default='Certificate' )

    uni_start_date = models.DateField(null=True, blank=True,verbose_name='Starting Date')
    uni_finish_date = models.DateField(null=True, blank=True,verbose_name='Finishing Date')

    def __str__(self):
        return  str(self.user)


#Secondary Level

class Secondary(models.Model):

    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    institution_high = models.CharField(max_length=100, null=True, blank=True,verbose_name='HighSchool Name')
    kcse_file = models.FileField(upload_to='allFiles', verbose_name='Upload KCSE',null=True, blank=True)
    sec_start_date = models.DateField(verbose_name='Starting Date',null=True, blank=True)
    sec_finish_date = models.DateField(verbose_name='Finishing Date',null=True, blank=True)

    def __str__(self):
        return  str(self.user)


#Secondary Level

class Primary(models.Model):

    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    institution_pri = models.CharField(max_length=100, null=True, blank=True,verbose_name='Primary School Name')

    kcpe_file = models.FileField(upload_to='allFiles', verbose_name='Upload KCPE',null=True, blank=True)
    start_date = models.DateField(verbose_name='Starting Date',null=True, blank=True)
    finish_date = models.DateField(verbose_name='Finishing Date',null=True, blank=True)

    def __str__(self):
        return  str(self.user)


#Upload Details page

class Upload(models.Model):
    
    #one to one relationship
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    cv_file = models.FileField(upload_to='allFiles', verbose_name='Upload CV',null=True, blank=True)
    aP_file = models.FileField(upload_to='allFiles', verbose_name='Upload Application Letter',null=True, blank=True)
    gD_file = models.FileField(upload_to='allFiles', verbose_name='Upload Good Conduct',null=True, blank=True)
    sL_file = models.FileField(upload_to='allFiles', verbose_name='Upload School Letter',null=True, blank=True)
    natID_file = models.ImageField(upload_to='allFiles', verbose_name='Upload National ID',null=True, blank=True)
    pP_file = models.ImageField(upload_to='allFiles', verbose_name='Upload PassPort',null=True, blank=True)
    personalAcc_file = models.FileField(upload_to='allFiles', verbose_name='Upload Personal Accidents Cover',null=True, blank=True)

    def __str__(self):
        return  str(self.user)

    @property
    def image_url(self):
        if self.pP_file and hasattr(self.pP_file, 'url'):
            return self.pP_file.url

    @property
    def get_image_path(self):
        if self.pP_file:
            return os.path.join(settings.MEDIA_ROOT, self.pP_file.path)
        return ''        


class State(models.Model):

    #One to one with user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #State primary key equal to user pk
    state_pk = models.IntegerField(primary_key=True, verbose_name='State User ID')
    #This are The Applicant States
    unverified = models.BooleanField('Unverified',default=True)
    shortlist = models.BooleanField('ShortList',default=False)
    verified = models.BooleanField('Verified',default=False)
    state_date = models.DateField(verbose_name='Verification Date', auto_now=True)

    def __str__(self):
        return  str(self.user)