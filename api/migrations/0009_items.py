# Generated by Django 3.0 on 2020-05-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0008_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('from_items', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
                ('thedate', models.DateField(db_index=True)),
                ('id_items', models.IntegerField()),
            ],
        ),
    ]
