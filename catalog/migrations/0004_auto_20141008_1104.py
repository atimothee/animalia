# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20141008_1103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Classe',
            new_name='Class',
        ),
    ]
