from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70,unique=True)
    phone_number = models.CharField(max_length=12)
   
    def __str__(self):
        return str(self.id) +"_"+ self.first_name


class SlotPreference(models.Model):
    employee = models.ForeignKey(
            Employee, on_delete=models.CASCADE)
    slots=(
        ('06:00am-02:00pm','06:00am-02:00pm'),
        ('02:00pm-10:00pm','02:00pm-10:00pm'), 
        ('10:00pm-06:00am','10:00pm-06:00am'),
    )
    preferred_slot = models.CharField(max_length=15,choices=slots,default=None)
    date = models.DateField(default=None,auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.employee.id)+"_"+str(self.date)


class Data_from_manager(models.Model):
    store_id = models.IntegerField(default=None,blank=False)
    total_no_of_emp = models.IntegerField(blank=False)
    max_emp_in_1slot = models.IntegerField(blank=False)
    min_emp_in_1slot = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.store_id)

class Scheduler(models.Model):
    employee = models.ForeignKey(
            Employee, on_delete=models.CASCADE)
    slots=(
        ('06:00am-02:00pm','06:00am-02:00pm'),
        ('02:00pm-10:00pm','02:00pm-10:00pm'), 
        ('10:00pm-06:00am','10:00pm-06:00am'),
    )
    assigned_slot = models.CharField(max_length=15,choices=slots,blank=False)
    scheduling_day = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.employee.id)+ "_" + self.assigned_slot
    
