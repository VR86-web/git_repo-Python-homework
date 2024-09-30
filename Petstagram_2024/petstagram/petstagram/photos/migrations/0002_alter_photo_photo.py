# Generated by Django 4.2.16 on 2024-09-30 18:41

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='media_files', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]
