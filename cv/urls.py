from django.urls import path
from . import views

app_name = 'panier'

urlpatterns = [
    path('', views.cv_view, name='cv'),

]