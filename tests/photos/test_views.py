from django.urls import reverse
from django.test import RequestFactory
from pic_sleuth.photos.views import HelloView


class TestHelloView:
    def test_hello_view_with_get(self):
        factory = RequestFactory()
        request = factory.get(reverse("hello"))
        response = HelloView(request)

        assert response.status_code == 200
        assert response.content.decode() == "Hello, World!"
