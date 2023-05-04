from django.urls import path

from .views import IndexView, CurriculoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('curriculo/', CurriculoView.as_view(), name='curriculo'),
    
]
