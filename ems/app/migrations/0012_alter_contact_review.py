# Generated by Django 5.1.2 on 2025-01-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
