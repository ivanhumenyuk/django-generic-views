from django.db import models
from management_system.department.models import Department
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone


class Employee(models.Model):
    first_name = models.CharField(
        max_length=120,
        validators=[
            RegexValidator(regex=r'^[A-Z][a-z]+$',
                           message='Field should contains only alphabet letters, \
                                                  started with uppercase')
        ]
    )
    last_name = models.CharField(
        max_length=120,
        validators=[
            RegexValidator(regex=r'^[A-Z][a-z]+$',
                           message='Field should contains only alphabet letters, \
                                                      started with uppercase')
        ]

    )
    age = models.IntegerField(
        validators=[
            MaxValueValidator(125, 'The maximum age of an employee does not exceed 125 years'),
            MinValueValidator(18, message='You must be over 18 years old')
        ]
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(regex=r'^[\w\-.]+@[\w\-]+\.[\w.]+$',
                           message="""Field should contains alphabet symbols in lower case,
                                   digits, signs '@', '-' and '.' in your e-mail field!""")
        ]
    )
    hire_date = models.DateField(editable=True, default=timezone.now())
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)