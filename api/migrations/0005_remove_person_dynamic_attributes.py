# Generated by Django 4.2.5 on 2023-09-12 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_dynamic_attibutes_person_dynamic_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='dynamic_attributes',
        ),
    ]
