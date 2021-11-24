
import json
import requests

class Meal:
    def get_meal_by_name(self, name):
        if type(name)!=str:
            raise Exception("Nazwa musi być stringiem")
        elif len(name)<2:
            raise Exception("Długość słowa musi być większa niż 1")
        else:
            r = requests.get("http://www.themealdb.com/api/json/v1/1/search.php?s="+name)
            js = r.json()
            wynik = { "Nazwa": js['meals'][0]['strMeal'], "Kategoria": js['meals'][0]['strCategory'], "Przepis": js['meals'][0]['strInstructions']}
            return wynik

    def get_meal_by_id(self, number):
        if type(number)!=int:
            raise Exception("Podaj liczbę")
        elif number<0:
            raise Exception("Podaj liczbę wiekszą/równą od 0")
        else:
            r = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + str(number))
            js = r.json()
            wynik = {"Nazwa": js['meals'][0]['strMeal'], "Kategoria": js['meals'][0]['strCategory'],
                     "Przepis": js['meals'][0]['strInstructions']}
            return wynik

    def get_meals_by_first_letter(self, letter):
        if type(letter)!=str:
            raise Exception("Nazwa musi być stringiem")
        elif len(letter)!=1:
            raise Exception("Długość słowa musi być równa 1")
        else:
            r = requests.get("http://www.themealdb.com/api/json/v1/1/search.php?f="+letter)
            js = r.json()
            wynik = []
            for i in js['meals']:
                wynik.append(i['strMeal'])
            return wynik


    def get_meals_by_category(self, name):
        if type(name)!=str:
            raise Exception("Nazwa musi być stringiem")
        elif len(name)<2:
            raise Exception("Długość słowa musi być większa niż 1")
        else:
            r = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=" + name)
            js = r.json()
            wynik = []
            for i in js['meals']:
                wynik.append(i['strMeal'])
            return wynik

    def get_meals_by_area(self, name):
        if type(name)!=str:
            raise Exception("Nazwa musi być stringiem")
        elif len(name)<2:
            raise Exception("Długość słowa musi być większa niż 1")
        else:
            r = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=" + name)
            js = r.json()
            wynik = []
            for i in js['meals']:
                wynik.append(i['strMeal'])
            return wynik




    def get_meals_for_vegan(self):
        r = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=vegan")
        js = r.json()
        wynik = []
        for i in js['meals']:
            wynik.append(i['strMeal'])
        return wynik

    def get_meals_for_average_chicken_fan(self):
        r = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?i=chicken")
        js = r.json()
        wynik = []
        for i in js['meals']:
            wynik.append(i['strMeal'])
        return wynik

    def get_meals_for_average_asian_cuisine_enjoyer(self):
        r1 = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=Chinese")
        r2 = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=Japanese")
        r3 = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=Vietnamese")
        r4 = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=Thai")
        js1 = r1.json()
        js2 = r2.json()
        js3 = r3.json()
        js4 = r4.json()
        wynik = []
        for i in js1['meals']:
            wynik.append(i['strMeal'])
        for i in js2['meals']:
            wynik.append(i['strMeal'])
        for i in js3['meals']:
            wynik.append(i['strMeal'])
        for i in js4['meals']:
            wynik.append(i['strMeal'])
        return wynik


