from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Booking(models.Model):
    """ Model for drf APP bookings """
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number_regex = RegexValidator(regex=r'^\+?\d{1,3}[-\.\s]?\d{1,14}[-\.\s]?\d{1,14}$')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_seats = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MenuItem(models.Model):
    """ Model for react App menu """

    """ React App menu titles """
    CATEGORY_CHOICES = (
        ('Rainbow_Burgers', 'Rainbow_Burgers'),
        ('No_chicken_Burgers', 'No_chicken_Burgers'),
        ('No_chicken', 'No_chicken'),
        ('Wraps', 'Wraps'),
        ('Wraps_Dressings', 'Wraps_Dressings'),
        ('Accessories', 'Accessories'),
        ('Desserts', 'Desserts'),
        ('Dip', 'Dip'),
        ('Drinks', 'Drinks'),
        ('Add_ons', 'Add_ons'),
        ('Snacks', 'Snacks'),
    )

    """ React Apps menu names """
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
        ('Salad', 'Salad'),
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

    """ React Apps name descriptions """
    DESCRIPTION_CHOICES = (
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('This is one of our favorite burger: Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Note that this burger has all of our toppings: Carrot, Avocado, Paprika, Aubergine, Tomato and Pickled Red Onion -for a tastier outcome', 'This is one of our favorite burger: Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Note that this burger has all of our toppings: Carrot, Avocado, Paprika, Aubergine, Tomato and Pickled Red Onion -for a tastier outcome'),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Carrots added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Avocado added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Yellow Paprika added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Aubergine added as topping -for a tastier outcome',),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Pickled Red Onion added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome', 'No Cheese and no lactos - Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten and Tomato added as topping -for a tastier outcome'),
        ('No Cheese and no lactos - This is one of our favorite burger: Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Note that this burger has all of our toppings: Carrot, Avocado, Paprika, Aubergine, Tomato and Pickled Red Onion -for a tastier outcome', 'No Cheese and no lactos - This is one of our favorite burger: Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Note that this burger has all of our toppings: Carrot, Avocado, Paprika, Aubergine, Tomato and Pickled Red Onion -for a tastier outcome'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with nice vegitable chicken taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with nice vegitable chicken taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crunchy Potato -for a spicier taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crunchy Potato -for a spicier taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crispy Cauliflower -for a spicier taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crispy Cauliflower -for a spicier taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crispy Union garlic -for a spicier taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with nice crispy Union garlic -for a spicier taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with Lentil -for a soft, but still spicy Taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Stuffed with Lentil -for a soft, but still spicy Taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh coriander leaves to enhance flavor', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh coriander leaves to enhance flavor'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh tomato slices to enhance flavor', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh tomato slices to enhance flavor'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh onion slices to enhance flavor', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh onion slices to enhance flavor'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh ginger slices to enhance flavor', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Fresh ginger slices to enhance flavor'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Cacao and coconut milk -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Cacao and coconut milk -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Blueberries and coconut milk -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Blueberries and coconut milk -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Vanilla and coconut milk -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Vanilla and coconut milk -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Apples and coconut milk -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Seasoned with Apples and coconut milk -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our ice creams have coconut milk as a base... Seasoned with Cacao -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our ice creams have coconut milk as a base... Seasoned with Cacao -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our ice creams have coconut milk as a base... Seasoned with Strawberries -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our ice creams have coconut milk as a base... Seasoned with Strawberries -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Tomato', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Tomato'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Bearnaise', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Bearnaise'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Mayonnaise', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Mayonnaise'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Garlic', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Garlic'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Sweet and Sour', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base - Seasoned with Sweet and Sour'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base... This dip sause is Seasoned with Jalapenos', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our dip sauces have OatMilk, chickpea spade and tofu as a base... This dip sause is Seasoned with Jalapenos'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Crispy potatos fried in Sunflower oil', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Crispy potatos fried in Sunflower oil'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Mixed salad without allergy-causing substances', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Mixed salad without allergy-causing substances'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oat milk, Tofu and Corn - fresh sweetpotatos', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oat milk, Tofu and Corn - fresh sweetpotatos'),
        ('Fresch Sliced Apples from the plants of Sweden', 'Fresch Sliced Apples from the plants of Sweden'),
        ('Fresch Sliced Ananas imported from Brazil', 'Fresch Sliced Ananas imported from Brazil'),
        ('Fresch Sliced Carrots from the plants of Sweden', 'Fresch Sliced Carrots from the plants of Sweden'),
        ('Fresch Sliced - Salted Pickles from the plants of Sweden', 'Fresch Sliced - Salted Pickles from the plants of Sweden'),
        ('Fresch Sliced - Tomatos from the plants of Sweden', 'Fresch Sliced - Tomatos from the plants of Sweden'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Rice Paper', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Rice Paper'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with Jalapenos', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with Jalapenos'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with a plantbased mozzarella spice', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Tofu and Seasoned with a plantbased mozzarella spice'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oumph and Seasoned with a nice vegitable chicken taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... Based on Oumph and Seasoned with a nice vegitable chicken taste'),
        ('All our sodas comes with a 33cl can and paper straw if asked for - Fanta', 'All our sodas comes with a 33cl can and paper straw if asked for - Fanta'),
        ('All our sodas comes with a 33cl can and paper straw if asked for - Coke', 'All our sodas comes with a 33cl can and paper straw if asked for - Coke'),
        ('All our sodas comes with a 33cl can and paper straw if asked for - Sprite', 'All our sodas comes with a 33cl can and paper straw if asked for - Sprite'),
        ('Fresh Spring water from the source of northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Spring water from the source of northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Oat milk produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Oat milk produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Apple Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Apple Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Fresh Orange Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses', 'Fresh Orange Juice produced by farmers in northern Sweden.. delivered in 33 cl paper glasses'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Strawberries -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Strawberries -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Cacao -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Cacao -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Rosee Hip -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Milk Shakes have coconut milk as a base... Seasoned with Rosee Hip -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Smoothies have coconut milk as a base... Topped with Blueberries -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Smoothies have coconut milk as a base... Topped with Blueberries -for a yummy taste'),
        ('Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Smoothies have coconut milk as a base... Topped with Rose Hip -for a yummy taste', 'Basic Ingredients= Only plants with vegetable oil, no E-topiccs or gluten... All our Smoothies have coconut milk as a base... Topped with Rose Hip -for a yummy taste'),
    )

    title = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30, choices=NAME_CHOICES)
    description = models.TextField(max_length=1000, choices=DESCRIPTION_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, default=User.objects.get(is_superuser=True).pk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
