from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, handler404
from tablets import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tablet_list, name='home'),
    url(r'^tablets/', include('tablets.urls')),
    url(r'^accounts/', include('accounts.urls')),
    path('brands/', views.brand_list, name='brand_list'),
    path('brand_create/', views.brand_create, name='brand_create'),

]

urlpatterns += staticfiles_urlpatterns()

handler404 = views.error_404

