# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('contingut_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['contingut.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal('contingut', ['Category'])

        # Adding model 'Article'
        db.create_table('contingut_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles', to=orm['contingut.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('contingut', ['Article'])

        # Adding model 'Comment'
        db.create_table('contingut_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['contingut.Article'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('contingut', ['Comment'])

        # Adding model 'Ad'
        db.create_table('contingut_ad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('contingut', ['Ad'])

        # Adding model 'ClientMessage'
        db.create_table('contingut_clientmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('contingut', ['ClientMessage'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('contingut_category')

        # Deleting model 'Article'
        db.delete_table('contingut_article')

        # Deleting model 'Comment'
        db.delete_table('contingut_comment')

        # Deleting model 'Ad'
        db.delete_table('contingut_ad')

        # Deleting model 'ClientMessage'
        db.delete_table('contingut_clientmessage')


    models = {
        'contingut.ad': {
            'Meta': {'ordering': "['id']", 'object_name': 'Ad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'contingut.article': {
            'Meta': {'ordering': "['-publish_date']", 'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': "orm['contingut.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contingut.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['contingut.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'contingut.clientmessage': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'ClientMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contingut.comment': {
            'Meta': {'ordering': "['id']", 'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['contingut.Article']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['contingut']