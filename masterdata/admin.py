# -*- coding: utf-8 -*-
from django.contrib import admin

from masterdata.models import SD_creation,MD_creation,Donor,Profile

# Register your models here.
class SD_creationAdmin(admin.ModelAdmin):
    list_display = ('name','creation_name')


admin.site.register(SD_creation,SD_creationAdmin)
admin.site.register(MD_creation)
admin.site.register(Donor)
admin.site.register(Profile)