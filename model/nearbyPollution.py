import extractGeolocation

import requests

def overpassRequest(body):
    result = requests.post("https://overpass-api.de/api/interpreter", data=body)
    return result.text

# takes a geotagged image file and returns a score from 0 to 10 on nearby
# pollution, from distance to close roads
def nearbyPollution(imageLocation):
    geolocation = extractGeolocation.extractGeolocation(imageLocation)
    if (geolocation[0] != 0.0 and geolocation[1] != 0.0):
        print(geolocation)
        overpass = overpassRequest(f"""
            <query type="way">
                <has-kv k="highway" regv="motorway|trunk|primary|motorway_link|trunk_link|primary_link"/>
                <around lat="{geolocation[0]}" lon="{geolocation[1]}" radius="250"/>
            </query>
            <union>
                <item/>
                <recurse type="down"/>
            </union>
            <print/>
        """)
        numberOfWays = overpass.count('way')
        return 10-2**(3.3-0.005 * numberOfWays)
    else:
        return 0

print(nearbyPollution("C:/Users/sebas/Downloads/Photos/IMG_20241019_121612143.jpg"))
print(nearbyPollution("C:/Users/sebas/Downloads/Photos/IMG_20241019_120511313.jpg"))
print(nearbyPollution("C:/Users/sebas/Downloads/Photos/MVIMG_20230317_213244.jpg"))