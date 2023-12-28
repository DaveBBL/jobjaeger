from django.contrib import admin

from .models import Company, Role, Interview, Application, Task

admin.site.register(Company)
admin.site.register(Role)
admin.site.register(Interview)
admin.site.register(Application)
admin.site.register(Task)
