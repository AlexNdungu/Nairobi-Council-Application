from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Gender)
admin.site.register(Application)
admin.site.register(Next)
admin.site.register(Edu_Level)
admin.site.register(Higher)
admin.site.register(Secondary)
admin.site.register(Primary)
admin.site.register(County)
admin.site.register(Upload)
admin.site.register(State)