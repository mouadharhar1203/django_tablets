from django.shortcuts import render, redirect
from .models import Tablet, Brand
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse

def tablet_list(request):
    new_tablets = Tablet.objects.filter(release_year__gte=2015).order_by('release_year').reverse()
    old_tablets = Tablet.objects.filter(release_year__lt=2015).order_by('release_year').reverse()
    return render(request, 'tablets/tablet_list.html', { 'newTablets': new_tablets, 'oldTablts':old_tablets })

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'tablets/brand_list.html', { 'brands': brands })

def tablet_detail(request, pk):
    tablet = Tablet.objects.get(id=pk)
    return render(request, 'tablets/tablet_detail.html', { 'tablet': tablet })

@login_required(login_url="/accounts/login/")
def delete_tablet(request, pk):
    try:
        tablet = Tablet.objects.get(id=pk)
        tablet.delete()
        messages.add_message(request, messages.INFO, 'Tablet deleted successfully !', 'success')
    except:
        messages.add_message(request, messages.INFO, 'Tablet not deleted !', 'warning')
    return tablet_list(request)

@login_required(login_url="/accounts/login/")
def tablet_create(request):
    if request.method == 'POST':
        form = forms.CreateTablet(request.POST, request.FILES)
        if form.is_valid():
            # save tablet to db
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, 'Tablet created successfully !', 'success')
            return redirect('home')
        else :
            messages.add_message(request, messages.INFO, 'Tablet not created, please correct the informations !', 'warning')
    else:
        form = forms.CreateTablet()
    return render(request, 'tablets/tablet_create.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def tablet_update(request, pk, template_name='tablets/tablet_update.html'):
    try:
        tablet = get_object_or_404(Tablet, pk=pk)
        form = forms.CreateTablet(request.POST or None, instance=tablet)
        if request.POST and form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Brand updated successfully !', 'success')
            return redirect('home')

        return render(request, template_name, {
            'form': form, 'tablet':tablet
        })
    except :
        messages.add_message(request, messages.INFO, 'Something went wrong, please try again !', 'warning')
        return redirect('home')

@login_required(login_url="/accounts/login/")
def brand_create(request):
    if request.method == 'POST':
        form = forms.CreateBrand(request.POST, request.FILES)
        if form.is_valid():
            # save tablet to db
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, 'Brand created successfully !', 'success')
            return redirect('home')
        else :
            messages.add_message(request, messages.INFO, 'Brand not created, please correct the informations !', 'warning')
    else:
        form = forms.CreateBrand()
    return render(request, 'tablets/brand_create.html', { 'form': form })

def error_404(request, exception):
    return render(request, 'tablets/404.html')