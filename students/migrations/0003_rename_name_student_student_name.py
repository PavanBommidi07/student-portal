# Generated by Django 5.2.4 on 2025-07-16 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_student_name_student_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
    ]
