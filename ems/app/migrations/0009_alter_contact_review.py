# Generated by Django 5.1.2 on 2025-01-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='review',
            field=models.TextField(),
        ),
    ]