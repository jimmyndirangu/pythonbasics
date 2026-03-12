# list datastructure features
# ordered.
# indexed.
# changeable.

names=["Jimmy","Jane","Mary","Victor","Ishmael"]
names.append("Samuel")
names.insert(1,"Alma")
print(names)
names[0]="Peter"
print(f"My name is {names[0]}")


# tuples datasructure features
# ordered.
# indexed.
# unchangeble.
country=("Kenya","Somalia","Burundi","Uganda","Tanzania")
# country[3]="Euthopia"
print(country)
print(f"I was born in {country[0]}")

# set datastructure features
#unordered.
# no index.
cars={"Mazda","Subaru","Mercedes","Toyota","Porsche","Nissan"}
print(cars)


# dictionary datastructure features
# key value pair 
# changeable
staff={"name":"Lookie", "Age":28, "Salary":"Ksh.200000"}
print(f"Employee name is {staff["name"]}")
print(f"Employee age is {staff["Age"]}")