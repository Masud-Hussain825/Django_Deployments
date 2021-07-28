from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('my_app1.urls')),
    path('login/', include('login_app.urls')),
    path('classView/', include('classBasedView.urls')),
]
