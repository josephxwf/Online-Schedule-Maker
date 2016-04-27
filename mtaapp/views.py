from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
#from .models import Greeting
from django.contrib.auth.forms import UserCreationForm
from mtaapp.forms import LoginForm
from mtaapp.models import notification
from django.template.context_processors import csrf

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #user = request.user
    logout(request)  #logout the user first if the user is loggedin from django.contrib.auth import authenticate, login,logout
    return render(request, 'index.html',{'notifications': notification.objects.all()})


'''
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
'''
#def calendar(request):
#    return render(request, 'calendar.html')


def login_page(request):
    c = {}
    c.update(csrf(request))
    c['form'] = LoginForm()
    return render(request, 'login.html',c)

def nextQuarter(request):
    c = {}
    c.update(csrf(request))
    c['form'] = LoginForm()
    return render(request, 'loginSecond.html',c)


def invalid_login(request):
    return render(request, 'invalid_login.html')

#def loggedin(request):
#    return render(request, 'loggedin.html',{'full_name':request.user.username})

def logout_page(request):
    logout(request)  # logout the user first if the user is loggedin
    return HttpResponseRedirect('/')
'''
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_success.html')
    args ={}
    args.update(csrf(request))
    args['form'] = registerForm()
    return render(request, 'register.html',args)
'''

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #return HttpResponseRedirect('/account/loggedin')
            return render(request, 'calendar.html')
            # Redirect to a success page.
        else:
            return HttpResponse("disabled account")
            # Return a 'disabled account' error message

    else:
        return HttpResponseRedirect('/account/invalid_login')
        # Return an 'invalid login' error message.


def auth_viewSecond(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #return HttpResponseRedirect('/account/loggedin')
            return render(request, 'calendarSecond.html')
            # Redirect to a success page.
        else:
            return HttpResponse("disabled account")
            # Return a 'disabled account' error message

    else:
        return HttpResponseRedirect('/account/invalid_login')
        # Return an 'invalid login' error message.
