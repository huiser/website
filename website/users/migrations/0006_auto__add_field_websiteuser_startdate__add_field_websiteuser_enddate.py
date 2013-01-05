# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WebsiteUser.startdate'
        db.add_column(u'users_websiteuser', 'startdate',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 1, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'WebsiteUser.enddate'
        db.add_column(u'users_websiteuser', 'enddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2040, 5, 20, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WebsiteUser.startdate'
        db.delete_column(u'users_websiteuser', 'startdate')

        # Deleting field 'WebsiteUser.enddate'
        db.delete_column(u'users_websiteuser', 'enddate')


    models = {
        u'users.websiteuser': {
            'Meta': {'object_name': 'WebsiteUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2040, 5, 20, 0, 0)'}),
            'enddate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2040, 5, 20, 0, 0)'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['users']