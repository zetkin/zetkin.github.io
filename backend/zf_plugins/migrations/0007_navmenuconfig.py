# Generated by Django 2.1 on 2019-09-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('zf_plugins', '0006_wideimageconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenuConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='zf_plugins_navmenuconfig', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(max_length=100)),
                ('symbol', models.CharField(blank=True, choices=[(None, '-'), ('book', 'Book'), ('calendar', 'Calendar'), ('chat', 'Chat'), ('feed', 'Feed'), ('info', 'Info'), ('money', 'Money'), ('person', 'Person'), ('pin', 'Pin'), ('point', 'Point'), ('question', 'Question'), ('share', 'Share'), ('sound', 'Sound'), ('time', 'Time')], max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
