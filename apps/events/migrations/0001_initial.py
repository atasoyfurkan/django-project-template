# Generated by Django 4.1.7 on 2023-03-25 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("entities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Epic",
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
                ("name", models.CharField(max_length=255)),
                ("participating_heroes", models.ManyToManyField(to="entities.hero")),
                (
                    "participating_villains",
                    models.ManyToManyField(to="entities.villain"),
                ),
            ],
            options={
                "verbose_name": "Epic",
                "verbose_name_plural": "Epics",
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                ("details", models.TextField()),
                ("years_ago", models.PositiveIntegerField()),
                (
                    "epic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.epic"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventVillain",
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
                ("is_primary", models.BooleanField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
                (
                    "hero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="entities.villain",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventHero",
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
                ("is_primary", models.BooleanField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
                (
                    "hero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="entities.hero"
                    ),
                ),
            ],
        ),
    ]
