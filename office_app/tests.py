from django.test import TestCase
from .models import Office
from .models import Person
from .models import WorkHistory

"""
class ProductListViewTests(TestCase):

    def test_product_list_view(self):
        # Create a product
        product = Product.objects.create(name='Laptop', price=1000)

        # Create a request object
        request = self.client.get('/products/')

        # Get the response
        response = product_list(request)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response content
        self.assertContains(response, product.name)
        self.assertContains(response, str(product.price))
"""
print("TODO: delete")

# create multiple methods in a testcase if they share setup and teardown
class XyzViewXyTestCase(TestCase):

    def test_product_list_view(self):
        print("TODO: delete")

print("TODO: # test fixtures have data")
print("TODO: # test that sample API key is loaded from ENV variables")
print("TODO: check that can access https://open-meteo.com/ API")
print("TODO: # Get office info by name and current temperature at this location at the moment")
print("TODO: # Get employees in an office")
print("TODO: # Get employees by first name")
print("TODO: # Get employees by last name")
print("TODO: # Get employees by first name and last name")
print("TODO: # Get employees returns the office where they work and places where they have worked previously")
print("TODO: # Add new employee to an office")
print("TODO: # Update employee’s offices which they have worked at")
print("TODO: # scheduled task to runs every day")
print("TODO: # scheduled task updates the last_checked field with the date on which the task is running")
print("TODO: # scheduled task can be run in batches iterated")

print("TODO: dockerise")


