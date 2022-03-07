from unicodedata import name
from django.urls import path
from . import views
from App1.views import userInfo


#All Links

urlpatterns = [
    # Register Path
    path('',views.Register, name='register'),
    # Login Path
    path('Login/',views.Login, name= 'login'),

    #Logout Path
    path('logout/', views.logOutUser, name='logout'),

    # Requirments Path
    path('Requirments/',views.Requir, name= 'requirments'),
    
    # Inherit Path
    path('inher/',views.Inher, name= 'inherit' ),

    # This Is the Personal Info Page
    path('Personal Info/',views.PInfo, name='personal_info'),
    
    # This Is the Next of kin Page
    path('Next Of Kin/',views.NextK, name='next_of_kin'),
    # This Is the Education  Page
    path('Educational BackGround/',views.EduBg, name='education'),
    # This Is the Upload  Page
    path('Upload Files/',views.Uploads, name='upload_Files'),
    # This Is the Success Register Page
    path('Success/',views.Success, name='success'),
    # This Is the Inherit Dashboard Page
    path('InDash/',views.InDash, name='dash inherit'),
    # This Is the Numbers Page
    path('Numbers/',views.Numbers, name='numbers'),
    # This Is the allApplicants Page
    path('All Applicants/',views.allApplicants, name='allApplicants'),
    # This Is the ShortList Page
    path('ShortList/',views.ShortList, name='shortList'),
    # This Is the Approved Page
    path('Approved/',views.Approved, name='Approved'),
    # This Is the Unverified Page
    path('Unverified/',views.Unverified, name='unverified'),
    # This Is the Information Page
    path('applicantInfo/<str:pk>/', userInfo.as_view(), name='applicantinfo'),
]
