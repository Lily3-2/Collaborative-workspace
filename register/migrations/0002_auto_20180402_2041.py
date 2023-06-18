# Generated by Django 2.0.3 on 2018-04-02 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='register.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='project',
            field=models.ManyToManyField(blank=True, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='invite',
            name='invited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='received_invites', to='register.UserProfile'),
        ),
        migrations.AddField(
            model_name='invite',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='made_invites', to='register.UserProfile'),
        ),
    ]
