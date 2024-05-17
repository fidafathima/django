from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App_22.form import LoginForm, WorkmanagerForm, customerForm, NotificationForm
from App_22.models import Notification, AppointmentSchedule, Customer, Appointment, Feedback


# Create your views here.
def demo(request):
    reply = Feedback.objects.all()
    return render(request,'index.html',{'reply':reply})
def base1(request):
    return render(request,'admin11/admin_base.html')

def base2(request):
    return render(request,'customer/customer_base.html')

def base3(request):
    return render(request,'workmanager/workmanager_base.html')

# def login(request):
#     return render(request,'login/log.html')
def work(request):
    form1=LoginForm()
    form2=WorkmanagerForm()
    if request.method=='POST':
            form1=LoginForm(request.POST)
            form2=WorkmanagerForm(request.POST,request.FILES)

            if form1.is_valid() and form2.is_valid():
                a=form1.save(commit=False)
                a.is_worksmanager=True
                a.save()
                user1=form2.save(commit=False)
                user1.user=a
                user1.save()
                return redirect('login_view')

    return render(request,'registration.html',{'form1':form1,'form2':form2})

def customerdata(request):
    form3=LoginForm()
    form4=customerForm()
    if request.method=='POST':
            form3=LoginForm(request.POST)
            form4=customerForm(request.POST)

            if form3.is_valid() and form4.is_valid():
                a=form3.save(commit=False)
                a.is_customer=True
                a.save()
                user1=form4.save(commit=False)
                user1.user=a
                user1.save()
                return redirect('login_view')

    return render(request,'customer.html',{'form3':form3,'form4':form4})

@login_required(login_url='login_view')
def note(request):
    form = NotificationForm()
    if request.method == 'POST':
        form1 = NotificationForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('demo')
    return render(request, 'note.html', {'form': form})

def login_view(request):
        if request.method=='POST':
            username=request.POST.get('uname')
            print(username)
            password=request.POST.get('pass')
            print(password)
            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('base1')
                elif user.is_worksmanager:
                    return redirect('profile_manager')
                elif user.is_customer:
                    return redirect('profile_cstmr')
            else:
                messages.info(request,"invalid credentials")
        return render(request,'login01/login_page.html')


def demo1(request):
    return render(request,'thank.html')

def demo2(request):
    return render(request,'message.html')
def logout_view(request):
    logout(request)
    return redirect('login_view')






