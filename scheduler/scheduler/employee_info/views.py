from django.shortcuts import render
from .models import Employee, Data_from_manager,Scheduler, SlotPreference
import json
from django.http import HttpResponse
import datetime
from .utils import sorter, serializer

def create_employee(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        employee_object = Employee(first_name=body['first_name'],last_name=body['last_name'],
                                    email=body['email'],phone_number=body['phone_number'])
        employee_object.save()
        employee_obj={}
        employee_obj['first_name'] = employee_object.first_name
        employee_obj['last_name'] = employee_object.last_name
        employee_obj['email'] = employee_object.email
        employee_obj['phone_number'] = employee_object.phone_number

        return HttpResponse(json.dumps({'success':True,'employee_info':employee_obj}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))


def get_employee(request,employee_id):
    if request.method == "GET":
        employee_object = Employee.objects.get(id=employee_id)
        employee_obj={}
        employee_obj['first_name'] = employee_object.first_name
        employee_obj['last_name'] = employee_object.last_name
        employee_obj['email'] = employee_object.email
        employee_obj['phone_number'] = employee_object.phone_number

        return HttpResponse(json.dumps({'success':True,'employee_info':employee_obj}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))


def update_employee(request,employee_id):
    if request.method == "PUT":

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        employee_obj = Employee.objects.get(id=employee_id)
        employee_obj.first_name = body['first_name']
        employee_obj.last_name = body['last_name']
        employee_obj.email = body['email']
        employee_obj.phone_number = body['phone_number']
        employee_obj.save()

        employee_data={}
        employee_data['first_name'] = employee_obj.first_name
        employee_data['last_name'] = employee_obj.last_name
        employee_data['email'] = employee_obj.email
        employee_data['phone_number'] = employee_obj.phone_number


        return HttpResponse(json.dumps({'success':True,'employee_info':employee_data}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))

def delete_employee(request,employee_id):
    if request.method == "DELETE":

        employee_object = Employee.objects.get(id=employee_id)
        employee_object.delete()

        return HttpResponse(json.dumps({'success':True}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))


def create_manageral_data(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data_object = Data_from_manager(total_no_of_emp=body['total_no_of_emp'],store_id=body['store_id'],
                        max_emp_in_1slot=body['max_emp_in_1slot'],min_emp_in_1slot=body['min_emp_in_1slot'])
        data_object.save()
        data_obj={}
        data_obj['store_id'] = data_object.store_id
        data_obj['total_no_of_emp'] = data_object.total_no_of_emp
        data_obj['max_emp_in_1slot'] = data_object.max_emp_in_1slot
        data_obj['min_emp_in_1slot'] = data_object.min_emp_in_1slot

        return HttpResponse(json.dumps({'success':True,'manageral_data':data_obj}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))

def create_slot_preference(request,employee_id):
    if request.method == "POST":

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        employee_obj = Employee.objects.get(id=employee_id)

        data_object = SlotPreference(preferred_slot=body['preferred_slot'],employee=employee_obj,
                                        date=datetime.datetime.now().date() )
        data_object.save()

        data_obj={}
        data_obj['employee_id'] = employee_id
        data_obj['preferred_slot'] = data_object.preferred_slot

        return HttpResponse(json.dumps({'success':True,'employee_preference':data_obj}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))

def create_scheduler(request,store_id):

    if request.method == "POST":
        list_6_2 = []
        list_2_10 = []
        list_10_6 = []
        preference_obj = SlotPreference.objects.filter(date=datetime.datetime.now().date())

        manageral_obj = Data_from_manager.objects.get(store_id=store_id)
        for objects in preference_obj:

            if objects.preferred_slot == '06:00am-02:00pm':
                list_6_2.append(objects)  

            if objects.preferred_slot == '02:00pm-10:00pm':
                list_2_10.append(objects)

            if objects.preferred_slot == '10:00pm-06:00am':
                list_10_6.append(objects)
        
        length_list_6_2 = len(list_6_2)
        length_list_2_10 = len(list_2_10)
        length_list_10_6 = len(list_10_6)

        if length_list_6_2>=manageral_obj.min_emp_in_1slot and length_list_10_6>=manageral_obj.min_emp_in_1slot and length_list_2_10>=manageral_obj.min_emp_in_1slot and length_list_6_2<=manageral_obj.max_emp_in_1slot and length_list_10_6<=manageral_obj.max_emp_in_1slot and length_list_2_10<=manageral_obj.max_emp_in_1slot:
            pass

        else:
            sorter(list_6_2,list_2_10,list_10_6,manageral_obj)
            sorter(list_2_10,list_10_6,list_6_2,manageral_obj)
            sorter(list_10_6,list_2_10,list_6_2,manageral_obj)
        
        scheduler_data={}
        scheduler_data_obj={}
        
        for terms in list_6_2:
            scheduler_object = Scheduler(employee=terms.employee,assigned_slot='06:00am-02:00pm',
                                        scheduling_day=datetime.datetime.now().date())
            scheduler_object.save() 
            scheduler_data=serializer(scheduler_data,scheduler_data_obj,scheduler_object)

        for terms in list_2_10:
            scheduler_object = Scheduler(employee=terms.employee,assigned_slot='02:00pm-10:00pm',
                                        scheduling_day=datetime.datetime.now().date())
            scheduler_object.save()
            scheduler_data=serializer(scheduler_data,scheduler_data_obj,scheduler_object)

        for terms in list_10_6:  
            scheduler_object = Scheduler(employee=terms.employee,assigned_slot='10:00pm-06:00am',
                                        scheduling_day=datetime.datetime.now().date())
            scheduler_object.save()
            scheduler_data=serializer(scheduler_data,scheduler_data_obj,scheduler_object)
        
        return HttpResponse(json.dumps({'success':True,'scheduler_data':scheduler_data}))

    return HttpResponse(json.dumps({'success':False,'message':'wrong request type'}))


