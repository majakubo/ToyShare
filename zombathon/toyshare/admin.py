from django.contrib import admin
from toyshare.models import *
admin.site.register(ExtUser)
admin.site.register(Toy)
admin.site.register(Renting)
admin.site.register(Rate)
admin.site.register(Wants)
admin.site.register(Unwanted)

# Register your models here.
