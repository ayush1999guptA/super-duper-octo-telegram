# Generated by Django 2.2 on 2019-04-19 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190419_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('writeup', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rollnumber', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=3)),
                ('photo', models.ImageField(upload_to='')),
                ('discription', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='FirstYear',
        ),
        migrations.DeleteModel(
            name='FourthYear',
        ),
        migrations.DeleteModel(
            name='NotificationF',
        ),
        migrations.DeleteModel(
            name='NotificationS',
        ),
        migrations.DeleteModel(
            name='NotificationT',
        ),
        migrations.DeleteModel(
            name='NotificationU',
        ),
        migrations.DeleteModel(
            name='SecondYear',
        ),
        migrations.DeleteModel(
            name='ThirdYear',
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Year'),
        ),
        migrations.AddField(
            model_name='notification',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Year'),
        ),
    ]
