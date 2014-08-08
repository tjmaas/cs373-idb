from django.test import TestCase
from haystack.query import SearchQuerySet
from .models import State,Park,Hike
from django.core.management import call_command
from django.test.utils import setup_test_environment
from django.test.utils import override_settings
class HaystackTestCase(TestCase) :
    multi_db = True
    def setUp(self) :
        setup_test_environment()
        with self.settings(HAYSTACK_CONNECTIONS = {
                            'default': {
                            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
                            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
                            'INCLUDE_SPELLING': True,
                            },})
        call_command('rebuild_index',interactive=False)

    #     tx = State.objects.create(name = "Texas",
    #                               date_founded = "12/12/1212",
    #                               flag = "www.google.com",
    #                               population = 1000,
    #                               size = 10,
    #                               video = "myvideourl")
    #     tx.save()
    #     p = Park.objects.create(
		  #  name = "Big Bend",
		  #  state = tx,
		  #  size = 0,
		  #  max_elevation = 9999,
		  #  date_founded = "1/1/2000",
		  #  park_image = "www.amazon.com",
		  #  num_visitors = 42,
		  #  video = "ThisIsAVideo")
    #     p.save()


    #     h = Hike.objects.create (
    #         name = "Forest Loop",
    #         distance = 1,
    #         est_time = 60,
    #         hike_image = "pretty trees",
    #         difficulty = "Moderate",
    #         park = p )
    #     h.save()




    def test_state_query (self) :
        texas = 'Texas'
        sqs = SearchQuerySet().auto_query(texas)
        tx  = State.objects.get(pk=sqs[0].pk)
        print (tx.name)
        self.assertEqual(sqs.count(),1)
        # self.assertEqual(sqs[0].verbose_name,'State')

        # self.assertEqual(tx.name.lower(),tx)

    def test_park_query (self) :

        park = 'big bend'
        sqs = SearchQuerySet().filter(content=park)
        self.assertEqual(sqs.count(),1)
        self.assertEqual(sqs[0].verbose_name,'Park')
        bb_park = Park.objects.get(pk=sqs[0].pk)
        self.assertEqual(bb_park.lower(),park)

    def test_hike_query (self) :
        hike = 'forest loop'
        sqs = SearchQuerySet().filter(content=hike)
        self.assertEqual(sqs.count(),1)
        self.assertEqual(sqs[0].verbose_name,'Hike')
        hike = Hike.objects.get(pk=sqs[0].pk)
        self.assertEqual(hike.name.lower(), hike)
        self.assertEqual(hike.difficulty,sqs[0].difficulty)

    def test_hike_to_park_query (self) :
        hike = 'rock creek'
        sqs = SearchQuerySet().filter(content=hike)
        self.assertEqual(sqs.count(),1)
        self.assertEqual(sqs[0].verbose_name,'Hike')
        hike = Hike.objects.get(pk=sqs[0].pk)
        self.assertEqual(hike.name.lower(), hike)
        self.assertEqual(hike.difficulty,sqs[0].difficulty)

        self.assertTrue(hike._meta.get_field('park').rel.to,Park)
        park = 'glacier bay'
        gb = Park.objects.get(pk=hike.park.pk)
        self.assertEqual(gb.name.lower(),park)





