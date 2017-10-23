from random import random

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tutor, Organization, Learner


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        # certificate = Base64ImageField()
        # photo = Base64ImageField()
        model = Tutor
        fields = ('name', 'email', 'country_code', 'phone_number', 'about', 'certificate', 'photo', 'subject', 'address', 'type')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = ('name', 'email', 'phone_number', 'photo')

