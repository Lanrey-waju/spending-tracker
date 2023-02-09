from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from .managers import UserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="email address")
    first_name = models.CharField(max_length=30, blank=True, verbose_name="first name")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="last name")
    date_joimed = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    is_active = models.BooleanField(default=True, verbose_name="active")

    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name",]

    # class Meta:
    #     verbose_name = _("user")
    #     verbose_name_plural = _("users")

    def __str__(self):
        """
        return a human readable string representative of the user
        """
        return self.first_name

    def get_short_name(self):
        """
        Return the first name of the user
        """

        return self.first_name

