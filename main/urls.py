from django.conf.urls import url
from .views import authenticate_tutor, authenticate_learner

urlpatterns = [
    url(r'^authenticate-tutor/$', authenticate_tutor, name='authenticate_tutor'),
    url(r'^authenticate-learner/$', authenticate_learner, name='authenticate_learner'),
]
