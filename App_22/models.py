from django.contrib.auth.models import AbstractUser
from django.db import models



class Login(AbstractUser):
  is_worksmanager = models.BooleanField(default=False)
  is_customer = models.BooleanField(default=False)

class Customer(models.Model):
  user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
  name = models.CharField(max_length=100)
  contact_no = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.TextField()

  def __str__(self):
    return self.name

class Workmanager(models.Model):
  user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='workmanager')
  name = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.TextField()
  mobile= models.CharField(max_length=100,null=False)
  document = models.FileField(upload_to='documents/')

  def __str__(self):
    return self.name
class Notification(models.Model):
  subject=models.CharField(max_length=100)
  date=models.DateField(auto_now=True)

class Feedback(models.Model):
  user = models.ForeignKey(Login,on_delete=models.CASCADE)
  date=models.DateField(auto_now=True)
  feedback=models.TextField()
  reply=models.TextField(null=True,blank=True)

class AppointmentSchedule(models.Model):
  date=models.DateField()
  start_time=models.TimeField()
  end_time=models.TimeField()


class Appointment (models.Model):
  user=models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='appointment')
  schedule=models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
  status=models.IntegerField(default=0)

class worksheet(models.Model):
  cat=(('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'))
  category=models.CharField(max_length=50,choices=cat)
  vehicle_no=models.PositiveIntegerField(null=False)
  vehicle_name=models.CharField(max_length=40,null=False)
  vehicle_model=models.CharField(max_length=40,null=False)
  vehicle_brand=models.CharField(max_length=40,null=False)

  problem_description=models.CharField(max_length=500,null=False)
  date=models.DateField(auto_now=True)
  cost=models.PositiveIntegerField(null=True,default=0)

  customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,null=True)
  workmanager=models.ForeignKey(Workmanager,on_delete=models.DO_NOTHING,null=True)

  status1=(('Repairing','Repairing'),('Repairing done','Repairing done'),('Released','Released'))
  status=models.CharField(max_length=50,choices=status1,default='pending',null=True)



