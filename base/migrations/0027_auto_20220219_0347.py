# Generated by Django 3.2.12 on 2022-02-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_patient_assigned_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='username',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
    ]
