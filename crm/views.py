from rest_framework import generics
from rest_framework import filters
from .models import Customer, Company, Interaction
from .serializers import CustomerSerializer, CompanySerializer, InteractionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Subquery, OuterRef, Max, Prefetch
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination

class InteractionPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'company__name', 'birth_date', 'last_interaction_date']
    filterset_fields = {
        'birth_date': ['range', 'exact', 'year', 'month', 'day'],
    }


    def get_queryset(self):
        last_interaction = Interaction.objects.filter(
            customer=OuterRef('pk')
        ).order_by('-interaction_date')

        return Customer.objects.all().annotate(
            last_interaction_date=Subquery(last_interaction.values('interaction_date')[:1]),
            last_interaction_type=Subquery(last_interaction.values('interaction_type')[:1])
        ).select_related('company', 'sales_representative')
    

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class InteractionListView(generics.ListAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    pagination_class = InteractionPagination
