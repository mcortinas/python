# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.num_visits'
        db.add_column('contingut_article', 'num_visits',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.num_visits'
        db.delete_column('contingut_article', 'num_visits')


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
            'num_visits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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