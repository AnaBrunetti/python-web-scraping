from django.contrib import admin
from general.models import EarthquakeXLSX

# Register your models here.
@admin.register(EarthquakeXLSX)
class EarthquakeXLSXAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'xlsx_file', 'updated_date']
