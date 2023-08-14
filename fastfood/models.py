from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number_regex = RegexValidator(regex=r'^\+?\d{1,3}[-\.\s]?\d{1,14}[-\.\s]?\d{1,14}$')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_seats = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('Rainbow Burgers', 'Rainbow Burgers'),
        ('No chicken Burgers', 'No chicken Burgers'),
        ('No chicken', 'No chicken'),
        ('Wraps', 'Wraps'),
        ('Wraps Dressings', 'Wraps Dressings'),
        ('Accessories', 'Accessories'),
        ('Desserts', 'Desserts'),
        ('Dip', 'Dip'),
        ('Drinks', 'Drinks'),
        ('Add-ons', 'Add-ons'),
        ('Snacks', 'Snacks'),
    )

    NAME_CHOICES = (
        ('Aurantius (Carrot)', 'Aurantius (Carrot)'),
        ('Chiorus (Avocado)', 'Chiorus (Avocado)'),
        ('Flavus (Paprika)', 'Flavus (Paprika)'),
        ('Purpureus (Aubergine)', 'Purpureus (Aubergine)'),
        ('Roseus (pickled red onion)', 'Roseus (pickled red onion)'),
        ('Ruber (Tomato)', 'Ruber (Tomato)'),
        ('Brunus (all ingredients)', 'Brunus (all ingredients)'),
        ('NC Aurantius (Carrot)', 'NC Aurantius (Carrot)'),
        ('NC Chiorus (Avocado)', 'NC Chiorus (Avocado)'),
        ('NC Flavus (Paprika)', 'NC Flavus (Paprika)'),
        ('NC Purpureus (Aubergine)', 'NC Purpureus (Aubergine)'),
        ('NC Roseus (pickled red onion)', 'NC Roseus (pickled red onion)'),
        ('NC Ruber (Tomato)', 'NC Ruber (Tomato)'),
        ('NC Brunus (all ingredients)', 'NC Brunus (all ingredients)'),
        ('Nuggets', 'Nuggets'),
        ('Stuffed Potato', 'Stuffed Potato'),
        ('Stuffed Cauliflower', 'Stuffed Cauliflower'),
        ('Stuffed Union garlic', 'Stuffed Union garlic'),
        ('Stuffed Lentil', 'Stuffed Lentil'),
        ('Coriander', 'Coriander'),
        ('Tomato', 'Tomato'),
        ('Onion', 'Onion'),
        ('Ginger', 'Ginger'),
        ('Chocolate pie', 'Chocolate pie'),
        ('Blueberry pie', 'Blueberry pie'),
        ('Vanilla pie', 'Vanilla pie'),
        ('Apple pie', 'Apple pie'),
        ('Chocolate Ice-cream', 'Chocolate Ice-cream'),
        ('Strawberry Ice-cream', 'Strawberry Ice-cream'), 
        ('Ketchup', 'Ketchup'),
        ('Bearnaise (coco milk)', 'Bearnaise (coco milk)'),
        ('Mayonnaise (chickpea)', 'Mayonnaise (chickpea)'),
        ('Carlic', 'Carlic'),
        ('Sweat-n-Sour', 'Sweat-n-Sour'),
        ('Cheese (Tofu)', 'Cheese (Tofu)'),
        ('Spicy', 'Spicy'),
        ('French Fries', 'French Fries'),
        ('Salad', 'Salad'),  # last updates
        ('Pickles', 'Pickles'),
        ('Tomatos', 'Tomatos'),
        ('Bacon (Rice paper)', 'Bacon (Rice paper)'),
        ('Cheese (Tofu)', 'Cheese (Tofu)'),
        ('Chili cheese (Tofu)', 'Chili cheese (Tofu)'),
        ('Mozzarella Buns (Tofu)', 'Mozzarella Buns (Tofu)'),
        ('Hot wings (Oumph)', 'Hot wings (Oumph)'),
        ('Fanta', 'Fanta'),
        ('Coca-Cola', 'Coca-Cola'),
        ('Sprite', 'Sprite'),
        ('Water', 'Water'),
        ('Milk (Oat)', 'Milk (Oat)'),
        ('Juice (Apple)', 'Juice (Apple)'),
        ('Juice (Orange)', 'Juice (Orange)'),
        ('Strawberry shake (Coco milk)', 'Strawberry shake (Coco milk)'),
        ('Chocolate shake (Coco milk)', 'Chocolate shake (Coco milk)'),
        ('Rose hip shake (Coco milk)', 'Rose hip shake (Coco milk)'),
        ('Smoothie (Blueberry)', 'Smoothie (Blueberry)'),
        ('smoothie (Rose hip)', 'smoothie (Rose hip)'),
    )

    DESCRIPTION_CHOICES = (
        ('Aurantius (Carrot)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('Chiorus (Avocado)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('Flavus (Paprika)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('Purpureus (Aubergine)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome'),
        ('Roseus (pickled red onion)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('Ruber (Tomato)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('Brunus (all ingredients)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome'),
        ('NC Aurantius (Carrot)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('NC Chiorus (Avocado)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('NC Flavus (Paprika)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('NC Purpureus (Aubergine)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome'),
        ('NC Roseus (pickled red onion)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('NC Ruber (Tomato)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('NC Brunus (all ingredients)', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome'),
        ('Nuggets', 'Golden and crispy plant-based nuggets -for a tastier outcome'),
        ('Stuffed Potato', 'Baked potato stuffed with plant-based ingredients -for a tastier outcome'),
        ('Stuffed Cauliflower', 'Baked cauliflower stuffed with plant-based ingredients -for a tastier outcome'),
        ('Stuffed Union garlic', 'Baked onion garlic stuffed with plant-based ingredients -for a tastier outcome'),
        ('Stuffed Lentil', 'Baked lentil stuffed with plant-based ingredients -for a tastier outcome'),
        ('Coriander', 'Fresh coriander leaves to enhance flavor'),
        ('Tomato', 'Fresh tomato slices to enhance flavor'),
        ('Onion', 'Fresh onion slices to enhance flavor'),
        ('Ginger', 'Fresh ginger slices to enhance flavor'),
        ('Chocolate pie', 'Delicious chocolate pie for dessert'),
        ('Blueberry pie', 'Delicious blueberry pie for dessert'),
        ('Vanilla pie', 'Delicious vanilla pie for dessert'),
        ('Apple pie', 'Delicious apple pie for dessert'),
        ('Chocolate Ice-cream', 'Creamy chocolate plant-based ice-cream'),
        ('Strawberry Ice-cream', 'Creamy strawberry plant-based ice-cream'),
        ('Ketchup', 'Classic ketchup condiment'),
        ('Bearnaise (coco milk)', 'Bearnaise sauce made with coconut milk'),
        ('Mayonnaise (chickpea)', 'Mayonnaise made with chickpea-based ingredients'),
        ('Carlic', 'Garlic cloves for an extra kick of flavor'),
        ('Sweat-n-Sour', 'Sweet and sour sauce for dipping'),
        ('Cheese (Tofu)', 'Plant-based tofu cheese topping'),
        ('Spicy', 'Spicy seasoning for those who like it hot'),
        ('French Fries', 'Crispy and golden french fries'),
        ('Salad', 'Fresh and nutritious salad'),
        ('Pickles', 'Fresh Sliced - Salted Pickles from the plants of Sweden'),
        ('Tomatoes', 'Fresh Sliced - Tomatoes from the plants of Sweden'),
        ('Bacon (Rice paper)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Rice Paper'),
        ('Cheese (Tofu)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu'),
        ('Chili cheese (Tofu)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with Jalapenos'),
        ('Mozzarella Buns (Tofu)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with a plant-based mozzarella spice'),
        ('Hot wings (Oumph)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oumph and Seasoned with a nice vegetable chicken Taste.'),
        ('Fanta', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('Coca-Cola', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('Sprite', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('Water', 'Fresh Spring water from the source of northern Sweden.. delivered in 33 cl paper glasses'),
        ('Milk (Oat)', 'Fresh Oat milk produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Juice (Apple)', 'Fresh Apple Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Juice (Orange)', 'Fresh Orange Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Strawberry shake (Coco milk)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Strawberries -for a yummy taste'),
        ('Chocolate shake (Coco milk)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Cacao -for a'),
        ('Rose hip shake (Coco milk)', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Rose hip -for a unique flavor'),
        ('Smoothie (Blueberry)', 'Fresh Blueberry Smoothie made from handpicked blueberries in northern Sweden'),
        ('Smoothie (Rose hip)', 'Fresh Rose hip Smoothie made from wild rose hips gathered in the forests of Sweden'),
    )

    title = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30, choices=NAME_CHOICES)
    description = models.CharField(max_length=1000, choices=DESCRIPTION_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, default=User.objects.get(is_superuser=True).pk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
Keep tuple price data for feature use...
    PRICE_CHOICES = (
        ('Aurantius (Carrot)', 5.99),
        ('Chiorus (Avocado)', 6.49),
        ('Flavus (Paprika)', 5.79),
        ('Purpureus (Aubergine)', 6.99),
        ('Roseus (pickled red onion)', 5.89),
        ('Ruber (Tomato)', 5.59),
        ('Brunus (all ingredients)', 7.99),
        ('NC Aurantius (Carrot)', 6.49),
        ('NC Chiorus (Avocado)', 6.99),
        ('NC Flavus (Paprika)', 6.49),
        ('NC Purpureus (Aubergine)', 7.29),
        ('NC Roseus (pickled red onion)', 6.19),
        ('NC Ruber (Tomato)', 5.99),
        ('NC Brunus (all ingredients)', 8.49),
        ('Nuggets', 3.33),
        ('Stuffed Potato', 4.99),
        ('Stuffed Cauliflower', 5.49),
        ('Stuffed Union garlic', 4.79),
        ('Stuffed Lentil', 4.99),
        ('Coriander', 0.99),
        ('Tomato', 0.49),
        ('Onion', 0.39),
        ('Ginger', 0.59),
        ('Chocolate pie', 4.99),
        ('Blueberry pie', 5.29),
        ('Vanilla pie', 4.79),
        ('Apple pie', 4.49),
        ('Chocolate Ice-cream', 3.99),
        ('Strawberry Ice-cream', 3.99),
        ('Ketchup', 0.29),
        ('Bearnaise (coco milk)', 0.89),
        ('Mayonnaise (chickpea)', 0.79),
        ('Carlic', 0.49),
        ('Sweat-n-Sour', 0.69),
        ('Cheese (Tofu)', 1.49),
        ('Spicy', 0.39),
        ('French Fries', 2.49),
        ('Salad', 3.99),
    )

Alo, # for future implementation... Keep availability model!

class Availability(models.Model):
    date = models.DateField()
    time = models.TimeField()
    max_seats_available = models.PositiveIntegerField()
    num_available_seats = models.PositiveIntegerField()
"""
