from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ads', views.AdViewSet)
router.register(r'proposals', views.ExchangeProposalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('ad/create/', views.ad_create, name='ad_create'),
]
