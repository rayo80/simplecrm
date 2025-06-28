from rest_framework import serializers
from .models import Customer, Company, Interaction

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    last_interaction = serializers.SerializerMethodField()
    birthday_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    def get_last_interaction(self, obj):
        if obj.last_interaction_date and obj.last_interaction_type:
            return {
                'type': obj.last_interaction_type,
                'date': obj.last_interaction_date
            }
        return None
    
    def get_birthday_formatted(self, obj):
        return obj.birth_date.strftime("%B %d")

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'
