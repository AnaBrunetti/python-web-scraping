from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class EarthquakeXLSX(models.Model):
    created_date = models.DateField("Created Date", auto_now=True, auto_now_add=False)
    xlsx_file = models.FileField("XLSX File", validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])
    updated_date = models.DateField("Updated Date", auto_now_add=True)    

    class Meta:        
        verbose_name = "Earthquake XLSX"
        verbose_name_plural = "Earthquake XLSXs"
