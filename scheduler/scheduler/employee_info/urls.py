from django.urls import path
from .views import *

urlpatterns = [
    
    path('create/',create_employee),
    path('get/<int:employee_id>/',get_employee),
    path('update/<int:employee_id>/',update_employee),
    path('delete/<int:employee_id>/',delete_employee),
    
    path('create/manageral/',create_manageral_data),

    path('create/scheduler/<int:store_id>/',create_scheduler),

]