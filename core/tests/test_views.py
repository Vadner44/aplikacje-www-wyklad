"""View tests."""
# Django
from django.test import TestCase
from django.urls import reverse

from core.tests.factories import BunnyFactory, BreedingFarmFactory


class ViewTest(TestCase):
    """Test cases."""

    def setUp(self) -> None:  # noqa: D102
        self.breeding_farm = BreedingFarmFactory()
        self.bunny = BunnyFactory(breeding_farm = self.breeding_farm)

    def test_bunny_view(self):
        response = self.client.get(reverse('bunny:bunny'))
        self.assertEqual(response.status_code, 200)

    def test_bunny_view_with_filtering(self):
        response = self.client.get(reverse('bunny:bunny'), {'name': self.bunny.name})
        self.assertEqual(response.status_code, 200)

    def test_breeding_farm_view(self):
        response = self.client.get(reverse('bunny:breeding-farm'))
        self.assertEqual(response.status_code, 200)

    def test_breeding_farm_view_with_filtering(self):
        response = self.client.get(reverse('bunny:breeding-farm'), {'name': self.breeding_farm.name})
        self.assertEqual(response.status_code, 200)

    def test_create_bunny_no_authenticated(self):
        response = self.client.post(reverse('bunny:create-bunny'), {})
        self.assertEqual(response.status_code, 401)

    def test_bunny_view_post_method(self):
        response = self.client.post(reverse('bunny:bunny'))
        self.assertEqual(response.status_code, 405)
