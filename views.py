from multiprocessing import context
from pyexpat import model
from django.shortcuts import render

# Create your views here.


animals_array = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
]

families_array = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
]

people_array = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def families(request,id):
    familieChoosen = ""
    for familie in families_array:
        if id == familie["id"]:
            familieChoosen = familie
            break

    context = {'familyChoosen':familieChoosen}    

    return render(request,'family.html',context)

def animals(request,id):
    animalsChoosen = ""
    for animal in animals_array:
        if id == animal["id"]:
            animalsChoosen = animal
            break

    context = {'animalsChoosen':animalsChoosen}

    return render(request,'animal.html',context)


# daily challenge 

def sortedPeople(request,age):
    sort_orders = sorted(people_array.items(), key=lambda x: x[1], reverse=True)
    peopleByAge = ""
    for i in sort_orders:
         if age == i[0]:
            peopleByAge = i
            break

    context = {'peopleByAge':peopleByAge}

    return render(request,'people.html',context) 

