# Generated by Django 4.2.6 on 2023-10-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0002_homedetails_sitesetting_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetails',
            name='body1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetails',
            name='body2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetails',
            name='body3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homedetails',
            name='header1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homedetails',
            name='header2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homedetails',
            name='header3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
