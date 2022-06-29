# Exercise 1
students = ['Candace', 'Thomas', 'Jessie', 'Essence', 'Jacky', 'Davis']
# print(students[1])
# print(students[-1])

# Exercise 2
foods = ('corn dogs', 'spaghetti', 'curry chicken', 'lentil stew', 'garlic knots', 'sushi')
# for food in foods:
#     print(f'{food} is a good food')

# Exercise 3
for food in foods:
    if food == foods[-2] or food == foods[-1]:
        print(food)  #narrow down

# Exercise 4
home_town = {
    'city': 'Radford',
    'state': 'Virginia',
    'population': '17,833'
}

# print(f"I was born in {home_town.get('city')}, {home_town.get('state')}- population of {home_town.get('population')}")

# Exercise 5
for key, value in home_town.items():
    print(key, value)

# Exercise 6
cohort = []
for idx, student in enumerate(students):
    # print(foods[idx])
    # print(student)
    cohort.append({"student": student, "fav_food": foods[idx]})
# print(cohort)

# Exercise 7
awesome_students = [f"{s} is awesome" for s in students]
# print(awesome_students)

# Exercise 8
a_in_foods = [f for f in foods if 'a' in f]
# print(a_in_foods)