from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from general.serializers import EarthquakeXLSXSerializer
from general.models import EarthquakeXLSX
from pathlib import Path
from bs4 import BeautifulSoup
import requests
import json
import shutil
import datetime
import xlsxwriter
import os


# Create your views here.

def CreateXLSX(attr_list):
    os.remove("earthquakes.xlsx")
    workbook = xlsxwriter.Workbook('earthquakes.xlsx')
    worksheet = workbook.add_worksheet() 
    worksheet.write(0, 0, 'DATA E HORA (UTC)')
    worksheet.write(0, 1, 'LAT')
    worksheet.write(0, 2, 'LONG')
    worksheet.write(0, 3, 'MAG')
    worksheet.write(0, 4, 'PROFUNDIDADE (km)')
    worksheet.write(0, 5, 'LOCAL')
    worksheet.write(0, 6, 'IRIS DETALHES')
    row = 1
    col = 0
    for earthquakes in attr_list:
        worksheet.write(row, col, earthquakes['DATA E HORA (UTC)'])
        worksheet.write(row, col + 1, earthquakes['LAT'])
        worksheet.write(row, col + 2, earthquakes['LONG'])
        worksheet.write(row, col + 3, earthquakes['MAG'])
        worksheet.write(row, col + 4, earthquakes['PROFUNDIDADE (km)'])
        worksheet.write(row, col + 5, earthquakes['LOCAL'])
        worksheet.write(row, col + 6, earthquakes['IRIS DETALHES'])
        row += 1 
    workbook.close()          

class ScrapyView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            page = requests.get('http://ds.iris.edu/seismon/eventlist/index.phtml')
            soup = BeautifulSoup(page.text, 'html.parser')
            body = soup.body
            table = soup.find( 'table', { 'class' : 'tablesorter'} ) 
            trs = table.find_all('tr')
            attr_list = []
            for tr in trs[1:]:
                attr_list.append({
                    "DATA E HORA (UTC)": tr.find_all('td')[0].get_text(strip=True),
                    "LAT": tr.find_all('td')[1].get_text(strip=True),                
                    "LONG": tr.find_all('td')[2].get_text(strip=True),
                    "MAG": tr.find_all('td')[3].get_text(strip=True),
                    "PROFUNDIDADE (km)": tr.find_all('td')[4].get_text(strip=True),
                    "LOCAL": tr.find_all('td')[5].get_text(strip=True),
                    "IRIS DETALHES": "http://ds.iris.edu/ds/nodes/dmc/tools/event/"+tr.find_all('td')[6].get_text(strip=True)                
                })
            CreateXLSX(attr_list)        
            return Response({"earthquakess": attr_list})
        except Exception as e:
            return Response({"erro": str(e)})         

class FileView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            now = str(datetime.datetime.now())[:19]
            now = now.replace(":","_")

            src="earthquakes.xlsx"
            dst="media/"+str(now)+"-earthquakes.xlsx"
            shutil.copy(src,dst)
            model = EarthquakeXLSX()
            model.xlsx_file = str(now)+"-earthquakes.xlsx"
            model.save()
            serializer = EarthquakeXLSXSerializer(model)
            return Response({"file": serializer.data})  
        except Exception as e:
            return Response({"erro": str(e)})