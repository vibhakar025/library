# Generated by Django 5.0.4 on 2024-04-06 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('BookID', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('BookName', models.CharField(default=None, max_length=100)),
                ('NumberOfCopies', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('MemberID', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('MemberName', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CirculationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventType', models.IntegerField(default=None)),
                ('Date', models.DateField(default=None)),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.books')),
                ('MemberId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.members')),
            ],
        ),
        migrations.CreateModel(
            name='Circulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventType', models.IntegerField(default=None)),
                ('Date', models.DateField(default=None)),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.books')),
                ('MemberId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.members')),
            ],
        ),
    ]
