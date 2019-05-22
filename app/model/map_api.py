from typing import List
import requests


class MapAPI:
    """Geolocation related queries using Bing Maps"""

    api_key = 'AgbLx7MM3w4fWXeLTg3rzlPLk5st6bK2gk81-wcmHmWvpopWvDVBVIZIm-p1BbUD'
    base_url = 'http://dev.virtualearth.net/REST/v1/'

    @staticmethod
    def get_search_suggestions(query: str) -> List[dict]:
        """Based on a query return a list of similar real life locations as suggestions."""
        query = MapAPI.base_url + 'Locations/Sweden+' + query + '?o=json&key=' + MapAPI.api_key
        response = requests.get(query.replace(" ", "+")).json()

        if len(response['resourceSets']) == 0:
            return []

        results = []
        for res in response['resourceSets'][0]['resources']:
            if set(('name', 'point', 'address')).issubset(res):
                entry = {
                    'name': res['name'],
                    'latitude': res['point']['coordinates'][0],
                    'longitude': res['point']['coordinates'][1],
                    'district': ""
                }

                address = res['address']
                if set(('adminDistrict', 'adminDistrict2')).issubset(address):
                    entry['district'] = "- " + address[
                        'adminDistrict'] + ', ' + address['adminDistrict2']

                results.append(entry)

        return results
