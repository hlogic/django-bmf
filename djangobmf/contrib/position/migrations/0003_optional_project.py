# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [
        ('djangobmf_position', '0002_optional_employee'),
        migrations.swappable_dependency(settings.BMF_CONTRIB_PROJECT),
    ]
    operations = [
        migrations.AddField(
            model_name='position',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.BMF_CONTRIB_PROJECT, null=True, related_name="+"),
            preserve_default=True,
        ),
    ]
