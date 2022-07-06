#!/bin/python
from random import choice
import pandas as pd
from jikanpy import Jikan

mal_ids = ["action", "adventure", 3, "comedy", "avant garde", 6, "mystery", "drama", 9, "fantasy", 11, 12, "historical", "horror", 15, 16, 17, 18, 19, "parody", "samurai", "romance", 23, "sci-fi", 25, "girls love", 27, "boys love", 29, "sports", 31, 32, 33, 34, 35, "slice of life", "supernatural", 38, 39, 40, "suspense", 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, "gag humor"]

jikan = Jikan()

anime = pd.read_json("database.json")

seen_anime = open("watched.txt").read().split('\n')

answer = input("Looking for a specific genre?\n")
if answer.lower() == "no":
    valid_anime = list(set(anime.index)-set(seen_anime))
    if len(valid_anime) == 0:
         print("No unseen anime in database, please select a genre to get new anime from.")
         answer = "yes"
    else:
        print(choice(valid_anime))
if answer.lower() == "yes":
    while True:
        genre_list = []
        print("Choose between:")
        print("----------------------------")
        for genre in mal_ids:
            if type(genre) != type(0):
                genre_list.append(genre)
                print(genre)
        print("----------------------------")
        answer = input().lower()
        if answer not in genre_list:
            print("Please choose a valid genre")
        else:
            valid_anime = list(anime[anime['tags'].apply(lambda x: answer in x)].index)
            for anime_name in seen_anime:
                if anime_name in valid_anime:
                    valid_anime.remove(anime_name)
            if len(valid_anime) < 10:
                potentials = jikan.genre(type='anime', genre_id=mal_ids.index(answer)+1)['anime']
                i = 0
                for potential in potentials:
                    if i == 10:
                        break
                    if potential['title'] in seen_anime or potential['title'] in anime.index:
                        continue
                    i += 1
                    potential_genres = []
                    for genre in potential['genres']:
                        potential_genres.append(genre['name'].lower())
                    anime.loc[potential['title']] = [potential_genres, potential['score']]
                    valid_anime.append(potential['title'])
                anime.to_json("database.json")
                
            if len(valid_anime) == 0:
                print("Sorry, no anime in that genre is registered. :(")
                break
            print(choice(valid_anime))
            break
