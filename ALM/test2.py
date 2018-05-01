# from tinydb import TinyDB, where,Query
# db = TinyDB('db.json')
# # db.insert({'casenumber': 1})
# # db.insert({'casenumber': 2})
#
# CN = Query()
# print(db.search(CN.casenumber == 3))

from datetime import datetime, timedelta

hourago=datetime.now() - timedelta(hours = 1)
print(hourago)
print(str(hourago).rpartition(':')[0])

