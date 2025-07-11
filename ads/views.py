from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters
from .models import Ad, ExchangeProposal
from .serializers import AdSerializer, ExchangeProposalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        # Можно добавить фильтры по категориям и состоянию
        category = self.request.query_params.get('category')
        condition = self.request.query_params.get('condition')
        if category:
            queryset = queryset.filter(category=category)
        if condition:
            queryset = queryset.filter(condition=condition)
        return queryset

class ExchangeProposalViewSet(viewsets.ModelViewSet):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ad_sender__title', 'ad_receiver__title', 'status']

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        proposal = self.get_object()
        status = request.data.get('status')
        if status in dict(ExchangeProposal.STATUS_CHOICES):
            proposal.status = status
            proposal.save()
            return Response({'status': 'updated'})
        return Response({'error': 'Invalid status'}, status=400)

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})
