from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from .forms import NuestroUserForm, NuestraEdicionUser
from .models import Avatar

def inicio (request):
    return render (request, 'accounts/index.html')

def mi_login(request):
    
    if request.method == 'POST':
        login_form = AuthenticationForm (request, data = request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password = password)

            if user is not None:
                login (request,user)
                return redirect('inicio')
            else:
                return render(request,'accounts/login.html', {'login_form': login_form, 'msj': 'El usuario no se pudo autenticar.'} )
        else:
            return render(request,'accounts/login.html', {'login_form': login_form, 'msj': 'Ha ocurrido un error al iniciar sesión. Verifique los datos e intente nuevamente.' } )


    login_form = AuthenticationForm()
    return render (request, 'accounts/login.html', {'login_form': login_form})


def signup(request):
    if request.method == 'POST':
        form = NuestroUserForm(request.POST)

        if form.is_valid():
            form.cleaned_data['username']
            form.save()
            return redirect('login')
        else:
            return render(request,'accounts/signup.html', {'form': form, 'msj': 'Ha ocurrido un error durante el registro.'} )


    form = NuestroUserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def editar (request): 

    if request.method =='POST':
        form = NuestraEdicionUser (request.POST)

        if form.is_valid():
            
            data = form.cleaned_data

            request.user.email = data.get('email', '')
            request.user.first_name = data.get('first_name', '')
            request.user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) >8:
                request.user.set_password(data.get('password1'))
                msj = 'Se modificó el password.'
            else:
                msj = 'No se modificó el password.'

            request.user.save()

            return render(request, 'accounts/index.html', {'msj': msj})
        else:
            return render(request, 'accounts/edit_user.html', {'form': form, 'msj':''})

    form = NuestraEdicionUser(initial= {'first_name': request.user.first_name,
    'last_name': request.user.last_name,    'email':request.user.email, 'username':request.user.username })
    return render (request, 'accounts/edit_user.html', {'form': form, 'msj': ''})

#def buscar_url_avatar(user):
    #return Avatar.objects.filter(user=user)[0].imagen.url