from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Tr_get3BData_dataView, Tr_gstr2b_itcsummView, Tr_gstr2b_itcsumm_FilterView

router = DefaultRouter()

urlpatterns = [
    path('Tr_get3BData/', Tr_get3BData_dataView.as_view(), name="Tr_get3BData"),
    path('Tr_gstr2b_itcsumm/', Tr_gstr2b_itcsummView.as_view(), name="Tr_gstr2b_itcsumm"),
    path('Tr_gstr2b_itcsumm_FilterView/', Tr_gstr2b_itcsumm_FilterView.as_view(), name="Tr_gstr2b_itcsumm_FilterView")
    
] + router.urls

