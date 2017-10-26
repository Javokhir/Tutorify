from django.contrib import admin
from . models import Tutor, Organization, Learner, Subject, Course, Announcement

# Register your models here.


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['username', 'subject_name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['username', ]


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'category']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['username', 'subject_name', 'price']
    list_filter = ['price', 'subject_name']
    search_fields = ['subject_name', 'description']


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['username', 'subject_name', 'description']
