from django.shortcuts import render

# Create your views here.
def index (request):
   


    return render(request, 'index.html', {'autos' : autos})

class Auto:
    def __init__(self, nombre, precio, modelo, color):
        self.nombre = nombre
        self.precio = precio
        self.modelo = modelo
        self.color = color

autos = [
    Auto('VW Jetta', 145000, 2018, 'Gris'),
    Auto ('Lexus', 256000, 2017, "Rojo"),
    Auto ('Futura', 0, 1954, 'Agua'),
    Auto ('Porsche', 25000, 2010, 'Azul'),
]