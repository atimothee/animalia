# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20141008_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phylum',
            new_name='classe',
        ),
    ]
