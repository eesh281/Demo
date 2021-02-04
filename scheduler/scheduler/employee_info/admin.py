from django.contrib import admin
from .models import Employee, Data_from_manager, Scheduler, SlotPreference

admin.site.register(Employee)
admin.site.register(Data_from_manager)
admin.site.register(Scheduler)
admin.site.register(SlotPreference)
