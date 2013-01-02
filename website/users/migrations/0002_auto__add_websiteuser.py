# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebsiteUser'
        db.create_table(u'users_websiteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75, db_index=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['WebsiteUser'])


    def backwards(self, orm):
        # Deleting model 'WebsiteUser'
        db.delete_table(u'users_websiteuser')


    models = {
        u'users.websiteuser': {
            'Meta': {'object_name': 'WebsiteUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['users']