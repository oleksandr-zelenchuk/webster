# Generated by Django 3.2.6 on 2021-08-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Phone'),
        ),
    ]
