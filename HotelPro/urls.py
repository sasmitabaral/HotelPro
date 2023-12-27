from django.contrib import admin
from django.urls import path,include
#from django.apps import hotel


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hotel.urls'))
]
