import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if type(category) not in [int,str]:
        return None
    
    if type(category) is int:
        sql = (f"SELECT film.title, language.name as languge, category.name as category\
             FROM language\
             INNER JOIN film ON language.language_id = film.language_id\
             INNER JOIN film_category ON film.film_id = film_category.film_id\
             INNER JOIN category ON film_category.category_id = category.category_id\
             WHERE category.category_id = {category}\
             ORDER BY film.title, language.name")
        
    if type(category) is str:
        category = "'" + category + "'"
        
        sql = (f"SELECT film.title, language.name as languge, category.name as category\
             FROM language\
             INNER JOIN film ON language.language_id = film.language_id\
             INNER JOIN film_category ON film.film_id = film_category.film_id\
             INNER JOIN category ON film_category.category_id = category.category_id\
             WHERE category.name = {category}\
             ORDER BY film.title, language.name")
    
    result = pd.read_sql(sql, con=connection)
    return result
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if type(category) not in [int,str]:
        return None
    
    if type(category) is int:
        sql = (f"SELECT film.title, language.name as languge, category.name as category\
             FROM language\
             INNER JOIN film ON language.language_id = film.language_id\
             INNER JOIN film_category ON film.film_id = film_category.film_id\
             INNER JOIN category ON film_category.category_id = category.category_id\
             WHERE category.category_id = {category}\
             ORDER BY film.title, language.name")
        
    if type(category) is str:
        category = "'" + category + "'"
        
        sql = (f"SELECT film.title, language.name as languge, category.name as category\
             FROM language\
             INNER JOIN film ON language.language_id = film.language_id\
             INNER JOIN film_category ON film.film_id = film_category.film_id\
             INNER JOIN category ON film_category.category_id = category.category_id\
             WHERE category.name ~* {category}\
             ORDER BY film.title, language.name")
    
    result = pd.read_sql(sql, con=connection)
    return result
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if type(title) is not str:
        return None
    
    title = "'" + title + "'"
    
    sql = (f"SELECT actor.first_name, actor.last_name\
             FROM actor\
             INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id\
             INNER JOIN film ON film_actor.film_id = film.film_id\
             WHERE film.title = {title}\
             ORDER BY actor.last_name, actor.first_name")
    
    result = pd.read_sql(sql, con=connection)
           
    return result
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    
    if type(words) is not list:
        return None
    
    words_string = f"'( |^)({words[0]}"
    for word in words[1:]:
        words_string += f"|{word}"
    words_string += ")+( |$)'"
    
    sql = f"SELECT title FROM film WHERE title ~* {words_string} ORDER BY title"
    
    result = pd.read_sql(sql, con=connection)
    
    return result