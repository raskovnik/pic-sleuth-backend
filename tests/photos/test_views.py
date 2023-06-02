import pytest
from django.urls import reverse
from django.http import HttpResponse
from django.test import RequestFactory
from pic_sleuth.photos.views import HelloView

from django.conf import settings
settings.configure()


class TestHelloView:
    def test_hello_view_with_get(self):
        factory = RequestFactory()
        request = factory.get(reverse("hello"))
        response = HelloView()

        assert response.status_code == 200
        assert response.content.decode() == "Hello, World!"

