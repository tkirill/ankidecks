import dbm

import requests
from pydantic_core import ValidationError

from ankigen.skell.models import SkellConcordanceResponse


class SkellClient:

    def __init__(self):
        self.cache = dbm.open('skell_cache', 'c')

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def close(self):
        self.cache.close()
    
    def search(self, query: str) -> SkellConcordanceResponse:
        cached = self.cache.get(query)
        if cached is not None:
            response_text = cached
        else:
            data = {
                'query': query,
                'lang': 'English',
                'format': 'json'
            }
            headers = {
                "Accept": "*/*",
                "Accept-Language": "en-US;q=0.8,en;q=0.7",
                "Priority": "u=1, i",
                "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                'Referer': "https://skell.sketchengine.eu/",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            }
            print('SKEll query:', query)
            response = requests.get('https://skell.sketchengine.eu/api/concordance', params=data, headers=headers)
            assert response.status_code == 200
            print('SKEll response success')
            response_text = response.text
            self.cache[query] = response_text
        try:
            model = SkellConcordanceResponse.model_validate_json(response_text)
            return model
        except ValidationError:
            print(response_text)
            raise