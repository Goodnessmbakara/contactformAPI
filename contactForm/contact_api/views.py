from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.core.mail import send_mail
from . serializers import EmailSerializer

class SendEmailAPI(APIView):
    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            recipient_email = serializer.validated_data['recipient_email']
            send_mail(subject, message, 'activation.django@gmail.com', [recipient_email], fail_silently=False)
            return Response({"message": "Email sent successfully."})
        return Response(serializer.errors, status=400)
