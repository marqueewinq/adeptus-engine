from django.db import models
from django.contrib.auth.models import User
	
class Account(models.Model):
	# because django already have User interface for auth,
	# we are not going to reimplement that anew; instead, 
	# we are making OneToOne connection to associated users,
	# effectively adding new fields to User model.
	# Usage:
	#	get django.User by Account: account.user
	# 	get Account by django.User: user.account
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	characters = models.ManyToManyField('Character', blank = True)

	def __str__(self):
		return "{}".format(self.user.username)

class Character(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)
	previous_accounts = models.ManyToManyField('Account', blank = True)

	status = models.CharField(max_length = 100)
	faction = models.ManyToManyField('Faction', blank = True)
	species = models.ForeignKey('Species', blank = True)

	wounds = models.IntegerField(default = 0)
	willpower = models.IntegerField(default = 0)

	# fiefs, units and ships are OneToMany rels, 
	# so they are defined in the corresponding classes

	def get_influence(self):
		pass

	def __str__(self):
		return "{name}, {status}".format(name = self.name, status = self.status)


class Planet(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)

	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)
	species = models.ForeignKey('PlanetType', blank = True)

	host = models.ForeignKey('Character')

	def get_influence(self):
		pass

	def __str__(self):
		return "{}".format(self.name)

class PlanetType(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)

	def __str__(self):
		return "{}".format(self.name)

class Species(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return "{}".format(self.name)

class Faction(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return "{}".format(self.name)

class Unit(models.Model):	
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)

	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)

	quantity = models.IntegerField(default = 0)

	ws = models.IntegerField(default = 0)
	bs = models.IntegerField(default = 0)
	armor = models.IntegerField(default = 0)
	wounds = models.IntegerField(default = 0)

	def __str__(self):
		return "{}".format(self.name)

class Ship(models.Model):
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)

	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)

	transport_capacity = models.IntegerField(default = 0)
	move = models.IntegerField(default = 0)	
	
	ws = models.IntegerField(default = 0)
	bs = models.IntegerField(default = 0)
	armor = models.IntegerField(default = 0)
	wounds = models.IntegerField(default = 0)

	def __str__(self):
		return "{}".format(self.name)

class Event(models.Model):
	pass

	def __str__(self):
		return 