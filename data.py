import os
import urllib
import json

# url = 'http://tester@localhost:8088/api/data/'
data_url = 'http://thedatahub.org/api/data/4faaef85-3b22-4ebb-ad28-fcc6bd4f5f3d'
metadata_url = 'http://thedatahub.org/api/data/fffc6388-01bc-44c4-ba0d-b860d93e6c7c' 

# localhost
# data_url = 'http://localhost:8088/api/data/874e6e14-b392-48cb-9ec6-3941deeb2b98'

series_data_csv = 'https://docs.google.com/spreadsheet/pub?key=0AogGMvffTHrgdFFjQy1qVWJGT1IteEhPallQbGlpbmc&single=true&gid=4&output=csv'
metadata_csv = 'https://docs.google.com/spreadsheet/pub?key=0AogGMvffTHrgdFFjQy1qVWJGT1IteEhPallQbGlpbmc&single=true&gid=1&output=csv'

from datastore.client import DataStoreClient

def data():
    # get the latest
    urllib.urlretrieve(series_data_csv, 'data/series-data.csv')
    print 'Retrieved latest data'

    client = DataStoreClient(data_url)
    client.delete()
    print 'Delete done'

    #mapping = json.load(open('data/mapping.json'))
    #client.mapping_update(mapping)

    client.upload('data/series-data.csv')
    print 'uploaded'

def metadata():
    urllib.urlretrieve(metadata_csv, 'data/series-metadata.csv')
    print 'Retrieved latest data'

    client = DataStoreClient(metadata_url)
    client.delete()
    print 'Delete done'

    client.upload('data/series-metadata.csv')
    print 'uploaded'


if __name__ == '__main__':
    metadata()
    data()

