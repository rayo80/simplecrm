from rest_framework import generics
from rest_framework import filters
from .models import Customer, Company, Interaction
from .serializers import CustomerSerializer, CompanySerializer, InteractionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Subquery, OuterRef, Max
from django.shortcuts import render
from django.http import HttpResponse

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'company__name', 'birth_date', 'last_interaction_date']

    def get_queryset(self):
        # Get the last interaction date for each customer
        last_interaction_date = Interaction.objects.filter(customer=OuterRef('pk')).order_by('-interaction_date').values('interaction_date')[:1]

        queryset = Customer.objects.all().annotate(last_interaction_date=Subquery(last_interaction_date))
        return queryset
    filterset_fields = {
        'birth_date': ['range', 'exact', 'year', 'month', 'day'],
    }
    #def get(self, request, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = self.get_serializer(queryset, many=True)
    #    return HttpResponse(serializer.data)

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    #def get(self, request, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = self.get_serializer(queryset, many=True)
    #    return HttpResponse(serializer.data)

class InteractionListView(generics.ListAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    #def get(self, request, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = self.get_serializer(queryset, many=True)
    #    return HttpResponse(serializer.data)
