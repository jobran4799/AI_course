# START

dict_israel = {'name': 'Israel', 'birth': 1948, 'population_millions': 9.3,
               'capital': 'jerusalem', 'language': 'Hebrew',
               'cities': ['jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
               'currency': 'ILS', 'area_Kilometer': 22145, 'gdb_billion': 450}

print("Capital:", dict_israel.get('capital'))
print("Keys:", dict_israel.keys())
print("Values:", dict_israel.values())
print("Items:")
for key, value in dict_israel.items():
    print(f"{key}: {value}")

dict_copy = dict_israel.copy()
print("New dictionary copied:", dict_copy)
dict_copy.pop("gdb_billion")

dict_other = dict.fromkeys(dict_israel.keys())

dict_other['name'] = input("Enter country name: ")
dict_other['birth'] = int(input("Enter year of birth: "))
dict_other['population_millions'] = float(input("Enter population in millions: "))
dict_other['capital'] = input("Enter capital city: ")
dict_other['language'] = input("Enter primary language: ")
dict_other['cities'] = [
    input("Enter city 1: "),
    input("Enter city 2: "),
    input("Enter city 3: ")
]
dict_other['currency'] = input("Enter currency: ")
dict_other['area_kilometer'] = int(input("Enter area in kilometers: "))
dict_other['gdp_billion'] = float(input("Enter GDP in billion: "))

print("Updated dictionary with user input:", dict_other)
# END
