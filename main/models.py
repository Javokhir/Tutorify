
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from .filename import RandomFileName


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ('subject_name',)

    def __str__(self):
        return self.subject_name


class Tutor(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    country_code = models.CharField(max_length=4)
    phone_number = models.CharField(unique=True, max_length=11)
    about = models.TextField(max_length=1000)
    certificate = models.ImageField(upload_to=RandomFileName('certificates'), blank=True, null=True)
    photo = models.ImageField(upload_to=RandomFileName('photos'), blank=True, null=True)
    subject_name = models.ForeignKey(Subject, related_name='subjects')
    address = models.TextField(max_length=500)
    type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_it_verified = models.BooleanField(default=False)


    #create_course = models.ManyToManyField(Course, on_delete=models.CASCADE)
    #create_announcement = models.ManyToManyField(Announcement, on_delete=models.CASCADE)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username


class Organization(models.Model):
    username = models.ForeignKey(Tutor, related_name='tutor_in_organization')
    type = models.CharField(max_length=100)
    size = models.PositiveIntegerField(null=True, blank=True, default=0)
    has_branch = models.CharField(max_length=200)

    class Meta:
        ordering = ('has_branch',)

    def __str__(self):
        return self.has_branch


class Course(models.Model):
    subject_name = models.ForeignKey(Subject, related_name='courses_created')
    level = models.CharField(max_length=50)
    username = models.ForeignKey(Tutor, related_name='tutor_in_courses')
    description = models.TextField(max_length=1000)
    price = models.FloatField(null=True, blank=True, default=0)
    location = models.TextField(max_length=200, default='Incheon')
    contact = models.TextField(max_length=1000)
    number_of_students = models.PositiveIntegerField(default=12)

    class Meta:
        ordering = ('subject_name',)

    def __str__(self):
        return str(self.subject_name)


class Announcement(models.Model):
    subject_name = models.ForeignKey(Subject, related_name='announcements_created')
    username = models.ForeignKey(Tutor, related_name='tutor_in_announcement')
    description = models.TextField(max_length=1000)
    schedule = models.TextField(max_length=1000)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('subject_name',)

    def __str__(self):
        return str(self.subject_name)


class Learner(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    country_code = models.CharField(max_length=4)
    phone_number = models.CharField(unique=True, max_length=11)
    photo = models.ImageField(upload_to=RandomFileName('photos'), blank=True, null=True)
    fav_announcement = models.ManyToManyField(Announcement, related_name='favorite_announcement')
    apply_course = models.ManyToManyField(Course, blank=True, related_name='apply_course')
    fav_course = models.ManyToManyField(Course, blank=True, related_name='fav_course')
    fav_tutor = models.ManyToManyField(Tutor, blank=True, related_name='fav_tutor')
    is_active = models.BooleanField(default=True)
    is_it_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username


class Sms(models.Model):
    country_code = models.CharField(max_length=4)
    phone_number = models.CharField(unique=True, max_length=11)
    verification_code = models.IntegerField()

    class Meta:
        ordering = ('phone_number',)

    def __str__(self):
        return self.phone_number






