from typing import List
from django.urls import path

from .views import ListMembersView, AddView, EditView, DeleteMemberView

urlpatterns = [
    #path('', views.list, name="list"),
    path('', ListMembersView.as_view(), name='list'),
    path('add/', AddView.as_view(), name='add'),
    path('edit/<slug:pk>', EditView.as_view(), name='edit'),
    path('delete/<slug:pk>', DeleteMemberView.as_view(), name='delete'),
]
 