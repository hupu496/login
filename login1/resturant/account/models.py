from django.db import models
from django.contrib.auth.models import User
class OTP(models.Model):
    otp=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    pub_date = models.DateTimeField('date published',null=True)
    ip_address = models.GenericIPAddressField(null=True,blank=True)

    def __str__(self):
        return self.otp



