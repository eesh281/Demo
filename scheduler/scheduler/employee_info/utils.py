from datetime import date, datetime

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def serializer(scheduler_data,scheduler_data_obj,scheduler_object):
    scheduler_data_obj['employee_id']=scheduler_object.employee.id
    scheduler_data_obj['employee_name']=scheduler_object.employee.first_name
    scheduler_data_obj['assigned_slot']=scheduler_object.assigned_slot
    scheduling_day = json_serial(scheduler_object.scheduling_day)
    scheduler_data_obj['scheduling_day']=scheduling_day

    scheduler_data[scheduler_object.id] = scheduler_data_obj
    return scheduler_data


def sorter(lista,listb,listc,manageral_obj):
    while len(lista) > manageral_obj.max_emp_in_1slot:
        popped_element = lista[-1]
        
        del lista[-1]  
            
        if listb>len(listc):  
            listc.append(popped_element)
        else:
            listb.append(popped_element)

    if len(lista) < manageral_obj.min_emp_in_1slot:
        
        if len(listb)>len(listc):
            popped_element_1 = listb[-1]
            
            del listb[-1]
            
            lista.append(popped_element_1)
        else:
            popped_element_1 = listc[-1]
            del listc[-1]
            lista.append(popped_element_1)

