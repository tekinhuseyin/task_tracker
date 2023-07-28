# Generated by Django 4.2.3 on 2023-07-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField()),
            ],
        ),
    ]
