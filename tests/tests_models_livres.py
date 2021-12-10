from django.test import TestCase

from tests_views_livres import Livres


class LivresTestCase(TestCase):

    def setUp(self):
        Livres.objects.create(
            nome="Livres"
        )


def test_retorno_str(self):
    p1 = Livres.objects.get(nome='Livres')
    self.assertEquals(p1.__str__(), 'Livres')
