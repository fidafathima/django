import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from App_22.models import Login, Customer, Workmanager, Notification, Feedback, AppointmentSchedule, Appointment, \
    worksheet


class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2')


class customerForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ('name','contact_no','email','address')

class WorkmanagerForm(forms.ModelForm):
    class Meta:
        model =Workmanager
        fields = ('name','email','address','mobile','document')

class NotificationForm(forms.ModelForm):
    class Meta:
        model =Notification
        fields = ('subject',)

class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ('feedback',)


class AdminFeedbackForm(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ('user','feedback','reply')

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleAdd(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    start_time=forms.TimeField(widget=TimeInput)
    end_time=forms.TimeField(widget=TimeInput)

    class Meta:
        model=AppointmentSchedule
        fields=('date','start_time','end_time')

    def clean(self):
        cleaned_data=super().clean()
        start=cleaned_data.get("start_time")
        end=cleaned_data.get("end_time")
        date=cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("End time should be greater than start time")
        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=('user','schedule','status')


class WorksheetForm(forms.ModelForm):
    class Meta:
        model=worksheet
        fields="__all__"

class WorksheetForm1(forms.ModelForm):
    class Meta:
        model=worksheet
        fields=('customer','cost','problem_description','status')
