from django.conf.urls import url
from django.urls import path
from login_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static , staticfiles_urlpatterns

app_name = "login_app"

urlpatterns = [
    path('', views.index_page, name='LoginPage'),
    path('register/', views.register, name='Register'),
    path('userLogin/', views.user_login, name='UserLogin'),
    path('logout/', views.user_logout, name='Logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)