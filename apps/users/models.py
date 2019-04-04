from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER = (
        ('M','male'),
        ('F','female'),
        ('NONB','non-binary'),
        ('PNS','prefer not to say'),
)

MEM_LEVEL = (
        ('AF', 'Always Forgetful'),
        ('SF', 'Somewhat Forgetful'),
        ('AVE', 'Average Memory'),
        ('GMEM', 'Good Memory'),
        ('EMEM', 'Perfect/Eidetic Memory')
)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default = 0)
    gender = models.CharField(max_length = 30, choices = GENDER,)
    memory = models.CharField(max_length = 30, choices = MEM_LEVEL,)
    country = models.CharField(max_length=100, default='Philippines')
    about = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
