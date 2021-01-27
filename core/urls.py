from django.urls import path

from core.views import BunnyView, CreateBunnyView, UpdateBunnyView, BreedingFarmView, CreateBreedingFarmView, \
    UpdateBreedingFarmView
from rest_framework.authtoken import views as rest_framework_views

app_name = 'bunny'

urlpatterns = [
    path('bunny/', BunnyView.as_view(), name='bunny'),
    path('bunny/get_auth_token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('bunny/create/', CreateBunnyView.as_view(), name='create-bunny'),
    path('bunny/update/', UpdateBunnyView.as_view(), name='update-bunny'),
    path('breeding_farm/', BreedingFarmView.as_view(), name='breeding-farm'),
    path('breeding_farm/create/', CreateBreedingFarmView.as_view(), name='breeding-farm-create'),
    path('breeding_farm/update/', UpdateBreedingFarmView.as_view(), name='breeding-farm-create')
]
