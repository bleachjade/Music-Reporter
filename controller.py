import sys
from flask import abort
from pymongo import MongoClient
from config import OPENAPI_AUTOGEN_DIR, DB_Client

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

client = MongoClient(DB_Client)
mydb = client['Song']


def get_song():
    # print(" i got called")
    # return "test"
    collection = mydb["Genius"]
    for col in collection.find():
        result = col['response']['hits'][0]['result']['title']
        return models.SongDetail(result)

print(get_song())


# def get_basin_details(basinId):
#     cs = db.cursor()
#     cs.execute("SELECT basin_id,name,area FROM basin WHERE basin_id=%s",[basinId])
#     result = cs.fetchone()
#     cs.close()
#     if result:
#         basin_id,name,area = result
#         return models.BasinFull(basin_id,name,area)
#     else:
#         abort(404)


# def get_stations(basinId):
#     cs = db.cursor()
#     cs.execute("SELECT station_id,ename FROM station WHERE basin_id=%s",[basinId])
#     result = [models.StationShort(id,name) for id,name in cs.fetchall()]
#     cs.close()
#     return result


# def get_station_details(stationId):
#     return "Do something"
