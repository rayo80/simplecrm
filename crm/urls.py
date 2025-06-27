from django.urls import path
from .views import CustomerListView, CompanyListView, InteractionListView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('interactions/', InteractionListView.as_view(), name='interaction-list'),
]
