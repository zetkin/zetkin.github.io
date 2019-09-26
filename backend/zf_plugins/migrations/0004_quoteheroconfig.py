# Generated by Django 2.1 on 2019-09-26 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
        ('zf_plugins', '0003_blurbconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteHeroConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='zf_plugins_quoteheroconfig', serialize=False, to='cms.CMSPlugin')),
                ('citation', models.CharField(max_length=400)),
                ('quote', models.CharField(max_length=200)),
                ('background', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_hero_background', to=settings.FILER_IMAGE_MODEL)),
                ('portrait', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_hero_portrait', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
