# Generated by Django 4.2.4 on 2023-09-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_alter_post_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='complete',
            field=models.CharField(choices=[('예', '예'), ('아니요', '아니요')], default='아니요', max_length=10, verbose_name='입금을 하셨나요?'),
        ),
    ]