# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class State(models.Model):
	class Meta:
		db_table='project_one_state'

	id 				  = models.AutoField(primary_key=True)
	name  		 	  = models.CharField(max_length=50)
	abbr	     	  = models.CharField(max_length=2)
	creation_date 	  = models.DateTimeField(default=datetime.now)
	last_update_date  = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name

class City(models.Model):
	id 				 = models.AutoField(primary_key=True)
	name			 = models.CharField(max_length=50)
	state            = models.ForeignKey(State)
	creation_date 	 = models.DateField(default=datetime.now)
	last_update_date = models.DateField(default=datetime.now)