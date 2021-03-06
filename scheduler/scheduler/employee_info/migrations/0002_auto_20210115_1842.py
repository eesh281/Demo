# Generated by Django 3.1.5 on 2021-01-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='preferred_slot',
            field=models.CharField(choices=[('06:00am-02:00pm', '06:00am-02:00pm'), ('02:00pm-10:00pm', '02:00pm-10:00pm'), ('10:00pm-06:00am', '10:00pm-06:00am')], default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
