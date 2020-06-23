from rest_framework import  serializers
from .models import  Link

class LinkSerializers(serializers.ModelSerializer):
    # shortened_url = serializers.URLField(source='short_url')
    class Meta:
        model = Link
        fields = ['id','shortened_url','original_url']
        

