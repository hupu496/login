from django.contrib import admin
from .models import OTP
admin.site.register(OTP)

#class OtpInline(admin.TabularInline):
#    model = Otp
#    extra = 3
#class UserAdmin(admin.ModelAdmin):
    #fieldsets = [(None, {'fields': ['username']}),
    #             ('email', {'fields': ['email']}),
   #              ('paasword1', {'fields': ['password1']}),
  #              ('password2', {'fields': ['password2']}),
 #    ]
#    inlines = [OtpInline]


#admin.site.register(User,UserAdmin)