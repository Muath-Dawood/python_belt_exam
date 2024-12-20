from django.urls import path
from .views import dashboard, list_pies, show_pie, edit_pie, delete_pie

urlpatterns = [
    path('dashboard/', dashboard, name='pies_dashboard'),
    path('pies/',list_pies, name='pies_list_pies'),
    path('pies/<int:id>/', show_pie, name='pies_show_pie'),
    path('pies/edit/<int:id>/', edit_pie, name='pies_edit_pie'),
    path('pies/delete/<int:id>/', delete_pie, name='pies_delete_pie'),
]
