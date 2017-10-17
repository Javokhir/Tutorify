from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


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
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    about = models.TextField(max_length=1000)
    certificate = models.FileField(upload_to='images')
    photo = models.FileField(upload_to='images')
    subject = models.ForeignKey(Subject, related_name='subjects')
    address = models.TextField(max_length=500)
    type = models.CharField(max_length=100)
    #create_course = models.ManyToManyField(Course, on_delete=models.CASCADE)
    #create_announcement = models.ManyToManyField(Announcement, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


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
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    photo = models.FileField(upload_to='images')
    fav_announcement = models.ManyToManyField(Announcement, related_name='favorite_announcement')
    apply_course = models.ManyToManyField(Course, related_name='apply_course')
    fav_course = models.ManyToManyField(Course, related_name='fav_course')
    fav_tutor = models.ManyToManyField(Tutor, related_name='fav_tutor')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

