import pandas as pd
import requests

class TypesConversions:
    
    def __init__(self):
        self.url = 'https://www.cbinsights.com/research-unicorn-companies/'
        self.ruta = r'C:/Users/ovsantiago/Desktop/py/web/web.xlsx'
    
    def csv_archive(self):
        table = pd.read_html(requests.get(self.url).text,flavor="bs4",decimal=",",thousands='.')
        return table[0].to_csv("archivo.csv")

    def xlsx_archive(self):
        archive = pd.ExcelWriter(self.ruta)
        table = pd.read_html(requests.get(self.url).text,flavor="bs4",decimal=",",thousands='.')    
        table[0].to_excel(archive,'Hoja1', index=False)
        return archive.save()
    
    def json_archive(self):
        table = pd.read_html(requests.get(self.url).text,flavor="bs4",decimal=",",thousands='.')
        return table[0].to_json("archivo.json")

Con = TypesConversions()
Con.csv_archive()
Con.xlsx_archive()
Con.json_archive()
