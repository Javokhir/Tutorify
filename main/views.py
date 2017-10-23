import random

from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from twilio.rest import Client

import requests
from Tutorify import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from main.models import Organization, Learner, Tutor
from .serializers import TutorSerializer, OrganizationSerializer, LearnerSerializer

from authy.api import AuthyApiClient
authy_api = AuthyApiClient('qq6mSfaAJDXAPZ7kgOI2XImAQF1iBtjl')


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny, ))
@permission_classes((AllowAny, ))
def authenticate_tutor(request):

    if request.method == 'POST':
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            t = serializer.save()

            country_code = t.country_code
            phone_number = t.phone_number

            authy_api.phones.verification_start(phone_number, country_code, via='sms')

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny, ))
@permission_classes((AllowAny, ))
def authenticate_learner(request):

    if request.method == 'POST':
        serializer = LearnerSerializer(data=request.data)
        if serializer.is_valid():
            t = serializer.save()
            verification_code = random.randint(1111, 9999)
            t.pin = verification_code
            t.save()
            number = t.phone_number

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(
                body="Your tutorify activation code is %s" % verification_code,
                to=str(number),
                from_=settings.TWILIO_NUMBER
            )
    return Response(status=status.HTTP_200_OK)









