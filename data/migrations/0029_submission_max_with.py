# Generated by Django 2.2.24 on 2021-12-01 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0028_allow_longer_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='max_with',
            field=models.ForeignKey(blank=True, help_text='The submission the max_similarity refers to', null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Submission'),
        ),
    ]
