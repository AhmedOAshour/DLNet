# Generated by Django 3.2.12 on 2022-06-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_auto_20220622_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female')], default='', max_length=50, null=True),
        ),
    ]
