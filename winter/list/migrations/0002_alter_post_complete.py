# Generated by Django 4.2.4 on 2023-09-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='complete',
            field=models.CharField(max_length=128, verbose_name='입금을 하셨나요?'),
        ),
    ]
