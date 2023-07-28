#import test case
from django.test import TestCase

#import the models from your Django project
from main_app.models import Plant

class PlantTest(TestCase):

    def test_create_plant(self):
        plant = Plant.objects.create(
            name='Tomato',
            type='vegetable',
            description='',
            color='red',
            season='any',
            sun='full',
            temp_min=50,
            temp_ideal=75,
            temp_max=100,
            spacing_x_min=1,
            spacing_x_max=2,
            spacing_y_min=3,
            spacing_y_max=None,
            height_min=None,
            height_max=None,
            width_min=None,
            width_max=None,
            depth_min=None,
            depth_max=None,
            germination_min=None,
            germination_max=None,
            harvest_min=None,
            harvest_max=None,
            days_to_transplant_min=None,
            days_to_transplant_max=None,
            )
        self.assertEqual(plant.name, 'Tomato')
        self.assertEqual(plant.type, 'vegetable')
        self.assertEqual(plant.description, '')
        self.assertEqual(plant.color, 'red')
        self.assertEqual(plant.season, 'any')
        self.assertEqual(plant.sun, 'full')
        self.assertEqual(plant.temp_min, 50)
        self.assertEqual(plant.temp_ideal, 75)
        self.assertEqual(plant.temp_max, 100)
        self.assertEqual(plant.spacing_x_min, 1)
        self.assertEqual(plant.spacing_x_max, 2)
        self.assertEqual(plant.spacing_y_min, 3)
        self.assertEqual(plant.spacing_y_max, None)
        self.assertEqual(plant.height_min, None)
        self.assertEqual(plant.height_max, None)
        self.assertEqual(plant.width_min, None)
        self.assertEqual(plant.width_max, None)
        self.assertEqual(plant.depth_min, None)
        self.assertEqual(plant.depth_max, None)
        self.assertEqual(plant.germination_min, None)
        self.assertEqual(plant.germination_max, None)
        self.assertEqual(plant.harvest_min, None)
        self.assertEqual(plant.harvest_max, None)
        self.assertEqual(plant.days_to_transplant_min, None)
        self.assertEqual(plant.days_to_transplant_max, None)

    def test_get_plant_by_name(self):
        plant = Plant.objects.create(name='Tomato', type='vegetable')
        plant2 = Plant.objects.get(name='Tomato')
        self.assertEqual(plant, plant2)

    def test_create_plant_missing_name(self):
        with self.assertRaises(ValueError):
            plant = Plant.objects.create(name='', type='vegetable')

    def test_create_plant_missing_type(self):
        with self.assertRaises(ValueError):
            plant = Plant.objects.create(name='Tomato', type='')