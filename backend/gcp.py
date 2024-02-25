import os
import pymongo
import json
import random
import hashlib
import time

import requests

from hashlib import sha256



def hashthis(st):


    hash_object = hashlib.md5(st.encode())
    h = str(hash_object.hexdigest())
    return h



def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()



    receiver_public_key = os.environ.get('ownpublic')

    mongostr = os.environ.get('MONGOSTR')
    client = pymongo.MongoClient(mongostr)
    db = client["insomna"]


    retjson = {}

    action = request_json['action']




    if action == "resetsamplesnore":
        col = db.snores

        found = 0
        count = 0
        id = "0" ##can change this

        id = request_json['dayid']
        user = request_json['userid']

        for x in col.find():
            if x['id'] == id and x['userid'] == user:
                found = 1
                id = x['id']
                count = x['count']

            break
        if found == 0:
            retjson['status'] = "unknown  id"
            retjson['userid'] = user
            

            return json.dumps(retjson)
        


        col.update_one({"id": id}, {"$set":{"count":0}})

        retjson['status'] = "snores reset"

        return json.dumps(retjson)




    if action == "addsnore":
        col = db.snores

        found = 0
        count = 0
        id = "0" ##can change this

        id = request_json['dayid']
        user = request_json['userid']

        for x in col.find():
            if x['id'] == id and x['userid'] == user:
                found = 1
                id = x['id']
                count = x['count']

            break
        if found == 0:
            retjson['status'] = "unknown  id"
            retjson['userid'] = user
            

            return json.dumps(retjson)
        


        col.update_one({"id": id}, {"$set":{"count":count+1}})

        retjson['status'] = "snores updated"

        return json.dumps(retjson)




    if action == "addreading":
        
        col = db.sampledata
        
        if request_json['type'] == "live":
            col = db.livedata
        
        maxid=1

        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        payload = {}

        uid = id 
        payload["id"] = id

        payload["name"] = request_json['name']
        payload["value"] = request_json['value']
        payload['userid'] = request_json['userid']


        payload["ts"] = str(int(time.time()))
        
        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added reading"
        retjson['reading id'] = id

        return json.dumps(retjson)        



    if action == "getallreadings":

        col = db.sampledata
        
        if request_json['type'] == "live":
            col = db.livedata


        data = []

        for x in col.find():
            ami = {}
            ami["id"] = x["id"]
            ami["name"] = x["name"]
            ami["value"] = x["value"]
            ami["userid"] = x["userid"]
            ami["timestamp"] = x["ts"]
            data.append(ami)

        retjson['readings'] = data

        return json.dumps(retjson)



    if action == "getuserdata":
        col = db.users
        for x in col.find():
            if int(x['id']) == int(request_json['userid']):
                name = x['name']
                utype = x['type']
                age = x['age']
                gender = x['gender']


                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['name'] = name
                retjson['type'] = utype                
                retjson['age'] = age
                retjson['gender'] = gender
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)


    if action == "updateuserdata":
        col = db.users
        for x in col.find():
            if int(x['id']) == int(request_json['id']):
                if 'name' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"name":request_json['name']}})
                if 'gender' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"gender":request_json['gender']}})
                if 'type' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"type":request_json['type']}})
                    
                # status = x['status']
                # diet = x['diet']
                # allergy = x['allergy']

                retjson = {}

                # retjson['dish'] = userid
                retjson['responsestatus'] = "success"
                # retjson['status'] = status
                # retjson['diet'] = diet
                # retjson['allergy'] = allergy
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)



    if action == "getallmemes":
        col = db.memes
        tables = []
        for x in col.find():
            table = {}

            table['memeid'] = x['id']
            table['url'] = x['url']
            table['userid'] = x['userid']
            table['text'] = x['text']

            tables.append(table)

            


        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "success"
        retjson['tables'] = tables
        

        return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)



    if action == "register" :
        maxid = 1
        col = db.users
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        payload = {}

        uid = id 
        payload["id"] = id
        # payload["uid"] = request_json['uid']
        # payload["name"] = request_json['name']
        payload["name"] = request_json['name']
        payload["email"] = request_json['email']
        payload["password"] = request_json['password']
        if "age" in request_json:
            payload["age"] = request_json['age']
        else:
            payload["age"] = "-1"
        if "gender" in request_json:
            payload["gender"] = request_json['gender']
        else:
            payload["gender"] = "great things happen after 2am"
        
        payload["type"] = request_json['type']
        
        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['userid'] = id

        return json.dumps(retjson)


    if action == "login":
        col = db.users
        for x in col.find():
            if x['email'] == request_json['email'] and x['password'] == request_json['password']:
                userid = x['id']
                name = x['name']
                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['name'] = name
                retjson['userid'] = userid
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['userid'] = "-1"

        return json.dumps(retjson)


    if action == "nothing":


        retjson = {}
         # retjson['dish'] = userid
        retjson['status'] = "nothing was done"

        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
