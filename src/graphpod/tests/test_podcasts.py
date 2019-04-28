from graphene.test import Client
from django.test import TestCase
from podcasts.schema import schema


class PodcastTestCase(TestCase):


    def test_get_podcasts():
        client = Client(schema)
        executed = client.execute('''
        query {
            podcasts {
                id
            }
        } 
        ''')
        assert executed == {
            'data': {
                'podcasts'
            }
        }

