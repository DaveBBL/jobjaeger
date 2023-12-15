from django.contrib import admin

from .models import Company, Role, Interview

admin.site.register(Company)
admin.site.register(Role)
admin.site.register(Interview)
