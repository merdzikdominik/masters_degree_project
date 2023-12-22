from django.urls import path
from .views import AnnualView

urlpatterns = [
    path('', AnnualView.as_view())
]
