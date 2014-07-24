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

		s = State.objects.create(
			name = "Arizona",
			date_founded = "12/12/1212",
			flag = "www.google.com",
			population = 1000,
			size = 10,
			video = "myvideourl")

		self.assertTrue(type(s) == State)
		self.assertEqual("Arizona", s.name)
		self.assertEqual("12/12/1212", s.date_founded)


	def test_state2 (self) :

		s = State.objects.create(
			name = "Colorado",
			date_founded = "12/12/1212",
			flag = "www.google.com",
			population = 1000,
			size = 10,
			video = "myvideourl")

		self.assertTrue(s.population > 10)
		self.assertEqual(s.size, 10)
		self.assertTrue(type(s) == State)

	def test_state3 (self) :

		s = State.objects.create(
			name = "Colorado",
			date_founded = "End of the World",
			flag = "www.reddit.com",
			population = -200,
			size = 0,
			video = "videoOfCats")

		self.assertTrue(s.population == -200)
		self.assertEqual(s.size, 0)
		self.assertTrue(type(s) == State)
		self.assertEqual(s.date_founded, "End of the World")
		self.assertEqual(s.flag, "www.reddit.com")
		self.assertEqual(s.video, "videoOfCats")



	# ----
	# Park Model
	# ----



	def test_park1 (self) :

		s = State.objects.create(
			name = "Colorado",
			date_founded = "End of the World",
			flag = "www.reddit.com",
			population = -200,
			size = 0,
			video = "videoOfCats")

		p = Park.objects.create(
		    name = "Zilker Park",
		    state = s,
		    size = 0,
		    max_elevation = 9999,
		    date_founded = "1/1/2000",
		    park_image = "www.amazon.com",
		    num_visitors = 42,
		    video = "ThisIsAVideo")

		self.assertTrue(type(p) == Park)
		self.assertTrue(type(p.state) == State)


	def test_park2 (self) :

		s = State.objects.create(
			name = "Arizona",
			date_founded = "12/12/1212",
			flag = "www.google.com",
			population = 1000,
			size = 10,
			video = "myvideourl")

		p = Park.objects.create(
		    name = "Zilker Park",
		    state = s,
		    size = 0,
		    max_elevation = 9999,
		    date_founded = "1/1/2000",
		    park_image = "www.amazon.com",
		    num_visitors = 42,
		    video = "ThisIsAVideo")

		self.assertTrue(p.max_elevation == 9999)
		self.assertEqual(p.size, 0)
		self.assertEqual(p.state.population, 1000)
		self.assertEqual(p.state.size, 10)


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
