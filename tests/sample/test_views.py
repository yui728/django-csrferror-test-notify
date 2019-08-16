from django.test.testcases import TestCase
from django.urls import reverse

class SampleViewTest(TestCase):
    def test_get_index_01(self):
        # print('acccess_url={}'.format(reverse('sample:index')))
        response = self.client.get(reverse('sample:index'))
        self.assertTemplateUsed(response, 'sample/index.html')

    def test_post_index_01(self):
        response = self.client.post(reverse('sample:index'), data={})
        self.assertTemplateUsed(response, 'sample/index.html')

    def test_post_index_02(self):
        response = self.client.post(reverse('sample:index'), data={'message': 'Test Message'})
        self.assertRedirects(response, reverse('sample:index'))