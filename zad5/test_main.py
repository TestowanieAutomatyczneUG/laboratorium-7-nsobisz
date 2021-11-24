from main import Meal
import unittest


class MealTest(unittest.TestCase):

    def setUp(self):
        self.temp = Meal()

    def test_meal_by_id(self):
        self.assertEqual(self.temp.get_meal_by_id(52772), {'Nazwa': 'Teriyaki Chicken Casserole', 'Kategoria': 'Chicken', 'Przepis': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!'})
    def test_meal_by_id_2(self):
        self.assertEqual(self.temp.get_meal_by_id(52770), {'Nazwa': 'Spaghetti Bolognese', 'Kategoria': 'Beef', 'Przepis': 'Put the onion and oil in a large pan and fry over a fairly high heat for 3-4 mins. Add the garlic and mince and fry until they both brown. Add the mushrooms and herbs, and cook for another couple of mins.\r\n\r\nStir in the tomatoes, beef stock, tomato ketchup or purée, Worcestershire sauce and seasoning. Bring to the boil, then reduce the heat, cover and simmer, stirring occasionally, for 30 mins.\r\n\r\nMeanwhile, cook the spaghetti in a large pan of boiling, salted water, according to packet instructions. Drain well, run hot water through it, put it back in the pan and add a dash of olive oil, if you like, then stir in the meat sauce. Serve in hot bowls and hand round Parmesan cheese, for sprinkling on top.'})

    def test_meal_by_id_wrong_number(self):
        self.assertRaises(Exception, self.temp.get_meal_by_id, -7)
    def test_meal_by_id_wrong_type_1(self):
        self.assertRaises(Exception, self.temp.get_meal_by_id, 1.1)

    def test_meal_by_id_wrong_type_2(self):
        self.assertRaises(Exception, self.temp.get_meal_by_id, {})

    def test_meal_by_name(self):
        self.assertEqual(self.temp.get_meal_by_name("Arrabiata"), {'Nazwa': 'Spicy Arrabiata Penne', 'Kategoria': 'Vegetarian', 'Przepis': 'Bring a large pot of water to a boil. Add kosher salt to the boiling water, then add the pasta. Cook according to the package instructions, about 9 minutes.\r\nIn a large skillet over medium-high heat, add the olive oil and heat until the oil starts to shimmer. Add the garlic and cook, stirring, until fragrant, 1 to 2 minutes. Add the chopped tomatoes, red chile flakes, Italian seasoning and salt and pepper to taste. Bring to a boil and cook for 5 minutes. Remove from the heat and add the chopped basil.\r\nDrain the pasta and add it to the sauce. Garnish with Parmigiano-Reggiano flakes and more basil and serve warm.'})



    def test_meal_by_name_2(self):
        self.assertEqual(self.temp.get_meal_by_name("Spaghetti Bolognese"), {'Nazwa': 'Spaghetti Bolognese', 'Kategoria': 'Beef', 'Przepis': 'Put the onion and oil in a large pan and fry over a fairly high heat for 3-4 mins. Add the garlic and mince and fry until they both brown. Add the mushrooms and herbs, and cook for another couple of mins.\r\n\r\nStir in the tomatoes, beef stock, tomato ketchup or purée, Worcestershire sauce and seasoning. Bring to the boil, then reduce the heat, cover and simmer, stirring occasionally, for 30 mins.\r\n\r\nMeanwhile, cook the spaghetti in a large pan of boiling, salted water, according to packet instructions. Drain well, run hot water through it, put it back in the pan and add a dash of olive oil, if you like, then stir in the meat sauce. Serve in hot bowls and hand round Parmesan cheese, for sprinkling on top.'})

    def test_meal_by_name_wrong_str(self):
        self.assertRaises(Exception, self.temp.get_meal_by_name, "d")
    def test_meal_by_name_wrong_type_1(self):
        self.assertRaises(Exception, self.temp.get_meal_by_name, 1.1)

    def test_meal_by_name_wrong_type_2(self):
        self.assertRaises(Exception, self.temp.get_meal_by_name, [8])

    def test_meals_by_first_letter(self):
        self.assertEqual(self.temp.get_meals_by_first_letter("a"),
                         ['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik', 'Ayam Percik'])

    def test_meals_by_first_letter_wrong_str(self):
        self.assertRaises(Exception, self.temp.get_meals_by_first_letter, "dsadasdasda")

    def test_meals_by_first_letter_wrong_type_1(self):
        self.assertRaises(Exception, self.temp.get_meals_by_first_letter, 1.1)

    def test_meals_by_first_letter_wrong_type_2(self):
        self.assertRaises(Exception, self.temp.get_meals_by_first_letter, {})

    def test_meals_by_category(self):
        self.assertEqual(self.temp.get_meals_by_category("Seafood"),
                         ['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish fofos', 'Fish pie', 'Fish Stew with Rouille', 'Garides Saganaki', 'Grilled Portuguese sardines', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns', 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Mee goreng mamak', 'Nasi lemak', 'Portuguese fish stew (Caldeirada de peixe)', 'Recheado Masala Fish', 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà', 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Spring onion and prawn empanadas', 'Three Fish Pie', 'Tuna and Egg Briks', 'Tuna Nicoise']
)

    def test_meals_by_category_wrong_str(self):
        self.assertRaises(Exception, self.temp.get_meals_by_category, "d")

    def test_meals_by_category_wrong_type_1(self):
        self.assertRaises(Exception, self.temp.get_meals_by_category, 1)

    def test_meals_by_category_wrong_type_2(self):
        self.assertRaises(Exception, self.temp.get_meals_by_category, {})

    def test_meals_by_area(self):
            self.assertEqual(self.temp.get_meals_by_area("Canadian"),
                             ['BeaverTails', 'Breakfast Potatoes', 'Canadian Butter Tarts', 'Montreal Smoked Meat', 'Nanaimo Bars', 'Pate Chinois', 'Pouding chomeur', 'Poutine', 'Rappie Pie', 'Split Pea Soup', 'Sugar Pie', 'Timbits', 'Tourtiere']

                             )

    def test_meals_by_area_wrong_str(self):
            self.assertRaises(Exception, self.temp.get_meals_by_area, "d")

    def test_meals_by_area_wrong_type_1(self):
            self.assertRaises(Exception, self.temp.get_meals_by_area, [3,4])

    def test_meals_by_area_wrong_type_2(self):
            self.assertRaises(Exception, self.temp.get_meals_by_area, 3.4)

    def test_meals_for_vegan(self):
            self.assertEqual(self.temp.get_meals_for_vegan(),
                             ['Roast fennel and aubergine paella', 'Vegan Chocolate Cake', 'Vegan Lasagna']
                             )
    def test_meals_for_average_chicken_fan(self):
            self.assertEqual(self.temp.get_meals_for_average_chicken_fan(),
                             ['Brown Stew Chicken', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Handi', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Thai Green Curry']

                             )
    def test_meals_for_average_asian_cuisine_enjoyer(self):
            self.assertEqual(self.temp.get_meals_for_average_asian_cuisine_enjoyer(),
                             ['Beef Lo Mein', 'Chicken Congee', 'Egg Drop Soup', "General Tso's Chicken", 'Hot and Sour Soup', 'Kung Pao Chicken', 'Kung Po Prawns', 'Ma Po Tofu', 'Shrimp Chow Fun', 'Sweet and Sour Pork', 'Szechuan Beef', 'Wontons', 'Chicken Karaage', 'Honey Teriyaki Salmon', 'Japanese gohan rice', 'Japanese Katsudon', 'Katsu Chicken curry', 'Teriyaki Chicken Casserole', 'Tonkatsu pork', 'Yaki Udon', 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber', 'Vietnamese Grilled Pork (bun-thit-nuong)', 'Massaman Beef curry', 'Pad See Ew', 'Thai Green Curry']

                             )



    def tearDown(self):
        self.temp = None