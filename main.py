import argparse
import flickrapi
import random
import math
import json

def random_flickr(args):
    cities = read_cities(args.cities)

    print(cities) 

    flickr = flickrapi.FlickrAPI(args.key, args.secret, format='parsed-json')

    random_city = cities[random.randint(0, len(cities)-1)]

    random_lat = random_city["latitude"] + random.uniform(-1, 1)
    random_long = random_city["longitude"] + random.uniform(-1, 1)

    photos = flickr.photos.search(lat=random_lat, lon=random_long, per_page='10')

    print(random_city["city"])
    print(random_lat, random_long)
    print(photos)

def read_cities(file):
    with open(file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--key', type=str, help='flickr key')
    parser.add_argument('--secret', type=str, help='flickr secret')
    parser.add_argument('--cities', type=str, default='cities.json', help='json of cities')


    args = parser.parse_args()

    random_flickr(args)