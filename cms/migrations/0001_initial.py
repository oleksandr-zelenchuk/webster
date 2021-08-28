# Generated by Django 3.2.6 on 2021-08-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg/')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Title')),
                ('cms_text', models.TextField(max_length=200, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]
