from rest_framework import serializers
from . import models


class billSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Bill
        fields = '__all__'
