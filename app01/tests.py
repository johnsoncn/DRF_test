from django.test import TestCase

# Create your tests here.

from app01 import models, serializers

p1 = models.Publisher.objects.first()
print(p1)
