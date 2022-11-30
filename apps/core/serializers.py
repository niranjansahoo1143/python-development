
from rest_framework import serializers

from .models import tr_get3BData, tr_gstr2b_itcsumm

class Tr_get3BData_data(serializers.ModelSerializer):
    class Meta:
        model = tr_get3BData
        fields = '__all__'


class Tr_gstr2b_itcsumm(serializers.ModelSerializer):
    class Meta:
        model = tr_gstr2b_itcsumm
        fields = '__all__'


