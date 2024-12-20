from django.urls import path

urlpatterns = [
    path('dashboard/', name='dashboard'),
    path('pies/', name='list_pies'),
    path('pies/<int:id>/', name='show_pie'),
    path('pies/edit/<int:id/', name='edit_pie'),
    path('pies/delete/<int:id/', name='delete_pie'),
]
