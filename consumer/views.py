from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest

# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):

    return render(request, 'consumer/index.html')




def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")


    context = {'registerform':form}

    return render(request, 'consumer/register.html', context=context)


# def submit_service_request(request):
#     if request.method == 'POST':
#         form = ServiceRequestForm(request.POST)
#         if form.is_valid():
#             service_request = form.save(commit=False)
#             service_request.user = request.user
#             service_request.save()
#             return redirect('dashboard')
#     else:
#         form = ServiceRequestForm()
#     return render(request, 'consumer/submit_service_request.html', {'form': form})



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'consumer/my-login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("")



@login_required(login_url="my-login")
def dashboard(request):
    user = request.user
    service_requests = ServiceRequest.objects.filter(user=user)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = user
            service_request.save()
            # After saving the service request, redirect to the dashboard
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()

    return render(request, 'consumer/dashboard.html', {'user': user, 'service_requests': service_requests, 'form': form})







