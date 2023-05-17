# Generated by Django 4.1.7 on 2023-05-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Contact", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
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
                ("Email", models.CharField(max_length=100)),
                ("Password", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="registration",
            name="Mobile_No",
            field=models.IntegerField(default="0"),
        ),
    ]
