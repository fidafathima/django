from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App_22.form import WorksheetForm, WorksheetForm1, WorkmanagerForm
from App_22.models import Notification, worksheet, Workmanager

@login_required(login_url='login_view')
def viewW(request):
    data = Notification.objects.all()
    print(data)
    return render(request, 'viewwork.html', {'data': data})
@login_required(login_url='login_view')
def status(request):
    user1=request.user
    user2 = Workmanager.objects.get(user=user1)
    form = worksheet.objects.filter(workmanager=user2)
    return render(request, 'workmanager/status.html', {'form':form})
@login_required(login_url='login_view')
def update_work(request,id):
    data2=worksheet.objects.get(id=id)
    form1 = WorksheetForm1(instance=data2)
    if request.method=='POST':
        form =WorksheetForm1(request.POST,instance=data2)
        if form.is_valid():
            form.save()
            return redirect('status')
    return render(request,'workmanager/update_work.html',{'form1':form1})

@login_required(login_url='login_view')
def profile_manager(request):
    user1=request.user
    form1=Workmanager.objects.get(user=user1)
    return render(request, 'workmanager/workmanager_profile.html', {'form1':form1})

# @login_required(login_url='login_view')
# def update(request,id):
#     data2=Workmanager.objects.get(id=id)
#     form2=WorkmanagerForm(instance=data2)
#     if request.method=='POST':
#         form=WorkmanagerForm(request.POST,instance=data2)
#         if form.is_valid():
#             form.save()
#             return redirect('view')
#     return render(request,'update.html',{'form2':form2})
