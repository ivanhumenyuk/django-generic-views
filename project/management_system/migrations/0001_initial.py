# Generated by Django 3.1.2 on 2020-10-20 13:35

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, validators=[django.core.validators.RegexValidator(message='Field should contains only alphabet letters,                         started with uppercase', regex='^[A-Z][a-z]+(\\s[A-Za-z][a-z]+)+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, validators=[django.core.validators.RegexValidator(message='Field should contains only alphabet letters,                                                   started with uppercase', regex='^[A-Z][a-z]+$')])),
                ('last_name', models.CharField(max_length=120, validators=[django.core.validators.RegexValidator(message='Field should contains only alphabet letters,                                                       started with uppercase', regex='^[A-Z][a-z]+$')])),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(125, 'The maximum age of an employee does not exceed 125 years'), django.core.validators.MinValueValidator(18, message='You must be over 18 years old')])),
                ('email', models.EmailField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message="Field should contains alphabet symbols in lower case,\n                                   digits, signs '@', '-' and '.' in your e-mail field!", regex='^[\\w\\-.]+@[\\w\\-]+\\.[\\w.]+$')])),
                ('hire_date', models.DateField(default=datetime.datetime(2020, 10, 20, 13, 35, 16, 249576, tzinfo=utc))),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management_system.department')),
            ],
        ),
    ]