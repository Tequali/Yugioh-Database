from django.test import TestCase
from Django_Yugioh_Database.add_precise_effects import main
from apps.Yugioh_Database.models import Effect
from apps.Yugioh_Database.enums import EffectTypeOptions

# Create your tests here.


class ModelTestCase(TestCase):
    def setUp(self):
        # create effect types so generation of cards can be done
        list_of_effect_categories: list = EffectTypeOptions.options()
        for effect_category in list_of_effect_categories:
            obj = Effect.objects.create(effect_type=effect_category)
            print(f"The following effect category has been created: {effect_category}")
        self.effects = Effect.objects.all().values()
        return super().setUp()

    def test_addition_of_precise_effects(self):
        success = main()
        self.assertTrue(success)
