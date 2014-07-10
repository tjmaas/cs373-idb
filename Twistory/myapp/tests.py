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
		self.assertEqual(myCluster.__unicode__(), myHandle.name)		

	def test_handle2 (self) :
		myHandle = self.create_handle(username = "Dwayne", bio = "basketball player")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.__unicode__(), myHandle.username)
		self.assertEqual(myCluster.__unicode__(), myHandle.bio)	

	def test_handle3 (self) :
		myHandle = self.create_handle(bio = "basketball player", name = "Dwayne Wade")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.__unicode__(), myHandle.bio)
		self.assertEqual(myCluster.__unicode__(), myHandle.name)	

	def test_handle4 (self) :
		myHandle = self.create_handle(username = "", name = "", bio = "")
		self.assertTrue(isInstance(myHandle, Handle))
		self.assertEqual(myHandle.username, "")
		self.assertEqual(myHandle.name, "")
		self.assertEqual(myHandle.bio, "") 




	# ----
	# Hashtag Model
	# ----

	def create_hashtag (self, name, description):
		return Hashtag.objects.create(name = "hashtag", description = "person")

	def test_hashtag1 (self) :
		myHashtag = self.create_hashtag(name = "NBAFinals", description = "NBA playoff finals for Miami Heat vs. San Antonio Spurs")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.name)
		self.assertEqual(myHashtag.__unicode__(), myHashtag.description)

	def test_hashtag2 (self) :
		myHashtag = self.create_hashtag(name = "Cramps", description = "people making fun of Lebron James's game performance")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.name)
		self.assertEqual(myHashtag.__unicode__(), myHashtag.description)


	def test_hashtag3 (self) :
		myHashtag = self.create_hashtag(name = "GoSpursGo", description = "San Antonio Spurs' chant")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.__unicode__(), myHashtag.name)
		self.assertEqual(myHashtag.__unicode__(), myHashtag.description)

	def test_hashtag4 (self) :
		myHashtag = self.create_hashtag(name = "", description = "")
		self.assertTrue(isInstance(myHashtag, Hashtag))
		self.assertEqual(myHashtag.name, "")
		self.assertEqual(myHashtag.description, "")




	# ----
	# Cluster Model
	# ----

	def create_cluster (self, name, parents, description) :
		return Cluster.objects.create(name = "clusterName", parents = "parents", description = "descriptions")

	def test_cluster1 (self) :
		myCluster = self.create_cluster(name = "NBAFinals", parents = "NBA", description = "finals bballz 2014")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.name)
		self.assertEqual(myCluster.__unicode__(), myCluster.parents)
		self.assertEqual(myCluster.__unicode__(), myCluster.description)

	def test_cluster2 (self) :
		myCluster = self.create_cluster(parents = "NBA", description = "finals bballz 2014")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.parents)
		self.assertEqual(myCluster.__unicode__(), myCluster.description)
		self.assertEqual(myCluster.name, "clusterName")		

	def test_cluster3 (self) :
		myCluster = self.create_cluster(name = "NBAFinals", parents = "NBA")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(myCluster.__unicode__(), myCluster.name)
		self.assertEqual(myCluster.__unicode__(), myCluster.parents)
		self.assertEqual(myCluster.description, "descriptions")	

	def test_cluster4 (self) :
		myCluster = self.create_cluster(name = "", parents = "", description = "")
		self.assertTrue(isInstance(myCluster, Cluster))
		self.assertEqual(name, "")
		self.assertEqual(parents, "")
		self.assertEqual(description, "")



# ----
# main
# ----

setup_test_environment()
#main()
