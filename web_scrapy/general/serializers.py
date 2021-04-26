from rest_framework import serializers
from general.models import EarthquakeXLSX

class EarthquakeXLSXSerializer(serializers.ModelSerializer):
    xlsx_file = serializers.SerializerMethodField()
    class Meta:
        model = EarthquakeXLSX
        fields = ['created_date', 'xlsx_file', 'updated_date']
    
    def get_xlsx_file(self, obj):
        return ("http://127.0.0.1:8000"+str(obj.xlsx_file.url))
        
