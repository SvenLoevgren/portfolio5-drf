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
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome', 'No Cheese and no lactos - Only plants with vegetable oil, no E-topiccs or gluten and All Ingredients added as topping -for a tastier outcome'),
        ('Golden and crispy plant-based nuggets -for a tastier outcome', 'Golden and crispy plant-based nuggets -for a tastier outcome'),
        ('Baked potato stuffed with plant-based ingredients -for a tastier outcome', 'Baked potato stuffed with plant-based ingredients -for a tastier outcome'),
        ('Baked cauliflower stuffed with plant-based ingredients -for a tastier outcome', 'Baked cauliflower stuffed with plant-based ingredients -for a tastier outcome'),
        ('Baked onion garlic stuffed with plant-based ingredients -for a tastier outcome', 'Baked onion garlic stuffed with plant-based ingredients -for a tastier outcome'),
        ('Baked lentil stuffed with plant-based ingredients -for a tastier outcome', 'Baked lentil stuffed with plant-based ingredients -for a tastier outcome'),
        ('Fresh coriander leaves to enhance flavor', 'Fresh coriander leaves to enhance flavor'),
        ('Fresh tomato slices to enhance flavor', 'Fresh tomato slices to enhance flavor'),
        ('Fresh onion slices to enhance flavor', 'Fresh onion slices to enhance flavor'),
        ('Fresh ginger slices to enhance flavor', 'Fresh ginger slices to enhance flavor'),
        ('Delicious chocolate pie for dessert', 'Delicious chocolate pie for dessert'),
        ('Delicious blueberry pie for dessert', 'Delicious blueberry pie for dessert'),
        ('Delicious vanilla pie for dessert', 'Delicious vanilla pie for dessert'),
        ('Delicious apple pie for dessert', 'Delicious apple pie for dessert'),
        ('Creamy chocolate plant-based ice-cream', 'Creamy chocolate plant-based ice-cream'),
        ('Creamy strawberry plant-based ice-cream', 'Creamy strawberry plant-based ice-cream'),
        ('Classic ketchup condiment', 'Classic ketchup condiment'),
        ('Bearnaise sauce made with coconut milk', 'Bearnaise sauce made with coconut milk'),
        ('Mayonnaise made with chickpea-based ingredients', 'Mayonnaise made with chickpea-based ingredients'),
        ('Garlic cloves for an extra kick of flavor', 'Garlic cloves for an extra kick of flavor'),
        ('Sweet and sour sauce for dipping', 'Sweet and sour sauce for dipping'),
        ('Plant-based tofu cheese topping', 'Plant-based tofu cheese topping'),
        ('Spicy seasoning for those who like it hot', 'Spicy seasoning for those who like it hot'),
        ('Crispy and golden french fries', 'Crispy and golden french fries'),
        ('Fresh and nutritious salad', 'Fresh and nutritious salad'),
        ('Fresh Sliced - Salted Pickles from the plants of Sweden', 'Fresh Sliced - Salted Pickles from the plants of Sweden'),
        ('Fresh Sliced - Tomatoes from the plants of Sweden', 'Fresh Sliced - Tomatoes from the plants of Sweden'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Rice Paper', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Rice Paper'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with Jalapenos', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with Jalapenos'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with a plant-based mozzarella spice', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with a plant-based mozzarella spice'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oumph and Seasoned with a nice vegetable chicken Taste.', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oumph and Seasoned with a nice vegetable chicken Taste.'),
        ('All our sodas come with a 33cl can and paper straw if asked for', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('All our sodas come with a 33cl can and paper straw if asked for', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('All our sodas come with a 33cl can and paper straw if asked for', 'All our sodas come with a 33cl can and paper straw if asked for'),
        ('Fresh Spring water from the source of northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Spring water from the source of northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Oat milk produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Oat milk produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Apple Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Apple Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Orange Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Orange Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Strawberries -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Strawberries -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Cacao -for a', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Cacao -for a'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Rose hip -for a unique flavor', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Rose hip -for a unique flavor'),
        ('Fresh Blueberry Smoothie made from handpicked blueberries in northern Sweden', 'Fresh Blueberry Smoothie made from handpicked blueberries in northern Sweden'),
        ('Fresh Rose hip Smoothie made from wild rose hips gathered in the forests of Sweden', 'Fresh Rose hip Smoothie made from wild rose hips gathered in the forests of Sweden'),
    )

    title = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30, choices=NAME_CHOICES)
    description = models.TextField(max_length=1000, choices=DESCRIPTION_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, default=User.objects.get(is_superuser=True).pk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
Keep tuple price data for feature use...
PRICE_CHOICES = (
    (5.99, 5.99),
    (6.49, 6.49),
    (5.79, 5.79),
    (6.99, 6.99),
    (5.89, 5.89),
    (5.59, 5.59),
    (7.99, 7.99),
    (6.49, 6.49),
    (6.99, 6.99),
    (6.49, 6.49),
    (7.29, 7.29),
    (6.19, 6.19),
    (5.99, 5.99),
    (8.49, 8.49),
    (3.33, 3.33),
    (4.99, 4.99),
    (5.49, 5.49),
    (4.79, 4.79),
    (4.99, 4.99),
    (0.99, 0.99),
    (0.49, 0.49),
    (0.39, 0.39),
    (0.59, 0.59),
    (4.99, 4.99),
    (5.29, 5.29),
    (4.79, 4.79),
    (4.49, 4.49),
    (3.99, 3.99),
    (3.99, 3.99),
    (0.29, 0.29),
    (0.89, 0.89),
    (0.79, 0.79),
    (0.49, 0.49),
    (0.69, 0.69),
    (1.49, 1.49),
    (0.39, 0.39),
    (2.49, 2.49),
    (3.99, 3.99),
    (0.11, 0.11),
    (0.11, 0.11),
    (0.13, 0.13),
    (0.13, 0.13),
    (2.39, 2.39),
    (4.40, 4.40),
    (6.50, 6.50),
    (1.10, 1.10),
    (1.10, 1.10),
    (1.10, 1.10),
    (1.00, 1.00),
    (1.00, 1.00),
    (1.00, 1.00),
    (1.00, 1.00),
    (2.00, 2.00),
    (2.00, 2.00),
    (2.00, 2.00),
    (1.50, 1.50),
    (1.50, 1.50),
)


Alo, # for future implementation... Keep availability model!

class Availability(models.Model):
    date = models.DateField()
    time = models.TimeField()
    max_seats_available = models.PositiveIntegerField()
    num_available_seats = models.PositiveIntegerField()
"""
