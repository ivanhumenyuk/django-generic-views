from django.db import models
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z][a-z]+(\s[A-Za-z][a-z]+)+$',
                message='Field should contains only alphabet letters, \
                        started with uppercase'
            )
        ]
    )
