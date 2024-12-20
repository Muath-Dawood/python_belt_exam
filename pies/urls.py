from django.urls import path
from .views import index, dashboard, list_pies, add_pie, show_pie, edit_pie, delete_pie

urlpatterns = [
    path('', index, name='pies_index'),
    path('dashboard/', dashboard, name='pies_dashboard'),
    path('pies/',list_pies, name='pies_list_pies'),
    path('pies/add/', add_pie, name='pies_add_pie'),
    path('pies/<int:id>/', show_pie, name='pies_show_pie'),
    path('pies/edit/<int:id>/', edit_pie, name='pies_edit_pie'),
    path('pies/delete/<int:id>/', delete_pie, name='pies_delete_pie'),
]
