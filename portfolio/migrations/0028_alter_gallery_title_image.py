# Generated by Django 5.0.4 on 2024-06-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_gallery_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title_image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
