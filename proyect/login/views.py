from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from login.models import Usuarios
# Create your views here.

TEMPLATE_DIRS =(
    'os.patch.join(BASE_DIR, "templates")'
)

 
def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def buscar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users}
    return render(request,'buscar.html', datos)

def registrar(request):
    if request.method =='POST':
       if request.POST.get('nombres') and request.POST.get('apellidos')and request.POST.get('idname')and request.POST.get('numcon')and request.POST.get('cargo')and request.POST.get('telefono'):
        user = Usuarios()
        user.nombres = request.POST.get('nombres')
        user.apellidos = request.POST.get('apellidos')
        user.idname = request.POST.get('idname')
        user.numcon = request.POST.get('numcon')
        user.cargo = request.POST.get('cargo')
        user.telefono = request.POST.get('telefono')
        user.save()
        return redirect('buscar.html') 
    
     
    else:
         return render(request,'registra.html')


def editar(request):
    return render(request,'editar_contrato.html')

def eliminar(request):
    return render(request,'eliminar_contrato.html')

def cargar(request):
    return render(request,'cargar_contrato.html')

def actualizar(request):
    return render(request,'actualizar_contrato.html')




