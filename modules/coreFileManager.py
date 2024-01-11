import json, os


def newFile(**param):
    with open(param['DB'],'w') as db:
        json.dump(param['data'],db,indent=2)

def checkFile(**param):
    if (os.path.isfile(param['DB'])):
        param['data'] = loadFile(DB = param['DB'])
    else:
        newFile(DB = param['DB'], data = param['data'])

def loadFile(**param):
    with open(param['DB'],'r') as db:
        return json.load(db)