from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            messages.add_message(request, messages.INFO, 'User registred successfully. WELCOME !', 'success')
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'Please try another username and password to register !', 'warning')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                messages.add_message(request, messages.INFO, 'User loged in successfully.', 'success')
                return redirect('home')
        else :   
            messages.add_message(request, messages.INFO, 'Usename or/and password are wrong. Please try again.', 'warning')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
        logout(request)
        messages.add_message(request, messages.INFO, 'User loged out successfully.', 'success')
        return redirect('home')