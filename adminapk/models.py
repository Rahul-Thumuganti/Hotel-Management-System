from django.db import models
from django.utils import timezone
from datetime import datetime


# --------------Hotel_Profile--------------#
class Hotel_Profile(models.Model):
    Hotel_name = models.CharField(max_length=200, null=True, blank=False)
    username = models.CharField(max_length=200, null=True, blank=False)
    Hotel_registration_number = models.CharField(max_length=14)
    hotel_image = models.ImageField()
    contact_by_mobile = models.CharField(max_length=200, null=False, blank=False)
    contact_by_mail = models.CharField(max_length=200, null=False, blank=False)
    About_us = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.Hotel_name


class amenities(models.Model):
    amenitie = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField()
    Ame_description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amenitie


from django.db import models
from datetime import datetime


class branch_management(models.Model):
    branch_image = models.ImageField()
    room_numbers = models.CharField(max_length=200, null=False, blank=False)
    contact_by_mobile = models.CharField(max_length=11)
    contact_by_mail = models.CharField(max_length=11)
    country = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    Branchlocation = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    pincode = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.created_at}"


class room(models.Model):
    room_type = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.room_type


class hotel(models.Model):
    image = models.ImageField()
    hotel_type = models.CharField(max_length=200, null=False, blank=False)
    availability = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=200, null=False, blank=False)
    location = models.CharField(max_length=500, null=False, blank=False)
    amenities = models.CharField(max_length=500, null=False, blank=False)
    policy = models.BooleanField()
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_type


class language(models.Model):
    Language = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.language


class currency(models.Model):
    Currency = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.currency


class service(models.Model):
    Service = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service


class cctv(models.Model):
    city = models.ForeignKey(branch_management, on_delete=models.CASCADE)  # Foreignkey
    no_cctv = models.IntegerField(default=0)
    desc = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city


class fire(models.Model):
    city = models.ForeignKey(branch_management, on_delete=models.CASCADE)  # Foreignkey
    no_drills = models.IntegerField(default=0)
    desc_d = models.CharField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.b_name


# class medical(models.Model):
#     city = models.CharField(max_length=200, null=False, blank=False)
#     desc_m = models.CharField(max_length=500, null=False, blank=False)
#     status = models.BooleanField(default=True, null=True, blank=False)

#     def __str__(self):
#         return self.b_Name


class reservation(models.Model):
    profile_name = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=200, null=False, blank=False)
    email_id = models.EmailField()
    city = models.ForeignKey(branch_management, on_delete=models.CASCADE)
    room_type = models.ForeignKey(room, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, null=True, blank=False)
    number_of_guest = models.IntegerField(default=0, blank=True, null=True)
    number_of_child = models.IntegerField(default=0, blank=True, null=True)
    check_in = models.CharField(max_length=200, null=False, blank=False)
    check_out = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.profile_name


class Department(models.Model):
    department = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation = models.CharField(max_length=200, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.designation


class Admin_staff(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    employee_age = models.IntegerField()
    gender = models.CharField(max_length=200, null=False, blank=False)
    emp_address = models.CharField(max_length=500, null=False, blank=False)
    nationality = models.CharField(max_length=200, null=False, blank=False)
    mobile_number = models.CharField(max_length=200, null=False, blank=False)
    alternative_mobile_number = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    pincode = models.CharField(max_length=200, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # ForeignKey
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)  # ForeignKey
    city = models.ForeignKey(branch_management, on_delete=models.CASCADE)
    shift_timings = models.CharField(max_length=200, null=False, blank=False)
    type_of_emp = models.CharField(max_length=200, null=False, blank=False)
    passport_image = models.ImageField()
    id_prooof = models.ImageField()
    certificates = models.ImageField()
    signature = models.ImageField()
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Adding_Rooms(models.Model):
    city = models.ForeignKey(branch_management, on_delete=models.CASCADE)
    Room_image = models.ImageField(null=False, blank=False)
    Room_number = models.CharField(max_length=200, null=False, blank=False)
    Room_area = models.IntegerField()
    room_type = models.ForeignKey(room, on_delete=models.CASCADE)  # ForeignKey
    No_of_beds = models.CharField(max_length=5)
    Price = models.FloatField()
    Room_description = models.CharField(max_length=500)
    status = models.BooleanField(default=True, null=True, blank=False)


    def _str_(self):
        return self.room_type



class Food_Services(models.Model):
    Recepie_name = models.CharField(max_length=31)
    Recepie_image = models.ImageField(null=False, blank=False)
    meal_type = models.CharField(max_length=50, null=True)
    Food_category = models.CharField(max_length=50, null=False)
    Price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    Recepie_Category = models.CharField(max_length=50, null=True)
    recepie_description = models.CharField(max_length=500, null=False)
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.Recepie_name


# Create your models here.
class Manageusers(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    id_proof = models.ImageField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    status = models.BooleanField(default=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.full_name