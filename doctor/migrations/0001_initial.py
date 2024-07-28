# Generated by Django 2.2.2 on 2019-06-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateDrReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=10000)),
                ('institute', models.CharField(max_length=1000)),
                ('patient', models.EmailField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CreateReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=10000)),
                ('institute', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('specialities', models.CharField(max_length=1000)),
                ('education', models.CharField(max_length=1000)),
                ('hospitals', models.CharField(max_length=1000)),
                ('rate', models.FloatField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Make_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorEmailId', models.EmailField(max_length=254)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('hr', models.IntegerField()),
                ('min', models.IntegerField()),
                ('problems', models.CharField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recharge_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_card', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Validate_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('hr', models.IntegerField()),
                ('min', models.IntegerField()),
                ('changedatetime', models.BooleanField(default=False)),
            ],
        ),
    ]
