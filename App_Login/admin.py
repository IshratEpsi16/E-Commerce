from django.contrib import admin
from App_Login.models import User, Profile
# Register your models here.
#email: a@gmail.com, pass: 123
admin.site.register(User)
admin.site.register(Profile)