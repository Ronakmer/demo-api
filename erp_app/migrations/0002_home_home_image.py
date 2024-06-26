# Generated by Django 4.1.5 on 2023-08-31 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("erp_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="home",
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
                ("name", models.CharField(default="", max_length=30)),
                ("data", models.CharField(default="", max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="home_image",
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
                ("image", models.FileField(upload_to="erp_app/img")),
                (
                    "image_is",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="erp_app.home"
                    ),
                ),
            ],
        ),
    ]
