from rest_framework import serializers
from Items.models import Itemlist, Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Itemlist
        fields=('SKU','Name','Tags','category','In_stock','Available_stock')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'