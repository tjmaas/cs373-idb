#!/usr/bin/env python3

# -------
# imports
# -------

from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from .models import State, Park, Hike


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

		s = State.objects.create(
			name = "Granola",
			date_founded = "19/90/1990",
			flag = "Cereal",
			population = 2,
			size = -37,
			video = "Box")

		p = Park.objects.create(
		    name = "Auditorium Shores",
		    state = s,
		    size = 27,
		    max_elevation = 9000,
		    date_founded = "1/31/2000",
		    park_image = "Pretty Skyline",
		    num_visitors = 5000,
		    video = "YouTube Video")


		self.assertTrue(type(p.state) == State)
		self.assertEqual(p.state.video, "Box")
		self.assertEqual(p.video, "YouTube Video")
		self.assertEqual(p.max_elevation, 9000)



	# ----
	# Hike Model
	# ----



	def test_hike1 (self) :
		s = State.objects.create(
			name = "Granola",
			date_founded = "19/90/1990",
			flag = "Cereal",
			population = 2,
			size = -37,
			video = "Box")

		p = Park.objects.create(
		    name = "Auditorium Shores",
		    state = s,
		    size = 27,
		    max_elevation = 9000,
		    date_founded = "1/31/2000",
		    park_image = "Pretty Skyline",
		    num_visitors = 5000,
		    video = "YouTube Video")

		h = Hike.objects.create (
		    name = "Simple Hike",
		    distance = 1,
		    est_time = 60,
		    hike_image = "pretty trees",
		    difficulty = "Moderate",
		    park = p )


		self.assertTrue(type(h) == Hike)
		self.assertEqual(h.name, "Simple Hike")
		self.assertEqual(h.hike_image, "pretty trees")
		self.assertEqual(h.difficulty, "Moderate")



	def test_hike2 (self) :
		s = State.objects.create(
			name = "Granola",
			date_founded = "19/90/1990",
			flag = "Cereal",
			population = 2,
			size = -37,
			video = "Box")

		p = Park.objects.create(
		    name = "Auditorium Shores",
		    state = s,
		    size = 27,
		    max_elevation = 9000,
		    date_founded = "1/31/2000",
		    park_image = "Pretty Skyline",
		    num_visitors = 5000,
		    video = "YouTube Video")

		h = Hike.objects.create (
		    name = "Hard Hike",
		    distance = 1,
		    est_time = 60,
		    hike_image = "pretty trees",
		    difficulty = "Moderate",
		    park = p )

		self.assertTrue(type(h.park) == Park )
		self.assertTrue(type(h.park.state == State))


	def test_hike3 (self) :

		s = State.objects.create(
			name = "Granola",
			date_founded = "19/90/1990",
			flag = "Cereal",
			population = 2,
			size = -37,
			video = "Box")

		p = Park.objects.create(
			name = "Auditorium Shores",
			state = s,
			size = 27,
			max_elevation = 9000,
			date_founded = "1/31/2000",
			park_image = "Pretty Skyline",
			num_visitors = 5000,
			video = "1924")

		h = Hike.objects.create (
			name = "Gatsby Trail",
			distance = 22,
			est_time = 33,
			hike_image = "44",
			difficulty = "55",
			park = p )

		self.assertTrue(h.distance < h.est_time)
		self.assertEqual(h.difficulty, "55")
		self.assertTrue(h.distance < h.park.size)
		self.assertTrue(h.name != h.park.name != h.park.state.name)




	# ----
	# API Request Tests
	# ----

	def setUp (self) :
	    self.c = Client()


	def test_api_state_1 (self) :
	    response = self.c.get('/api/states/ABC/')

	    self.assertEqual(response.status_code,404)

	def test_api_state_2 (self) :
	    response = self.c.get('/api/states/ABC')

	    self.assertEqual(response.status_code,301)

	def test_api_state_3 (self) :
	    response = self.c.get('/api/states/')

	    self.assertEqual(response.status_code,200)

	def test_api_park_1 (self) :
	    response = self.c.get('/api/parks/P/')

	    self.assertEqual(response.status_code,404)

	def test_api_park_2 (self) :
	    response = self.c.get('/api/parks/')

	    self.assertEqual(response.status_code,200)

	def test_api_park_3 (self) :
	    response = self.c.get('/api/parks')

	    self.assertEqual(response.status_code,301)


	def test_api_hike_1 (self) :
	    response = self.c.get('/api/hikes/h2/')

	    self.assertEqual(response.status_code,404)

	def test_api_hike_2 (self) :
	    response = self.c.get('/api/hikes/')

	    self.assertEqual(response.status_code,200)

	def test_api_hike_3 (self) :
	    response = self.c.get('/api/hikes/h')

	    self.assertEqual(response.status_code,301)

















# ----
# main
# ----

setup_test_environment()

# main()
