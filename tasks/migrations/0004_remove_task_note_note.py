# Generated by Django 4.2.7 on 2023-11-12 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_delete_note_task_note"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="note",
        ),
        migrations.CreateModel(
            name="Note",
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
                ("note", models.TextField(null=True)),
                (
                    "task",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
    ]