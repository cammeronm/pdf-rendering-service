# Generated by Django 3.1.5 on 2021-01-24 12:30

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_name', models.TextField(blank=True)),
                ('status', models.TextField(blank=True, choices=[(0, 'processing'), (1, 'done')], db_index=True, default=0)),
                ('n_pages', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
    ]
