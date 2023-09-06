# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

brand = {"name": "Zara", 
         "creation_date": 1975, 
         "creator_name": "Amancio Ortega Gaona", 
         "types_of_clothes": ["men", "women", "children", "home"], "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 7000, 
         "major_color": 
             {"France": "blue", 
              "Spain": "red", 
              "US": ["pink", "green"]}}

brand["number_stores"] = 2

print("Zara's clients are")
for clothing_type in brand["types_of_clothes"]:
    print(clothing_type)

brand["country_creation"] = "Spain"

brand["international_competitors"].append("Desigual")

del brand["creation_date"]
last_comp = brand["international_competitors"][-1]

print("the final international competitor is ", last_comp)

us_clr = brand["major_color"]["US"]
print("major clothes colors in the US are", us_clr)

entries = len(brand)
print("number of pairs in this dictionary are: ", entries)

keys = brand.keys()
key_list = list(keys)
print(key_list)

more_on_zara = {"creation_date": 1975, "number_stores": 10000}

brand.update(more_on_zara)
print(brand)