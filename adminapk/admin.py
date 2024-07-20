from django.contrib import admin
from .models import branch_management,room,hotel,amenities,currency,language,service,fire,cctv,reservation,Admin_staff,Adding_Rooms,Hotel_Profile,Food_Services,Manageusers

admin.site.register(branch_management)

admin.site.register(room)
admin.site.register(hotel)
admin.site.register(amenities)

admin.site.register(currency)
admin.site.register(language)
admin.site.register(service)
admin.site.register(cctv)
admin.site.register(fire)

admin.site.register(reservation)
admin.site.register(Admin_staff)
admin.site.register(Adding_Rooms)
admin.site.register(Hotel_Profile)
admin.site.register(Food_Services)
admin.site.register(Manageusers)