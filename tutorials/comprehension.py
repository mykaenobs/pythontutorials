# LIST COMPREHENSIONS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [i for i in numbers if i%2==0]
odds = [i for i in numbers if i%3==0]
sqrt = [i*i for i in numbers]

print(evens)
print(f'odd numbers {odds}')
print(f'sqare numbers {sqrt}')



#  SET COMPREHENSIONS
numbers = set([1, 2, 1, 3, 4, 2]) # this kind of set clean the list if there are duplicate results
evens = {i for i in numbers if i%2==0}
print(f'Sets {numbers}')
print(f'Sets evens numbers {evens}')


# DIC COMPREHENSIONS
cities = ['Mumbai', 'New York', 'Paris']
countries = ['India', 'USA', 'France']

z = zip(cities, countries)
for c in z:
    print(c)

d = {
    city: country for city, country in zip(cities, countries) 
}

print(f'Countries to their capitals {d}')