from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


##Codigo basado de https://www.geeksforgeeks.org/get-post-requests-using-python/
def index(request):


    # api-endpoint
    URL = "https://rickandmortyapi.com/api/episode/"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()

    #data es un diccionario!
    chapters = []

    ##RECOLECTAMOS DATOS DE LA PRIMERA PAGINA
    for tupla in data['results']:
        chapter = {}
        chapter['id'] = tupla['id']
        chapter['name'] = tupla['name']
        chapter['air_date'] = tupla['air_date']
        chapter['episode'] = tupla['episode']
        chapters.append(chapter)


    ##SI QUEDAN MÁS PAGINAS SEGUIMOS
    current_page = data['info']['next']
    while current_page!= '':
        r = requests.get(url=current_page)
        data = r.json()
        for tupla in data['results']:
            chapter = {}
            chapter['id'] = tupla['id']
            chapter['name'] = tupla['name']
            chapter['air_date'] = tupla['air_date']
            chapter['episode'] = tupla['episode']
            chapters.append(chapter)
        current_page = data['info']['next']
    context = {'latest_question_list': chapters}
    return render(request, 'rick/index.html', context)


def details_chapter(request, id_capitulo):
    # api-endpoint
    URL = "https://rickandmortyapi.com/api/episode/{}".format(id_capitulo)

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()

    personajes = data["characters"]

    single_episode = {}
    single_episode["name"]=(data["name"])
    single_episode["air_date"]=(data["air_date"])
    single_episode["episode"]=(data["episode"])
    todos = []
    for p in personajes:
        personaje = {}
        info_personaje = requests.get(url = p).json()
        personaje["id"] = info_personaje["id"]
        personaje["name"]= info_personaje["name"]
        todos.append(personaje)
    single_episode["characters"] = todos

    context = {'information': single_episode}
    return render(request, 'rick/details_chapter.html', context)


def details_character(request, id_character):
    # api-endpoint
    URL = "https://rickandmortyapi.com/api/character/"+str(id_character)

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()

    info = data

    lugares ={}

    lugar= {}
    lugar["name"] = info["location"]["name"]

    if lugar['name'] == 'unknown':
        lugar['id'] = 0
    else:
        lugar["id"] = requests.get(url=info["location"]["url"]).json()["id"]




    lugares["lugar"]=lugar

    origin = {}
    origin["name"] = info["origin"]["name"]


    if origin['name'] == 'unknown':
        origin['id'] = 0
    else:
        origin["id"] = requests.get(url=info["origin"]["url"]).json()["id"]

    lugares["origin"] = origin

    chapters = []
    for tupla in data['episode']:
        chapter = {}
        p = requests.get(url=tupla).json()
        chapter['id'] = p['id']
        chapter['name'] = p['name']
        chapter['air_date'] = p['air_date']
        chapter['episode'] = p['episode']
        chapters.append(chapter)


    context = {'information': info,
               "lugares":lugares,
               "chapters":chapters}


    return render(request, 'rick/details_character.html', context)



def details_location(request, id_location):
    # api-endpoint
    URL = "https://rickandmortyapi.com/api/location/{}".format(id_location)

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()

    info = data


    residents=[]
    for p in info["residents"]:
        personaje = {}
        info_personaje = requests.get(url = p).json()
        personaje["id"] = info_personaje["id"]
        personaje["name"]= info_personaje["name"]
        residents.append(personaje)



    context = {'information': info,
               "residents":residents,}


    return render(request, 'rick/details_location.html', context)



def search(request):

    variable = request.GET["name"]
    variable = str(variable)



    ##episodios
    URL = "https://rickandmortyapi.com/api/episode/"
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    # extracting data in json format
    data = r.json()
    chapters = []
    for tupla in data['results']:
        chapter = {}
        chapter['id'] = tupla['id']
        chapter['name'] = tupla['name']
        chapter['air_date'] = tupla['air_date']
        chapter['episode'] = tupla['episode']
        chapters.append(chapter)

        ##SI QUEDAN MÁS PAGINAS SEGUIMOS
    current_page = data['info']['next']
    while current_page != '':
        r = requests.get(url=current_page)
        data = r.json()
        for tupla in data['results']:
            chapter = {}
            chapter['id'] = tupla['id']
            chapter['name'] = tupla['name']
            chapter['air_date'] = tupla['air_date']
            chapter['episode'] = tupla['episode']
            chapters.append(chapter)
        current_page = data['info']['next']

    # PERSONAJES

    URL = "https://rickandmortyapi.com/api/character/"
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    # extracting data in json format
    data = r.json()
    characters = []
    for tupla in data['results']:
        chapter = {}
        chapter['id'] = tupla['id']
        chapter['name'] = tupla['name']
        characters.append(chapter)

        ##SI QUEDAN MÁS PAGINAS SEGUIMOS
    current_page = data['info']['next']
    while current_page != '':
        r = requests.get(url=current_page)
        data = r.json()
        for tupla in data['results']:
            chapter = {}
            chapter['id'] = tupla['id']
            chapter['name'] = tupla['name']
            characters.append(chapter)
        current_page = data['info']['next']

    ##LUGARES
    URL = "https://rickandmortyapi.com/api/location/"
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    # extracting data in json format
    data = r.json()
    locations = []
    for tupla in data['results']:
        chapter = {}
        chapter['id'] = tupla['id']
        chapter['name'] = tupla['name']
        locations.append(chapter)

        ##SI QUEDAN MÁS PAGINAS SEGUIMOS
    current_page = data['info']['next']
    while current_page != '':
        r = requests.get(url=current_page)
        data = r.json()
        for tupla in data['results']:
            chapter = {}
            chapter['id'] = tupla['id']
            chapter['name'] = tupla['name']
            locations.append(chapter)
        current_page = data['info']['next']


    resultados_characters = []
    for char in characters:
       # print("COMPRANDO VARIABLE {} CON {}".format(variable,char["name"]))
        if char["name"].lower().find(variable)!=-1:
            resultados_characters.append(char)

    resultados_chapters = []
    for chapt in chapters:
        if  chapt["name"].lower().find(variable) != -1:
            resultados_chapters.append(chapt)

    resultados_locations = []
    for loc in locations:
        if  loc["name"].lower().find(variable) != -1:
            resultados_locations.append(loc)





    context = {'characters': resultados_characters,
               "locations":resultados_locations,
               "chapters":resultados_chapters}

    return render(request, 'rick/search.html', context)
