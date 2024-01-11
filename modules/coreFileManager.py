import json, os


def newFile(**param):
    with open(param['DB'],'w') as db:
        json.dump(param['data'],db,indent=2)

def checkFile(**param):
    if (os.path.isfile(param['DB'])):
        param['data'].update(loadFile(DB = param['DB']))
    else:
        newFile(DB = param['DB'], data = param['data'])

def loadFile(**param):
    with open(param['DB'],'r') as db:
        return json.load(db)

def addData(**param):
    datos = loadFile(DB = param['DB'])
    with open(param['DB'],'r+') as db:
        db.seek(0)
        datos.update(param['data'])
        json.dump(datos,db,indent=4)

def deleteData(**param):
    pass