from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import OTP
import datetime,socket,random
def index(request):
    return render(request,'index.html')
def registerview(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('register')
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html', {'form': form})
def loginview(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username OR password is incorrect')
        #else:
        #    messages.info(request, 'Today login validation is completed this user name')

    context={}
    return render(request,'registration/login.html',context)

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')
def logoutview(request):
    logout(request)
    return redirect('index')

class emailotp:
    def email(self,request):
        if request.method == 'POST':
            u = request.POST.get('username')
            self.user = User.objects.get(username=u)
            number = range(100000, 999999)
            n = str(random.choice(number))
            host=socket.gethostname()
            ipaddress=socket.gethostbyname(host)
            self.users = OTP.objects.create(otp=n, user_id=self.user.id, pub_date=datetime.datetime.now(), ip_address=ipaddress)
            self.users.save()
            send_mail(
                'OTP receive for reset password',
                n,
                '<otprequest@gmail.com>',
                [self.user.email],
                fail_silently=False
            )
            return True
    def passwordreset(self,request):
        if request.method == 'POST':
            p = request.POST.get('password')
            otp = request.POST.get('OTP')
            verify=OTP.objects.get(otp=otp,user_id=self.user.id)
            self.user.set_password(p)
            self.user.save()
            self.users.delete()
            return True

emailotps=emailotp()

def email_request(request):
    if request.method=='POST':
        try:
            check=emailotps.email(request)
            return redirect('password_reset')
        except:
            messages.info(request, 'Wrong username insert! please insert correct username ')
    return render(request, 'registration/email.html')
def password_reset(request):
    if request.method=='POST':
        try:
            check = emailotps.passwordreset(request)
            return redirect('message')
        except:
            i=0
            while i>5:
                msg = messages.info(request, 'Wrong otp insert! please insert correct otp ')



    return render(request,'registration/password_reset.html')
def message(request):
    return render(request,'registration/message.html')
def warning(request):
    return render(request,'registration/warning.html')


