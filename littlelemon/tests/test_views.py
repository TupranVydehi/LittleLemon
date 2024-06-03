from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuViewTest(TestCase):
    def setUp(self) -> None:
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Rice", price=50, inventory=200)
        MenuItem.objects.create(title="Dosa", price=30, inventory=150)
    
    def test_getall(self):
        item1 = MenuItem.objects.get(title="IceCream")
        item2 = MenuItem.objects.get(title="Rice")
        item3 = MenuItem.objects.get(title="Dosa")
        self.assertEqual([str(item1), str(item2), str(item3)], ["IceCream : 80.00", "Rice : 50.00", "Dosa : 30.00"])
