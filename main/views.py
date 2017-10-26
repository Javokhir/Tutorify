from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from authy.api import AuthyApiClient

from main.models import Tutor, Subject, Announcement, Course

authy_api = AuthyApiClient('qq6mSfaAJDXAPZ7kgOI2XImAQF1iBtjl')

from .serializers import TutorSerializer, LearnerSerializer, SmsVerifySerializer
from .serializers import SubjectSerializer, AnnouncementSerializer, CourseSerializer


@api_view(['POST'])
@csrf_exempt
@permission_classes((AllowAny,))
@permission_classes((AllowAny,))
@parser_classes((MultiPartParser, FormParser, JSONParser))
def authenticate_tutor(request):
    if request.method == 'POST':
        serializer = TutorSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            tutor = serializer.save()

            phone_number = tutor.phone_number
            country_code = tutor.country_code

            authy_api.phones.verification_start(phone_number, country_code, via='sms')
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def authenticate_learner(request):
    if request.method == 'POST':
        serializer = LearnerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            t = serializer.save()

            country_code = t.country_code
            phone_number = t.phone_number

            authy_api.phones.verification_start(phone_number, country_code, via='sms')
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def sms_confirmation(request):
    if request.method == 'POST':
        serializer = SmsVerifySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            sms = serializer.save()

            country_code = sms.country_code
            phone_number = sms.phone_number
            verification_code = sms.verification_code

            ver = authy_api.phones.verification_check(phone_number, country_code, verification_code)

            if ver:
                Tutor.objects.update_or_create(phone_number=phone_number, defaults={'is_active': True,
                                                                                    'is_it_verified': True})

            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def tutor_list(request):
    tutors = Tutor.objects.all()
    serializer = TutorSerializer(tutors, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def tutor_by_subject(request, subject_id):
    tutors = Tutor.objects.filter(subject_name=subject_id).all()
    serializer = TutorSerializer(tutors, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def create_announcement(request):

    if request.method == 'POST':
        serializer = AnnouncementSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def create_course(request):

    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def announcement_list(request):

    announcements = Announcement.objects.all()
    serializer = AnnouncementSerializer(announcements, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def course_list(request):

    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
@authentication_classes((AllowAny,))
@permission_classes((AllowAny,))
def course_by_subject(request, subject_id):

    courses = Course.objects.filter(subject_name=subject_id).all()
    serializer = CourseSerializer(courses, many=True)

    return JsonResponse(serializer.data, safe=False)

#
# @api_view(['GET'])
# @csrf_exempt
# @authentication_classes((AllowAny,))
# @permission_classes((AllowAny,))
# def course_by_tutor(request, tutor_id):
#
#     courses = Course.objects.filter(username=tutor_id).all()
#     serializer = CourseSerializer(courses, many=True)
#
#     return JsonResponse(serializer.data, safe=False)








