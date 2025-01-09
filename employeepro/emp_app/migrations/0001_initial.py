# Generated by Django 5.1.4 on 2025-01-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('date_of_join', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=50)),
                ('dob', models.DateField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='emp_images')),
            ],
        ),
    ]
