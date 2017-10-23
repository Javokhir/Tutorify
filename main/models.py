from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from rest_framework.authtoken.models import Token


class Subject(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    country_code = models.CharField(max_length=4, default='+82')
    phone_number = PhoneNumberField(unique=True)
    about = models.TextField(max_length=1000)
    certificate = models.CharField(blank=True, max_length=200)
    photo = models.CharField(blank=True, max_length=200)
    subject = models.ForeignKey(Subject, related_name='subjects')
    address = models.TextField(max_length=500)
    type = models.CharField(max_length=100)
    token = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_it_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name', 'email', 'phone_number']

    #create_course = models.ManyToManyField(Course, on_delete=models.CASCADE)
    #create_announcement = models.ManyToManyField(Announcement, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Tutor)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Organization(models.Model):
    tutor = models.ForeignKey(Tutor, related_name='tutor_in_organization')
    type = models.CharField(max_length=100)
    size = models.PositiveIntegerField(null=True, blank=True, default=0)
    has_branch = models.CharField(max_length=200)

    class Meta:
        ordering = ('has_branch',)

    def __str__(self):
        return self.has_branch


class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='courses_created')
    level = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutor, related_name='tutor_in_courses')
    description = models.TextField(max_length=1000)
    price = models.FloatField(null=True, blank=True, default=0)
    location = models.TextField(max_length=200)
    contact = models.TextField(max_length=1000)
    number_of_students = models.PositiveIntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ('subject',)

    def __str__(self):
        return self.subject


class Announcement(models.Model):
    subject = models.ForeignKey(Subject, related_name='announcements_created')
    tutor = models.ForeignKey(Tutor, related_name='tutor_in_announcement')
    description = models.TextField(max_length=1000)
    schedule = models.TextField(max_length=1000)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('subject',)

    def __str__(self):
        return self.subject


class Learner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone_number = PhoneNumberField(unique=True)
    photo = models.CharField(max_length=200)
    fav_announcement = models.ManyToManyField(Announcement, related_name='favorite_announcement')
    apply_course = models.ManyToManyField(Course, related_name='apply_course')
    fav_course = models.ManyToManyField(Course, related_name='fav_course')
    fav_tutor = models.ManyToManyField(Tutor, related_name='fav_tutor')
    pin = models.IntegerField(blank=False, default=0000)
    token = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_it_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

