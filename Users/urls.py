from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import registro,profile,logoutView,edit_profile,change_password
from django.conf.urls import include, url
from WebApp.views import home
from django.conf import settings
from django.conf.urls.static import static

app_name='AppUsers'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('registro/', registro, name='registro'),
  path('profile/', profile, name='profile'),
  path('edit_profile/', edit_profile, name='edit_profile'),
  url(r'^logout/$', logoutView, name='logout'),
  url(r'^change-password/$', change_password, name='change_password')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)