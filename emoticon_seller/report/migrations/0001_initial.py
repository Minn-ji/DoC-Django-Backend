# Generated by Django 5.0.6 on 2024-06-26 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                ("reportId", models.AutoField(primary_key=True, serialize=False)),
                ("age", models.PositiveIntegerField()),
                ("gender", models.CharField(max_length=3)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "report",
            },
        ),
    ]
