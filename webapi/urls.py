from .views import *
from django.urls import path,include
from knox import views as knox_views

urlpatterns = [

    path('web/login/',  LoginAPI.as_view(), name='login'),
    path('web/Registar_usuario/', Criar_Conta.as_view(), name='registar_usurio'),
    path('web/exchange_rates_population_gpd/',Exchange_Rates_population_GPD.as_view(),name="echange_rates"),

    ]