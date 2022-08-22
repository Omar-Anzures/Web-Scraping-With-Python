#importamos las librerias que vamos a utilizar
import pandas as pd
import requests

#se crea la clase 
class TypesConversions:
    
    #metodo para los atributos que se comparten
    def __init__(self):
        self.url = 'https://www.cbinsights.com/research-unicorn-companies/'
        self.ruta = r'/ruta-a-guardar/nombre-archivo.xlsx'
        self.table = pd.read_html(requests.get(self.url).text,flavor="bs4",decimal=",",thousands='.')
    
    #metodo para exportar a csv 
    def csv_archive(self):
        return self.table[0].to_csv("archivo.csv")

    #metodo para exportar a xlsx 
    def xlsx_archive(self):
        archive = pd.ExcelWriter(self.ruta)   
        self.table[0].to_excel(archive,'Hoja1', index=False)
        return archive.save()
    
    #metodo para exportar a json
    def json_archive(self):
        return self.table[0].to_json("archivo.json")

#se crean el objeto convert a partir de la clase
Conver = TypesConversions()

#a partir del objeto creado mandamos a llamar al tipo de archivo que deseemos exportar
Conver.csv_archive()
Conver.xlsx_archive()
Conver.json_archive()
