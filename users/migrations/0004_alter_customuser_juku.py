# Generated by Django 4.1.1 on 2022-09-11 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_juku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='juku',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.juku'),
        ),
    ]
