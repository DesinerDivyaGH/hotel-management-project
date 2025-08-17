from django.contrib import admin
from .models import Hotels
from .models import Rooms
from .models import Reservation

from .models import Contact



# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)

admin.site.register(Contact)






 
