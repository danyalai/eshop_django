from django.urls import path
from . import views
urlpatterns = {
    path('', views.eshop_app),
    path('<slug>', views.my_slug),
}
