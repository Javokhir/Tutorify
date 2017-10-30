from django.conf.urls import url
from django.conf.urls.static import static

from Tutorify import settings
from .views import authenticate_tutor, authenticate_learner, sms_confirmation, tutor_list, tutor_by_subject, subject_list
from .views import create_announcement, course_list, announcement_list, create_course, course_by_subject


urlpatterns = [
    url(r'^authenticate-tutor/$', authenticate_tutor, name='authenticate_tutor'),
    url(r'^authenticate-learner/$', authenticate_learner, name='authenticate_learner'),
    url(r'^sms-confirmation/$', sms_confirmation, name='sms_confirmation'),
    url(r'^tutor-list/$', tutor_list),
    url(r'^tutor-list/(?P<subject_id>[0-9]+)/$', tutor_by_subject),
    url(r'^subject-list/$', subject_list),
    url(r'^create-announcement/$', create_announcement),
    url(r'^announcement-list/$', announcement_list),
    url(r'^create-course/$', create_course),
    url(r'^course-list/$', course_list),
    url(r'^course-list/(?P<subject_id>[0-9]+)/$', course_by_subject),
#    url(r'^course-list/(?P<tutor_id>[0-9]+)/$', course_by_tutor),


]
