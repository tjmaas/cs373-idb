#!/usr/bin/env python3

# -------
# imports
# -------

from django.test import TestCase
from django.test.utils import setup_test_environment
from myapp.models import Handle, Hashtag, Cluster

# -----------
# test
# -----------

class Test (TestCase) :
	# ----
	# Handle Model
	# ----

	def create_handle (self, username, name, bio) :
		return Handle.objects.create(username = "person", name = "realName", bio = "biography")

	def test_handle1 (self) :
		myHandle = self.create_handle(username = "Dwayne", name = "Dwayne Wade")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.__unicode__(), myHandle.username)

	def test_handle2 (self) :
		myHandle = self.create_handle(username = "Dwayne", bio = "basketball player")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.__unicode__(), myHandle.username)

	def test_handle3 (self) :
		myHandle = self.create_handle(bio = "basketball player", name = "Dwayne Wade")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.__unicode__(), myHandle.username)



	# ----
	# Hashtag Model
	# ----
	def create_hashtag (self, name, description):
		return Hashtag.objects.create(name = "hashtag", description = "person")

	def test_hashtag1 (self) :
		myHashtag = self.create_hashtag(name = "LebronSucks", description = "people hating Lebron")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.username)

	def test_hashtag2 (self) :
		myHashtag = self.create_hashtag(name = "LebronSucks", description = "people hating Lebron")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.username)


	def test_hashtag3 (self) :
		myHashtag = self.create_hashtag(name = "LebronSucks", description = "people hating Lebron")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.username)



	# ----
	# Cluster Model
	# ----
	def create_cluster (self, name, parents, description) :
		return Cluster.objects.create(name = "clusterName", parents = "parents", description = "descriptions")

	def test_cluster1 (self) :
		myCluster = self.create_handle(name = "NBAFinals", parents = "NBA", description = "finals bballz 2014")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.username)

	def test_cluster2 (self) :
		myCluster = self.create_handle(parents = "NBA", description = "finals bballz 2014")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.username)

	def test_cluster3 (self) :
		myCluster = self.create_handle(name = "NBAFinals", parents = "NBA")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.username)

# ----
# main
# ----

setup_test_environment()
#main()
