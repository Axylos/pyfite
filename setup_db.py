#!/usr/bin/env python3

from pymongo import MongoClient
client = MongoClient()

validator_json = { "$and":
    [
        { 'name': { '$type': "string", '$exists': 'true'} },
        { 'fites': { '$type': 'array', '$exists': 'true' }},
        { 'status': { '$in': ["Pending", "Active", "Inactive"], '$exists': 'true' } },
        { 'votes': { '$type': 'array', '$exists': 'true' } },
    ]
}
db = client['errfite']
db.create_collection("fitelist", validator=validator_json)

