#!/usr/bin/env python3

# -------
# imports
# -------

from django.test import TestCase
from django.test.utils import setup_test_environment
from myapp.models import State, Park, Hike

# -----------
# test
# -----------

class Test (TestCase) :

	# ----
	# State Model
	# ----


	def test_state1 (self) :

		s = State.objects.get(name = "Arizona")
		p = Park.objects.filter(state = s)
		if p[0] is not null :
			self.assertEqual(p[0].state, s.name) 
		self.assertTrue(isInstance(s, State))
		self.assertEqual(s.__unicode__(), s.name)
		self.assertEqual(s.__unicode__(), s.date_founded)


	def test_state2 (self) :

		s = State.objects.get(name = "Colorado")

		self.assertTrue(isInstance(s, State))
		self.assertEqual(s.__unicode__(), s.name)
		self.assertEqual(s.__unicode__(), s.date_founded)		

	def test_state3 (self) :

		s = State.objects.get(name = "Washington")

		self.assertTrue(isInstance(s, State))
		self.assertEqual(s.__unicode__(), s.name)
		self.assertEqual(s.__unicode__(), s.date_founded)		


	# ----
	# Park Model
	# ----



	def test_park1 (self) :

		p = Park.objects.get(name = "Grand Canyon")

		self.assertTrue(isInstance(p, Park))
		self.assertEqual(p.date_founded, "02/26/1919")
		self.assertEqual(p.__unicode__(), p.name)
		self.assertEqual(p.__unicode__(), p.date_founded)				

	def test_park2 (self) :

		p = Park.objects.get(name = "Rocky Mountain")

		self.assertTrue(isInstance(p, Park))
		self.assertEqual(p.date_founded, "01/26/1915")
		self.assertEqual(p.__unicode__(), p.name)
		self.assertEqual(p.__unicode__(), p.date_founded)


	def test_park3 (self) :

		p = Park.objects.get(name = "Denali")

		self.assertTrue(isInstance(p, Park))
		self.assertEqual(p.date_founded, "02/26/1917")
		self.assertEqual(p.__unicode__(), p.name)
		self.assertEqual(p.__unicode__(), p.date_founded)



	# ----
	# Hike Model
	# ----



	def test_hike1 (self) :

		h = Hike.objects.get(name = "Gower Gulch Loop")

		self.assertTrue(isInstance(h, Hike))
		self.assertEqual(h.difficulty, "moderate")
		self.assertEqual(p.__unicode__(), h.name)
		self.assertEqual(p.__unicode__(), h.difficulty)



	def test_hike2 (self) :

		h = Hike.objects.get(name = "Lower Yosemite Fall Trail")

		self.assertTrue(isInstance(h, Hike))
		self.assertEqual(h.difficulty, "easy")
		self.assertEqual(p.__unicode__(), h.name)
		self.assertEqual(p.__unicode__(), h.difficulty)


	def test_hike3 (self) :

		h = Hike.objects.get(name = "Mount Healy")

		self.assertTrue(isInstance(h, Hike))
		self.assertEqual(h.difficulty, "strenuous")
		self.assertEqual(p.__unicode__(), h.name)
		self.assertEqual(p.__unicode__(), h.difficulty)


# ----
# main
# ----

setup_test_environment()
#main()
