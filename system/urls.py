from django.urls import path
from .views import ProductMaterialRequestView

urlpatterns = [
    path('materials/', ProductMaterialRequestView.as_view(), name='request-materials'),
]