# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# print(x)
# print(students[0]['last_name'])
# print(sports_directory['soccer'][0])
# print(z[0]['y'])

# 2. Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in range(len(students)):
        print('first_name - ' + students[i]['first_name'] +
              ', ' + 'last_name - ' + students[i]['last_name'])


# iterateDictionary(students)

# 3. Get Values From a List of Dictionaries


def iterateDictionary2(key_name, students):
    for i in range(len(students)):
        print(students[i][key_name])


# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key.upper())
        for i in range(len(dojo[key])):
            print(dojo[key][i])


printInfo(dojo)
