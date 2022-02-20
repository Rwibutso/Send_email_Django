from django.urls import path
from .views import NumberView, NumberSuccessView

app_name = 'number'

urlpatterns = [
    path('', NumberView.as_view(), name="number"),
    path('success/', NumberSuccessView.as_view(), name="success"),
]