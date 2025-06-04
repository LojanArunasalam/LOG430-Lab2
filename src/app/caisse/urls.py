from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("report/", views.sales_report, name="report"),
    path("products/", views.search_products, name="products"),
    path("dashboard/", views.dashboard_logistique, name="dashboard")
]