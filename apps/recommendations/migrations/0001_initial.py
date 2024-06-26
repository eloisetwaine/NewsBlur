# Generated by Django 2.0 on 2020-06-16 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rss_feeds", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RecommendedFeed",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("is_public", models.BooleanField(default=False)),
                ("created_date", models.DateField(auto_now_add=True)),
                ("approved_date", models.DateField(null=True)),
                ("declined_date", models.DateField(null=True)),
                ("twitter", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "feed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recommendations",
                        to="rss_feeds.Feed",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recommendations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-approved_date", "-created_date"],
            },
        ),
        migrations.CreateModel(
            name="RecommendedFeedUserFeedback",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("score", models.IntegerField(default=0)),
                ("created_date", models.DateField(auto_now_add=True)),
                (
                    "recommendation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback",
                        to="recommendations.RecommendedFeed",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feed_feedback",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
