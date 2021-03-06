# Generated by Django 3.0.4 on 2020-03-26 02:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('des', models.CharField(blank=True, max_length=1024)),
                ('year', models.IntegerField()),
                ('brand', models.CharField(max_length=64)),
                ('category', models.CharField(choices=[('Hatchback', 'Hatchback'), ('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Trucks', 'Trucks')], max_length=32)),
                ('model', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('horsepower', models.IntegerField()),
                ('mpg', models.IntegerField(help_text='Combined Fuel Economy')),
                ('fuelType', models.CharField(default='Gasoline', max_length=32)),
                ('seating', models.CharField(default='Second Row Seating', max_length=32)),
                ('drivetrain', models.CharField(default='FWD', max_length=32)),
                ('interiorColor', models.CharField(default='white', max_length=32)),
                ('exteriorColor', models.CharField(default='white', max_length=32)),
                ('engine', models.CharField(blank=True, max_length=64)),
                ('transmission', models.CharField(blank=True, max_length=64)),
                ('stockid', models.CharField(blank=True, max_length=64)),
                ('vin', models.CharField(blank=True, max_length=64)),
                ('mileage', models.IntegerField(default=50)),
                ('expertRating', models.IntegerField(default=3)),
                ('img', models.CharField(default='cars/1.png', max_length=64)),
                ('detailImgs', models.CharField(default='cars/1.png', max_length=256)),
                ('enable', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img', models.CharField(default='avatars/1.png', max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('saveForLater', models.BooleanField(default=False)),
                ('createTime', models.DateField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['createTime'],
                'unique_together': {('user', 'car')},
            },
        ),
    ]
