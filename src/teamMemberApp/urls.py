from django.contrib import admin
from django.urls import path, include

#from teamMember.views import list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teamMember.urls')),
]
