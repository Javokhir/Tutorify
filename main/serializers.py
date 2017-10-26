from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Tutor, Organization, Learner, Sms, Course, Subject, Announcement

User = get_user_model()


class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ('username', 'email', 'country_code', 'phone_number', 'about', 'certificate', 'photo',
                  'subject_name', 'address', 'type')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization


class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = ('username', 'email', 'country_code', 'phone_number', 'photo')


class SmsVerifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Sms
        fields = ('country_code', 'phone_number', 'verification_code')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('subject_name', 'category', 'description')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('subject_name', 'level', 'username', 'description', 'price', 'location', 'contact',
                  'number_of_students')


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ('subject_name', 'username', 'description', 'schedule')



