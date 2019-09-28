# Generated by Django 2.1 on 2019-09-26 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('zf_plugins', '0002_buttonconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlurbConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='zf_plugins_blurbconfig', serialize=False, to='cms.CMSPlugin')),
                ('header', models.CharField(max_length=200)),
                ('symbol', models.CharField(blank=True, choices=[(None, '-'), ('book', 'Book'), ('calendar', 'Calendar'), ('chat', 'Chat'), ('feed', 'Feed'), ('info', 'Info'), ('money', 'Money'), ('person', 'Person'), ('pin', 'Pin'), ('point', 'Point'), ('question', 'Question'), ('share', 'Share'), ('sound', 'Sound'), ('time', 'Time')], max_length=20, null=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]