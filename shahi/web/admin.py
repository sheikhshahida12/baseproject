from django.contrib import admin
from .models import employee,student,Teacher

class TeacherAdmin(admin.ModelAdmin):
     list_display = ('name','age','subject')
# Register your models here.
admin.site.register(employee),
admin.site.register(Teacher)
