from django.db import models
from django.contrib.auth.models import User

class CommonToken(models.Model):
	""" Many models in our work suite purely 
		informational purpose and include
		'name' field and nothing more; we are
		going to use this class as an ancestor
		for those models.
	"""
	is_active = models.BooleanField(default = True)
	name = models.CharField(max_length = 100)

class CombatToken(CommonToken):
	""" Both types of units share basic statistics
		for combat; they are defined here to 
		avoid accidental typos
	"""
	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)
	
	ws = models.IntegerField(default = 0)
	bs = models.IntegerField(default = 0)
	armor = models.IntegerField(default = 0)
	wounds = models.IntegerField(default = 0)
	
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

class Character(CommonToken):
	previous_accounts = models.ManyToManyField('Account', blank = True)

	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)
	species = models.ForeignKey('Species', blank = True)

	wounds = models.IntegerField(default = 0)
	willpower = models.IntegerField(default = 0)

	# fiefs, units and ships are OneToMany rels, 
	# so they are defined in the corresponding classes

	def get_influence(self):
		pass

class Planet(CommonToken):
	status = models.CharField(max_length = 100)
	faction = models.ForeignKey('Faction', blank = True)
	species = models.ForeignKey('PlanetType', blank = True)

	host = models.ForeignKey('Character')

	def get_influence(self):
		pass

class PlanetType(CommonToken):
	pass
class Species(CommonToken):
	pass
class Faction(CommonToken):
	pass

class Unit(CombatToken):	
	quantity = models.IntegerField(default = 0)

class Ship(CombatToken):
	transport_capacity = models.IntegerField(default = 0)
	move = models.IntegerField(default = 0)	

