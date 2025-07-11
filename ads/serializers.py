from rest_framework import serializers
from .models import Ad, ExchangeProposal

class AdSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ad
        fields = ['id', 'user', 'title', 'description', 'image_url', 'category', 'condition', 'created_at']

class ExchangeProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeProposal
        fields = ['id', 'ad_sender', 'ad_receiver', 'comment', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
