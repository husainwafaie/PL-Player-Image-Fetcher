import requests

url = 'https://footballapi.pulselive.com/football/players'

params = {
    'pageSize': 20,
    'compSeasons': 578,
    'altIds': True,
    'page': 0,
    'type': 'player',
    'id': -1,
    'compSeasonId': 578
}