import requests
import json

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  """
  #constants
  API_KEY = '3KuGd18Jt2pFK1xXj44zGA==tuRW35T7QHTvzoml'
  BASE_URL = 'https://api.api-ninjas.com/v1/animals'

  url = f'{BASE_URL}?name={animal_name}'
  headers ={
    'X-Api-Key':API_KEY
  }
  response = requests.get(url,headers=headers)
  animals = response.json()
  return animals

