from email.mime import application
from multiprocessing import context
from re import template
from urllib import request, response
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group,User
from .models import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,admin_only,applicant_only
from django.views.generic.detail import DetailView
import urllib.request
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here
#from social_django import UserSocialAuth
# select_related for performance.
#google_logins = UserSocialAuth.objects.select_related("user").filter(provider="google-oauth2")
#for google_login in google_logins:
   # print(google_login.user.pk, google_login.user.email)
 


#The Google Register Logic
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def handle_new_job(sender, **kwargs):
    if kwargs.get('created', False):
        user = kwargs.get('instance')
        g = Group.objects.get(name='applicant')
        user.groups.add(g)

        Application.objects.create(
            user=user,
            full_name = user.username,
            email = user.email,
        )

         #Create Next Of Kin Object
        Next.objects.create(
            user=user,
            kin_email=user.email
        )

        #Create Upload Object
        Upload.objects.create(
            user=user,
        )

        #Create University Object
        Higher.objects.create(
            user=user,
        )

        #Create Secondary Object
        Secondary.objects.create(
            user=user,
        )

        #Create Primary Object
        Primary.objects.create(
            user=user,
        )

        #Create State Object
        State.objects.create(
            user=user,
            state_pk = user.pk,
        )

        ###
            
#Register Function
@unauthenticated_user
def Register(request):

    allusers = User.objects.all()

    #Register Fuctionality
    reg_form = createUserForm()

    if request.method == 'POST':
        reg_form = createUserForm(request.POST)
        if reg_form.is_valid():

            U_Email = reg_form.cleaned_data.get('email')
            if User.objects.filter(email=U_Email).exists():
                messages.warning(request, "Email already exists")   
            else:    
                reg_form.save()

                #Auto Login
                username = reg_form.cleaned_data.get('username')
                password = reg_form.cleaned_data.get('password1')

                userreg = authenticate(username=username, password=password)
                login(request, userreg)
                return redirect('personal_info')

        else:
            print(reg_form.errors)
            messages.info(request, 'Username Already Exits!!!') 


    context = {'reg_form':reg_form,'allusers':allusers}

    return render(request, 'Register.html',context)

#Requirments Page
@login_required(login_url='login')
@applicant_only
def Requir(request):
    return render(request, 'requir.html')   

#Login Fuction
@unauthenticated_user
def Login(request):

    if request.method == 'POST':

        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user1 = authenticate(username=username1, password=password1)

        if user1 is not None:
            login(request, user1)
            return redirect('numbers')
        else:
            messages.info(request, 'Username Or Password Is INCORRECT!!!')   

    return render(request, 'Login.html')


#logout user 
def logOutUser(request):
    logout(request)    
    return redirect('login')


#This is the Inherit page Fuction 
@login_required(login_url='login')
@applicant_only
def Inher(request):
    return render(request, 'regFolder/inherReg.html')   


#This is thePersonal Info Page
@login_required(login_url='login')
def PInfo(request ):

    #This is where i will handle the uploading infomation
    #I will use forms.py 

    #applicant = Application.objects.get(id=pk)

    applicant = request.user.application

    theApplicationForm = appplicantInfoForm(instance=applicant)


    if request.method == 'POST':
        theApplicationForm = appplicantInfoForm(request.POST,instance=applicant)
        if theApplicationForm.is_valid():
            theApplicationForm.save()
            return redirect('next_of_kin')
        else:
            print(theApplicationForm.errors)
            messages.info(request, 'FORM SUBMITTION FAILED!!') 


    context = {'theApplicationForm':theApplicationForm}

    return render(request, 'regFolder/PersIn.html',context)    

#Next Of Kin View Page
@login_required(login_url='login')
@applicant_only
def NextK(request):

    kin = request.user.next

    nextInfo = NextOfKinForm(instance=kin)

    #Creating records Next Of kin

    if request.method == 'POST':
        nextInfo = NextOfKinForm(request.POST,instance=kin)
        if nextInfo.is_valid():
            print('valid')
            nextInfo.save()
            return redirect('upload_Files')
        else:
            print(nextInfo.errors)
            messages.info(request, 'FORM SUBMITTION FAILED!!') 

    context = {'nextInfo':nextInfo}

    return render(request, 'regFolder/nextK.html',context)     

#Upload File Page View 
@login_required(login_url='login')
@applicant_only
def Uploads(request):

    upApp = request.user.upload
    #Uploading all file
    allFiles = upFilesAll(instance=upApp)

    #Uploading all files

    if request.method == 'POST':
        allFiles = upFilesAll(request.POST, request.FILES,instance=upApp)
        if allFiles.is_valid():
            print('valid')
            allFiles.save()
            return redirect('education')
        else:
            print(allFiles.errors)
            messages.info(request, 'FORM SUBMITTION FAILED!!')    


    context = { 'allFiles':allFiles }

    return render(request, 'regFolder/upL.html',context)    

#Educational Background Page View 
@login_required(login_url='login')
@applicant_only
def EduBg(request):

    uniInst = request.user.higher
    secInst = request.user.secondary
    priInst = request.user.primary

    #Creating Forms for view for all educational levels
    university = UniversityForm(instance=uniInst)
    secondary = SecondaryForm(instance=secInst)
    primary = PrimaryForm(instance=priInst)
    

    #Uploading university level

    if request.method == 'POST':

        university = UniversityForm(request.POST, request.FILES,instance=uniInst)
        secondary = SecondaryForm(request.POST, request.FILES,instance=secInst)
        primary = PrimaryForm(request.POST, request.FILES,instance=priInst)

        if university.is_valid() and secondary.is_valid() and primary.is_valid():
            print('valid')
            university.save()
            secondary.save()
            primary.save()
            return redirect('success')
        else:
            print(university.errors)
            print(secondary.errors)
            print(primary.errors)
            messages.info(request, 'FORM SUBMITTION FAILED!!') 

    context = {'university':university, 'secondary':secondary,'primary':primary}

    return render(request, 'regFolder/eduBg.html',context)

#Success Registeration Page View 
@login_required(login_url='login')
@applicant_only
def Success(request):
    return render(request, 'regFolder/regSuc.html')   

#Then After Being Verified, the applicant will get the pdf below

#PDF Template  
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):

        #Add A context dict to contain all the neccesary items

        context = {
            'userPic': request.user.upload.get_image_path,
            'full_name': request.user.application.full_name,
            'nat_id': request.user.application.nat_id,
            'institute': request.user.higher.institution,
            'course': request.user.higher.course,
            'email': request.user.application.email,
            'phone': request.user.application.phone,
        }

        pdf = render_to_pdf('extras/pdf.html',context)
        return HttpResponse(pdf, content_type='application/pdf')

#Download pdf
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):

        context = {
            'userPic': request.user.upload.get_image_path,
            'full_name': request.user.application.full_name,
            'nat_id': request.user.application.nat_id,
            'institute': request.user.higher.institution,
            'course': request.user.higher.course,
            'email': request.user.application.email,
            'phone': request.user.application.phone,
        }

        nat_id = request.user.application.nat_id
		
        pdf = render_to_pdf('extras/pdf.html',context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "AT_%s.pdf" %(nat_id)
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response


#Inherit Dashboard
@login_required(login_url='login')
@admin_only
def InDash(request):
    return render(request, 'dashFolder/inhDash.html')
    
#Numbers
@login_required(login_url='login')
@admin_only
def Numbers(request):

    #Getting the number of applicants
    applicants_numbers = Application.objects.all()
    allApps = applicants_numbers.count()

    #Getting the number of verified users
    ver = User.objects.filter(state__verified=True)
    verA = ver.count()


    #Getting Unverifed People
    pend = User.objects.filter(state__shortlist=False)
    pendAll = pend.count()

    #Number Of Short Listed Users
    allU = User.objects.filter(state__shortlist=True).exclude(state__verified=True)
    shortListNum = allU.count()

    context = {'allApps':allApps,'shortListNum':shortListNum,'verA':verA,'pendAll':pendAll}

    return render(request, 'dashFolder/numDash.html',context) 

#allApplicants
@login_required(login_url='login')
@admin_only
def allApplicants(request):

    #group = Group.objects.get(name='applicant')
    allApplicant = User.objects.filter(state__unverified=True)

    context = {'allApplicant':allApplicant}

    return render(request, 'dashFolder/allApplicants.html',context) 

#Short List
@login_required(login_url='login')
@admin_only
def ShortList(request):

    #group = Group.objects.get(name='applicant')
    allShorts = User.objects.filter(state__shortlist=True).exclude(state__verified=True)

    context = {'allShorts':allShorts}

    return render(request, 'dashFolder/shortList.html',context) 

#Approved
@login_required(login_url='login')
@admin_only
def Approved(request):

    #group = Group.objects.get(name='applicant')
    allShorts = User.objects.filter(state__verified=True)

    context = {'allShorts':allShorts}

    return render(request, 'dashFolder/approved.html',context)

#Unverified
@login_required(login_url='login')
@admin_only
def Unverified(request):

    #group = Group.objects.get(name='applicant')
    allShorts = User.objects.filter(state__shortlist=False)

    context = {'allShorts':allShorts}


    return render(request, 'dashFolder/unverified.html',context)   

#Applicatnt Details
class userInfo(DetailView):
    model = User
    template_name = 'dashFolder/info.html'
    context_object_name = 'appDetail'    
    form_class = shortChange

    def get_form(self):

        stateform = State.objects.get(pk=self.kwargs.get('pk'))
        formstate = shortChange(instance=stateform)

        return formstate



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userview = User.objects.get(pk=self.kwargs.get('pk'))

        context.update({
            'update_state_form': self.get_form(),
        })

        return context

    #Saving The data
    #To submit with post in a class you need the post method

    def post(self, request, *args, pk):

        stateform = State.objects.get(pk=pk)
        formstate = shortChange(instance=stateform)

        if request.method == 'POST':
            formstate = shortChange(request.POST, request.FILES,instance=stateform)
            if formstate.is_valid():
                print('Valid')
                formstate.save()
            else:
                print(formstate.errors)
                messages.info(request, 'FORM SUBMITTION FAILED!!') 

        return self.get(request, *args, pk)
    
    

 #Email Template
def Email(request):
    return render(request, 'extras/email.html')   


#Error Handling
""" 
def pageError(request,exception):
    return render(request, 'errors/404.html')

def pageError1(request,exception):
    return render(request, 'errors/403.html')  

def pageError2(request,exception=None):
    return render(request, 'errors/500.html')         """