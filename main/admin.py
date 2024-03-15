from django.contrib import admin
from . import models

#main ichidagi modellar django adminga regstartsiya qilindi
admin.site.register(models.Home)
admin.site.register(models.Table)
admin.site.register(models.Comment)
admin.site.register(models.Contact)
admin.site.register(models.MedicalThem)
admin.site.register(models.ServiceInformation)
admin.site.register(models.Services)