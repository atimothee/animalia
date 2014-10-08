# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20141008_1100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Classe',
        ),
    ]
