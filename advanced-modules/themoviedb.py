import requests
import json


class theMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/'
        self.api_key = '1cf7652c5c47756e21cbaeef39d30e12'
        
    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getSearch(self,search):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={search}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSeçim: ")
    
    if secim == '3':
        break
    
    elif secim == '1':
        ## json data =  ## json data == https://api.themoviedb.org/3/movie/popular?api_key=1cf7652c5c47756e21cbaeef39d30e12&language=en-US&page=1
        movies = movieApi.getPopulars()
        for movie in movies['results']:
            print(movie['title']) # name bilgisini alır
            
    elif secim == '2':
        search = input("Aratmak istediğiniz Kelimeyi Giriniz : ")
        movies = movieApi.getSearch(search)
        for movie in movies['results']:
            print(movie['name'])
            
    