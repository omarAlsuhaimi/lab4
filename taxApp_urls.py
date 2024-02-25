from django.urls import path
from .  import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("<int:number>/",views.taxCal,name = "taxCalculation"),
    path("<rate>/",views.display_tax,name = "displaytax")
]