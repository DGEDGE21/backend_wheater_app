from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.mail import send_mail
from .models import *
from .serializers import *
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
import  string,random
from  time import *


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializado

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)

        return Response({'token': token})

class Criar_Conta(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        info = self.request.data
        nome = info['nome']
        mail = info['mail']
        password = info['password']
        adress=info['endereco']

        username = nome.replace(" ", "")
        username = username.lower()

        try:
            serializer = self.get_serializer(
                data={"username": f"{username}", "password": f"{password}", "email": f"anisio2000@gmail.com"})
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        except:
            serializer = self.get_serializer(data={
                "username": f"{username}{localtime().tm_year}{localtime().tm_mon}{localtime().tm_mday}{localtime().tm_hour}{localtime().tm_min}{localtime().tm_sec}",
                "password": f"{password}", "email": f"anisio2000@gmail.com"})
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        user_id = serializer.data
        user_id = user_id['id']

        ss = EmailMessage('Bem vindo ao Portal',
                          "Para aceder ao Portal use as seguintes credencias\n"
                          f"\nusuario:{username}\n"
                          f"\npassword:{password}\n",
                          to=[mail])

        ss.send()

        n = Usuario.objects.create(
            nome=nome,
            email=mail,
        morada =adress,


        user=user

        )
        n.save()
        return Response(data={"username": username, "password": password})


class Exchange_Rates_population_GPD(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        import requests
        import  json
        Exchange_URL = "http://api.exchangeratesapi.io/v1"
        Exchange_API_KEY = "3c9219ff47b72b84f87522174bbc1e15"
        url = f"{Exchange_URL}/latest?access_key={Exchange_API_KEY}&symbols={self.request.data['moeda']}"
        WDBAPI_url = f"http://api.worldbank.org/v2/countries/{self.request.data['citycode']}/indicators/SP.POP.TOTL?format=json"
        WDBAPI_url_GPD = f"http://api.worldbank.org/v2/countries/{self.request.data['citycode']}/indicators/NY.GDP.PCAP.CD?format=json"

        try:
            response = requests.get(url)
            respone_data = response.json()
            if response.status_code == 200:
                info=respone_data
                dados=dict()
                dados.update(info)
                d=str(info['rates']).replace("{", "").replace("}", "").replace("'","").replace("'","")
                dados.update({"rates":f"{d}"})


            response = requests.get(WDBAPI_url)
            data = response.json()
            if len(data) > 1:
                population_data = [entry for entry in data[1] if entry['value'] is not None]
                if population_data:
                       dados.update({"population":population_data[0]['value']})
                       print(population_data[0]['value'])
            response = requests.get(WDBAPI_url_GPD)
            data = response.json()

            if len(data) > 1:
                gdp_per_capita_data = [entry for entry in data[1] if entry['value'] is not None]
                if gdp_per_capita_data:
                    dados.update({"gpd":gdp_per_capita_data[0]['value']})



        except requests.exceptions.RequestException as e:
            print('Error fetching data:', e)

        return  Response(dados)




