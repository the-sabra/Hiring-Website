# Generated by Django 4.0.6 on 2022-08-21 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_city', to='accounts.city'),
            preserve_default=False,
        ),
    ]