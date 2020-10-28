from django.db import models

# Create your models here.
class User(models.Model):

    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'protect'),
    )

    username = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    gender = models.SmallIntegerField(choices=gender_choices, default=2)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'drf_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

