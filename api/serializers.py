from rest_framework import serializers
from  .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields=('category','from_items','title','text','thedate', 'id_items')