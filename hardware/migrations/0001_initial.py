# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Hardware'
        db.create_table('hardware_hardware', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Employee'])),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hardware', ['Hardware'])

        # Adding model 'Computer'
        db.create_table('hardware_computer', (
            ('hardware_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hardware.Hardware'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('hardware', ['Computer'])

        # Adding model 'Phone'
        db.create_table('hardware_phone', (
            ('hardware_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hardware.Hardware'], unique=True, primary_key=True)),
            ('call_number', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('hardware', ['Phone'])


    def backwards(self, orm):
        
        # Deleting model 'Hardware'
        db.delete_table('hardware_hardware')

        # Deleting model 'Computer'
        db.delete_table('hardware_computer')

        # Deleting model 'Phone'
        db.delete_table('hardware_phone')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'employees.employee': {
            'Meta': {'object_name': 'Employee', '_ormbases': ['auth.User']},
            'entry_date': ('django.db.models.fields.DateField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['employees.Team']"}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'employees.team': {
            'Meta': {'ordering': "['parent_team__siglum', 'siglum']", 'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent_team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['employees.Team']", 'null': 'True', 'blank': 'True'}),
            'siglum': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        },
        'hardware.computer': {
            'Meta': {'object_name': 'Computer', '_ormbases': ['hardware.Hardware']},
            'hardware_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hardware.Hardware']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'hardware.hardware': {
            'Meta': {'object_name': 'Hardware'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['employees.Employee']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'hardware.phone': {
            'Meta': {'object_name': 'Phone', '_ormbases': ['hardware.Hardware']},
            'call_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'hardware_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hardware.Hardware']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['hardware']
