from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Todo)
admin.site.register(Department)
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Doctors)