# Generated by Django 4.2.6 on 2023-11-02 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0005_alter_accessor_book_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessor',
            name='date_checked_out',
        ),
    ]
