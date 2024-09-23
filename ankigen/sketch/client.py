import dbm
import json

import requests
from pydantic_core import ValidationError

from ankigen.sketch.models import SketchConcordanceResponse


class SketchClient:

    def __init__(self):
        self.cache = dbm.open('sketch_cache', 'c')

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def close(self):
        self.cache.close()
    
    def search(self, query: str) -> SketchConcordanceResponse:
        cached = self.cache.get(query)
        if cached is not None:
            response_text = cached
        else:
            params = {
                'corpname': 'preloaded/bawe2',
                'default_attr': 'lemma',
                'attrs': 'word',
                'refs': '=text.genre',
                'attr_allpos': 'all',
                'viewmode': 'sen',
                'cup_hl': 'q',
                'structs': 's,g',
                'fromp': 1,
                'pagesize': 1000,
                'kwicleftctx': '100#',
                'kwicrightctx': '100#',
                'json': f'{{"concordance_query":[{{"queryselector":"cqlrow","cql":{json.dumps(query)},"default_attr":"lemma"}},{{"q":"e300"}}]}}'
            }
            data = {
                'results_url': r'https://app.sketchengine.eu/#concordance?corpname=preloaded%2Fbawe2&tab=advanced&queryselector=cql&attrs=word&viewmode=kwic&attr_allpos=all&refs_up=0&shorten_refs=1&glue=1&gdex_enabled=1&gdexcnt=300&show_gdex_scores=0&itemsPerPage=20&structs=s%2Cg&refs=%3Dtext.genre&default_attr=lemma&cql=%5Blemma%3D%22afford%22%5D%20%5Blemma%3D%22to%22%5D%20%5Btag%3D%22V.*%22%5D&showresults=1&showTBL=0&tbl_template=&gdexconf=&f_tab=basic&f_showrelfrq=1&f_showperc=0&f_showreldens=0&f_showreltt=0&c_customrange=0&t_attr=&t_absfrq=0&t_trimempty=1&t_threshold=5&operations=%5B%7B%22name%22%3A%22cql%22%2C%22arg%22%3A%22%5Blemma%3D%5C%22afford%5C%22%5D%20%5Blemma%3D%5C%22to%5C%22%5D%20%5Btag%3D%5C%22V.*%5C%22%5D%22%2C%22query%22%3A%7B%22queryselector%22%3A%22cqlrow%22%2C%22cql%22%3A%22%5Blemma%3D%5C%22afford%5C%22%5D%20%5Blemma%3D%5C%22to%5C%22%5D%20%5Btag%3D%5C%22V.*%5C%22%5D%22%2C%22default_attr%22%3A%22lemma%22%7D%2C%22id%22%3A3720%7D%5D&showresults=1'
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
                'Referer': "https://app.sketchengine.eu/",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            }
            response = requests.post('https://app.sketchengine.eu/bonito/run.cgi/concordance', params=params, headers=headers)
            assert response.status_code == 200
            response_text = response.text
            self.cache[query] = response_text
        try:
            model = SketchConcordanceResponse.model_validate_json(response_text)
            return model
        except ValidationError:
            print(response_text)
            raise