# Create your views here.
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
)
from drf_spectacular.utils import extend_schema_view
from rest_framework import parsers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication


# from apps.core.authentication import AuthenticationBackend

from apps.core.models import tr_get3BData, tr_gstr2b_itcsumm
from apps.core.serializers import Tr_get3BData_data, Tr_gstr2b_itcsumm


@extend_schema(
    tags=["GST table Data"],
    auth=[{}],
    request=Tr_gstr2b_itcsumm,
    summary="tr_gstr2b_itcsumm Data",
    responses={
        200: OpenApiResponse(description="OK"),
        400: OpenApiResponse(description="Bad Request"),
        401: OpenApiResponse(description="Unauthorized User"),
        500: OpenApiResponse(description="Internal Server Error"),
    }
)
class Tr_gstr2b_itcsummView(GenericAPIView):
    queryset = tr_gstr2b_itcsumm.objects.all()
    serializer_class = Tr_gstr2b_itcsumm

    def get(self, *args, **kwargs):
        qs = tr_gstr2b_itcsumm.objects.all()
        serializer = Tr_gstr2b_itcsumm(qs, many=True)
        serializer_data = serializer.data

        return Response({"status": "success", "data": serializer_data}, status=status.HTTP_200_OK)




@extend_schema(
    tags=["GST table Data"],
    auth=[{}],
    request=Tr_get3BData_data,
    summary="tr_get3BData Data",
    responses={
        200: OpenApiResponse(description="OK"),
        400: OpenApiResponse(description="Bad Request"),
        401: OpenApiResponse(description="Unauthorized User"),
        500: OpenApiResponse(description="Internal Server Error"),
    }
)
class Tr_get3BData_dataView(GenericAPIView):
    queryset = tr_get3BData.objects.all()
    serializer_class = Tr_get3BData_data

    def get(self, *args, **kwargs):
        qs = tr_get3BData.objects.all()
        serializer = Tr_get3BData_data(qs, many=True)
        serializer_data = serializer.data

        return Response({"status": "success", "data": serializer_data}, status=status.HTTP_200_OK)





@extend_schema(
    tags=["Filter Data"],
    auth=[{}],
    request=Tr_gstr2b_itcsumm,
    summary="tr_gstr2b_itcsumm filter Data",
    responses={
        200: OpenApiResponse(description="OK"),
        400: OpenApiResponse(description="Bad Request"),
        401: OpenApiResponse(description="Unauthorized User"),
        500: OpenApiResponse(description="Internal Server Error"),
    }
)
class Tr_gstr2b_itcsumm_FilterView(GenericAPIView):
    queryset = tr_gstr2b_itcsumm.objects.all()
    serializer_class = Tr_gstr2b_itcsumm

    def get(self, *args, **kwargs):
        qs = tr_gstr2b_itcsumm.objects.filter(invoice_category__isnull=True,  summ_type = 'itcavl', 
            supply_type = 'nonrevsup', gstin = '27GSPTN5151G1ZU', fp = '01-2021')
        serializer = Tr_gstr2b_itcsumm(qs, many=True)
        serializer_data = serializer.data


        qs2 = tr_gstr2b_itcsumm.objects.filter(invoice_category__isnull=False,  summ_type = 'itcavl', 
            supply_type = 'nonrevsup', gstin = '27GSPTN5151G1ZU', fp = '01-2021')
        serializer2 = Tr_gstr2b_itcsumm(qs2, many=True)
        serializer_data2 = serializer2.data



        tr_cess_sum = sum(item['tr_cess'] for item in serializer_data2)
        tr_sgst_sum = sum(item['tr_sgst'] for item in serializer_data2)
        tr_cgst_sum = sum(item['tr_cgst'] for item in serializer_data2)
        tr_igst_sum = sum(item['tr_igst'] for item in serializer_data2)
        for sum_data in serializer_data:
            if sum_data["summary_cess"] == tr_cess_sum and sum_data["summary_sgst"] == tr_sgst_sum and sum_data["summary_cgst"] == tr_cgst_sum and sum_data["summary_igst"] == tr_igst_sum:
            #     return Response({"status": "success"}, status=status.HTTP_200_OK)
            # else:
                # sum_data.update ({
                #     'tr_cess': tr_cess_sum,
                #     'tr_sgst': tr_sgst_sum,
                #     'tr_cgst': tr_cgst_sum,
                #     'tr_igst': tr_igst_sum
                # })

                r_data= sum_data["TableName3B"]
                
                sample_str = r_data[0:1] + '.' + r_data[1+1:]
                strObj = sample_str[0 : 3 : ] + sample_str[3 + 1 : :]

        qs_3b = tr_get3BData.objects.filter(GSTIN = '27GSPTN5151G1ZU', FP = '01-2021', Three_BTable = strObj)
        serializer_3b = Tr_get3BData_data(qs_3b, many=True)
        serializer_data_3b = serializer_3b.data
        for matching_data in serializer_data_3b:
            if matching_data["IGSTAmount"] == tr_igst_sum and matching_data["CGSTAmount"] == tr_cgst_sum and matching_data["SGSTAmount"] == tr_sgst_sum and matching_data["CESSAmount"] == tr_cess_sum:
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            else:
                data3 = matching_data | {
                    'tr_cess': tr_cess_sum,
                    'tr_sgst': tr_sgst_sum,
                    'tr_cgst': tr_cgst_sum,
                    'tr_igst': tr_igst_sum
                }
                return Response({"status": "success", "data": data3}, status=status.HTTP_200_OK)