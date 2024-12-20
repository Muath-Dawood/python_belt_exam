from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('my_auth.urls')),
    path('', include('pies.urls'))
]
