from rest_framework import serializers
from client.models import user_detail
 
class user_detail_Serializer(serializers.ModelSerializer):
 
    class Meta:
        model = user_detail
        fields = "__all__"