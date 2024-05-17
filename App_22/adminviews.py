from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App_22.form import customerForm, WorkmanagerForm, LoginForm, AdminFeedbackForm, CustomerFeedbackForm, ScheduleAdd, \
    AppointmentForm, WorksheetForm
from App_22.models import Notification, Customer, Workmanager, Feedback, AppointmentSchedule, Appointment, worksheet



@login_required(login_url='login_view')
def viewA(request):
    data = Notification.objects.all()
    print(data)
    return render(request, 'viewadmin.html', {'data': data})
@login_required(login_url='login_view')
def view_data(request):
    data=Customer.objects.all()
    print(data)
    return render(request,'customer_data.html',{'data':data})

@login_required(login_url='login_view')
def delete(request, id):
    if request.method == 'POST':
      data = Notification.objects.get(id=id)
      data.delete()
      return redirect("view")



@login_required(login_url='login_view')
def delete_data(request, id):
    if request.method == 'POST':
        data = Customer.objects.get(id=id)
        data.delete()
        return redirect("view_data")
@login_required(login_url='login_view')
def view_manager(request):
    data = Workmanager.objects.all()
    print(data)
    return render(request, 'manager_data.html', {'data': data})

@login_required(login_url='login_view')
def update(request,id):
    data2=Workmanager.objects.get(id=id)
    # form1=LoginForm(instance=data2)
    form2=WorkmanagerForm(instance=data2)
    if request.method=='POST':
        form=WorkmanagerForm(request.POST,instance=data2)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'update.html',{'form2':form2})

@login_required(login_url='login_view')
def delete_manager(request, id):
    if request.method == 'POST':
        data = Workmanager.objects.get(id=id)
        data.delete()
        return redirect("view_data")
@login_required(login_url='login_view')
def feedback_view(request):
    data =Feedback.objects.all()
    return render(request, 'admin11/feedbackview.html', {'data':data,})


@login_required(login_url='login_view')
def reply(request,id):
    form= Feedback.objects.get(id=id)
    if request.method == 'POST':
        form2 =request.POST.get('reply')
        form.reply=form2
        form.save()
        return redirect('feedback_view')
    return render(request, 'admin11/reply1.html', {'form':form})

@login_required(login_url='login_view')
def schedule(request):
    form = ScheduleAdd()
    if request.method == 'POST':
        form1 = ScheduleAdd(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('schedule')
    return render(request, 'admin11/schedule.html', {'form': form})

@login_required(login_url='login_view')
def delete_schedule(request, id):
    if request.method == 'POST':
      data =AppointmentSchedule.objects.get(id=id)
      data.delete()
      return redirect("admin_view")
@login_required(login_url='login_view')
def admin_view(request):
    data=AppointmentSchedule.objects.all()
    return render(request, 'admin11/adminschedule_view.html', {'data':data})

@login_required(login_url='login_view')
def appointment_view(request):
    data =Appointment.objects.all()
    return render(request, 'admin11/appointments.html', {'data':data,})


@login_required(login_url='login_view')
def accept(request,id):
    form1=Appointment.objects.get(id=id)
    if request.method=='POST':
        form1.status=1
        form1.save()
    return redirect('appointment_view')

@login_required(login_url='login_view')
def reject(request,id):
    if request.method == 'POST':
     form=Appointment.objects.get(id=id)
     form.status=2
     form.save()
    return redirect('appointment_view')
@login_required(login_url='login_view')
def work_assign(request):
    form = WorksheetForm()
    if request.method == 'POST':
        form1 = WorksheetForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('base1')
    return render(request, 'admin11/worksheet.html', {'form': form})
@login_required(login_url='login_view')
def work_status(request):
    form= worksheet.objects.all()
    return render(request, 'admin11/work_status.html', {'form':form})
@login_required(login_url='login_view')
def delete_work(request, id):
    if request.method == 'POST':
      data =worksheet.objects.get(id=id)
      data.delete()
      return redirect("work_status")


