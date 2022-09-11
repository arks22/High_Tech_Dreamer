# Generated by Django 4.1 on 2022-09-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Records",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.DateField(null=True, verbose_name="年月日")),
                (
                    "type",
                    models.CharField(
                        choices=[("A", "定期"), ("B", "模試")],
                        max_length=20,
                        verbose_name="定期or模試",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("A", "国語"),
                            ("B", "数学"),
                            ("C", "理科"),
                            ("D", "社会"),
                            ("E", "英語"),
                        ],
                        max_length=20,
                        verbose_name="科目選択",
                    ),
                ),
                ("score", models.FloatField(verbose_name="点数")),
                ("averagescore", models.FloatField(verbose_name="平均点")),
            ],
        ),
    ]