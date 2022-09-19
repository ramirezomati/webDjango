from django.http import HttpResponse
from django.template import loader

def home(self, name):
    return HttpResponse(f'Hola soy {name}')

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9,10]
    data = {'nombre':'Matías', 'apellido':'Ramirez', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    planilla = loader.get_template('cursos.html')
    documento = planilla.render()
    return HttpResponse(documento)