# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WebsiteUser.is_active'
        db.add_column(u'users_websiteuser', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'WebsiteUser.end'
        db.alter_column(u'users_websiteuser', 'end', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'WebsiteUser.is_active'
        db.delete_column(u'users_websiteuser', 'is_active')


        # Changing field 'WebsiteUser.end'
        db.alter_column(u'users_websiteuser', 'end', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'users.websiteuser': {
            'Meta': {'object_name': 'WebsiteUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2040, 5, 20, 0, 0)'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['users']