# Generated by Django 5.0.3 on 2024-03-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_project_issue_issue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_history',
            name='reporting_manager',
            field=models.CharField(max_length=200),
        ),
    ]
