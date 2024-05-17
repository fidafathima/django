from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App_22.form import CustomerFeedbackForm, AppointmentForm
from App_22.models import Notification, Feedback, AppointmentSchedule, Appointment, Customer, worksheet

@login_required(login_url='login_view')
def viewC(request):
    data = Notification.objects.all()
    print(data)
    return render(request, 'viewcustomer.html', {'data': data})

@login_required(login_url='login_view')
def feedback(request):
    form =CustomerFeedbackForm()
    u =request.user
    print(u)
    if request.method == 'POST':
        form1 = CustomerFeedbackForm(request.POST)
        if form1.is_valid():
            obj=form1.save(commit=False)
            obj.user=u
            obj.save()

            return redirect('demo1')
    return render(request, 'feedback.html', {'form':form})
@login_required(login_url='login_view')
def viewreply(request):
    reply = Feedback.objects.all()
    return render(request, 'customer/replyview.html', {'reply':reply})
@login_required(login_url='login_view')
def viewschedule(request):
    data=AppointmentSchedule.objects.all()
    return render(request, 'customer/scheduleview.html', {'data':data})
# @login_required(login_url='login_view')
def appointment(request,id):
    schedule=AppointmentSchedule.objects.get(id=id)
    u=Customer.objects.get(user=request.user)
    appointment=Appointment.objects.filter(user=u,schedule=schedule)
    if appointment.exists():
        messages.info(request,'you have already requested appointment')
        return redirect('viewschedule')
    else:
        if request.method=='POST':
            obj=Appointment()
            obj.user=u
            obj.schedule=schedule
            obj.save()
            messages.info(request,'Appointment booked successfully')
            return redirect('demo2')

@login_required(login_url='login_view')
def booking_status(request):
    user1=request.user
    user2=Customer.objects.get(user=user1)
    data=Appointment.objects.filter(user=user2)
    return render(request, 'customer/booking_status.html', {'data':data})
@login_required(login_url='login_view')
def view_work(request):
    user1=request.user
    user2 = Customer.objects.get(user=user1)
    work=worksheet.objects.filter(customer=user2)
    return render(request, 'customer/workview.html', {'work':work})

@login_required(login_url='login_view')
def profile_cstmr(request):
    user1=request.user
    form1=Customer.objects.get(user=user1)
    return render(request, 'customer/customer_profile.html', {'form1':form1})

