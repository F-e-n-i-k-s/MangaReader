# Generated by Django 2.0.4 on 2018-04-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_auto_20180410_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='poster',
            field=models.ImageField(blank=True, upload_to='upload/manga/', verbose_name=models.CharField(max_length=250)),
        ),
    ]