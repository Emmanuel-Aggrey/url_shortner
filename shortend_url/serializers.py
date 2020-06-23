from rest_framework import  serializers
from .models import  Link

class LinkSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Link
        fields = ['id','shortened_url','original_url']
        

class ShortToLongUrlSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Link
        fields = ['shortened_url','original_url']
        