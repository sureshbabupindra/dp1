from django.contrib import admin

from .models import pumpInstData
from .models import ind
from .models import dd

from import_export.admin import ImportExportModelAdmin

#admin.site.register(pumpInstData)

# Register your models here.

@admin.register(pumpInstData)
@admin.register(ind)
@admin.register(dd)

class pumpInstDataAdmin(ImportExportModelAdmin):
	pass

class indAdmin(ImportExportModelAdmin):
	pass

class ddAdmin(ImportExportModelAdmin):
	pass