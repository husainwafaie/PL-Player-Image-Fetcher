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

headers = {
    'Accept': 'application/json',
    'Origin': 'https://www.premierleague.com',
    'Referer': 'https://www.premierleague.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}