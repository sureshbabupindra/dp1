from django.contrib import admin

from .models import pumpInstData

from import_export.admin import ImportExportModelAdmin

#admin.site.register(pumpInstData)

# Register your models here.

@admin.register(pumpInstData)

class pumpInstDataAdmin(ImportExportModelAdmin):
	pass