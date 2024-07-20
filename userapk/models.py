from django.db import models
from datetime import datetime


# Create your models here.
class User_Signup(models.Model):
    # Add a registration ID field
    registration_id = models.CharField(max_length=10, unique=True, editable=False)

    # Add a registration_count field to keep track of the count
    registration_count = models.PositiveIntegerField(default=0, editable=False)

    user_full_name = models.CharField(max_length=250)
    user_image = models.ImageField(upload_to="users", null=False)
    user_name = models.CharField(max_length=80, unique=True)
    user_gender = models.CharField(max_length=80)
    user_age = models.IntegerField(null=True, blank=True)
    user_nationality = models.CharField(max_length=200)
    user_email = models.EmailField()
    user_mobile_number = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=80)
    user_otp = models.IntegerField(null=True, blank=True)
    user_address = models.CharField(max_length=200)
    user_adhaar_number = models.IntegerField(null=True, blank=True)
    user_adhaar_pdf = models.FileField()
    user_date = models.DateTimeField(default=datetime.now)


    class Meta:
        ordering = ['-user_date']

    def __str__(self):
        return self.user_name

    def isExistsphone(self):
        if User_Signup.objects.filter(user_mobile_number=self.user_mobile_number):
            return True

        return False

    def isExistsemail(self):
        if User_Signup.objects.filter(user_email=self.user_email):
            return True

        return False

    @classmethod
    def generate_registration_id(cls):
        # Get the last two digits of the current year
        current_year = datetime.now().year % 100

        while True:
            # Generate a candidate registration ID
            count = cls.objects.count() + 1
            registration_id = f'{current_year:02d}RAJ {count}'

            # Check if the generated ID already exists in the database
            if not cls.objects.filter(registration_id=registration_id).exists():
                return registration_id

        # Optionally, you can add logic to handle the case where the maximum count is reached.

        return None  # Return None if no unique ID can be generated

    def save(self, *args, **kwargs):
        # Generate the registration ID only if it's not set
        if not self.registration_id:
            self.registration_id = self.generate_registration_id()

        super().save(*args, **kwargs)

    # ... other fields ...
