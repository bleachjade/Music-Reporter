import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

db = mysql.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD,db=DB_NAME)


def get_basins():
    cs = db.cursor()
    cs.execute("SELECT basin_id,name FROM basin")
    result = [models.BasinShort(id,name) for id,name in cs.fetchall()]
    cs.close()
    return result


def get_basin_details(basinId):
    cs = db.cursor()
    cs.execute("SELECT basin_id,name,area FROM basin WHERE basin_id=%s",[basinId])
    result = cs.fetchone()
    cs.close()
    if result:
        basin_id,name,area = result
        return models.BasinFull(basin_id,name,area)
    else:
        abort(404)


def get_stations(basinId):
    cs = db.cursor()
    cs.execute("SELECT station_id,ename FROM station WHERE basin_id=%s",[basinId])
    result = [models.StationShort(id,name) for id,name in cs.fetchall()]
    cs.close()
    return result


def get_station_details(stationId):
    return "Do something"
