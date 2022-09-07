from django import forms
from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Article,Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages
# Create your views here.

def index(request):
    
    html = []
    year = 2000
    while year<=2040:
        if year%4 == 0:
            if year%100!=0:
                html.append(year)
            else:
                if year%400 == 0:
                    html.append(year)
        year+=1
    
    nombre = 'Juan Jose'
    lenguajes = [
        "Python",
        "Css",
        "PHP",
        "C",
        "Putas"
    ]

    lista2 = range(2020,2051,1)
    return render(request,'index.html',{
        'title':'Inicio',
        'mi_variable':'Soy un dato k esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'lista':html,
        'par':lista2
    })


def hola_mundo(request):
    return render(request,'hola_mundo.html ')

def pagina(request,redirigir=0):
    if redirigir==1:
        return redirect('Contacto',nombre = "Juan Jose",apellidos="Martinez")
    
    return render(request,'pagina.html',{
        'texto':'',
        'listax':["loca",1,2,4]
    })

def contacto(request,nombre="",apellidos=""):
    html = ""
    
    if nombre and apellidos:
        html+=f"{nombre} {apellidos} puedes"
    elif nombre:
        html+=f"{nombre} puedes"
    else:
        html = "Puedes"
    return render(request,'contacto.html')

def crear_articulo(request,title,content,public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):
    if request.method == 'POST':
        
        articulo = Article(
            title = request.POST['title'],
            content = request.POST['content'],
            public = request.POST['public']
        )
        articulo.save()

        return HttpResponse(f"Articulo creado <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse(f"<h2>No se ha podido crear el articulo</h2>")
   

def create_article(request):

    return render(request,'create_article.html')


def create_full_article(request):

    if request.method =='POST':
        
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form['title']
            content = data_form['content'] 
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
                )

            articulo.save()

            messages.success(request,'Has creado correctamente el articulo')

            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request,'create_full_article.html',{
        'formulario':formulario
    })


def articulo(request):
    try:
        articulo = Article.objects.get(title='superman',public=True)
        return HttpResponse(f"Articulo: {articulo.content}")
    except:
        return HttpResponse("<h2>No se encuentra el articulo</h2>")
    
def edita_articulo(request,id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "I like to suck pussys"
    articulo.public = True
    articulo.save() 

    return HttpResponse(f"<p>Articulo {articulo.id} actualizado</p>")

def articulos(request):
    
    articulos = Article.objects.filter(public=True)

    """articulos = Article.objects.filter(id__lte=11,title__contains="2")

    articulos = Article.objects.filter(
        title__iexact="articulo",
       
    ).exclude(
        public = False
    )

    articulos = Article.objects.raw("Select * from miapp_article where title='Articulo2' and public=1")
    
    articulos = Article.objects.filter(
        Q(title__contains="2") |   Q(public=True)   )"""
    
    return render(request,'articulos.html',{
        'articulos':articulos
    })

def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
