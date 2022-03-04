from email.mime import application
from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group,User
from .models import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,admin_only,applicant_only

# Create your views here.

#Register Function
@unauthenticated_user
def Register(request):

    #Register Fuctionality
    reg_form = createUserForm()

    if request.method == 'POST':
        reg_form = createUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            #username = reg_form.cleaned_data.get('username')

            #Adding To Group(Customers)
            group = Group.objects.get(name='applicant')
            user.groups.add(group)

            #Creating an Applicant
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


            #Auto Login
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')

            userreg = authenticate(username=username, password=password)
            login(request, userreg)
            return redirect('personal_info')


    context = {'reg_form':reg_form}

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

#Inherit Dashboard
@login_required(login_url='login')
@admin_only
def InDash(request):
    return render(request, 'dashFolder/inhDash.html')
    
#Numbers
@login_required(login_url='login')
@admin_only
def Numbers(request):
    return render(request, 'dashFolder/numDash.html') 

#allApplicants
@login_required(login_url='login')
@admin_only
def allApplicants(request):
    return render(request, 'dashFolder/allApplicants.html') 

#Short List
@login_required(login_url='login')
@admin_only
def ShortList(request):
    return render(request, 'dashFolder/shortList.html') 

#Approved
@login_required(login_url='login')
@admin_only
def Approved(request):
    return render(request, 'dashFolder/approved.html')

#Unverified
@login_required(login_url='login')
@admin_only
def Unverified(request):
    return render(request, 'dashFolder/unverified.html')   


#Unverified
@login_required(login_url='login')
@admin_only
def Information(request):
    return render(request, 'dashFolder/info.html')                         