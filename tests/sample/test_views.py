from django.test.testcases import TestCase
from django.urls import reverse
from django.test.client import Client

class SampleViewTest(TestCase):

    def _pre_setup(self):
        super()._pre_setup()
        self.client = Client(enforce_csrf_checks=True)

    def test_get_index_01(self):
        response = self.client.get(reverse('sample:index'))
        self.assertTemplateUsed(response, 'sample/index.html')

    def test_post_index_01(self):
        response = self.client.post(reverse('sample:index'), data={})
        # If csrf_token was template given.
        # self.assertTemplateUsed(response, 'sample/index.html')
        # If csrf_token was't template given.
        self.assertEquals(403, response.status_code)

    def test_post_index_02(self):
        response = self.client.post(reverse('sample:index'), data={'message': 'Test Message'})
        # If csrf_token was template given.
        # self.assertRedirects(response, reverse('sample:index'))
        # If csrf_token was't template given.
        self.assertEquals(403, response.status_code)