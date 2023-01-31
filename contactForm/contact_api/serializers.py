from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
    recipient_email = serializers.EmailField(default='activation.django@gmail.com')
