import sys, os
from json import load
PLAY = "►"
PAUSE = "||"
STOP = "■"

def listFromFile(file):
    try:
        with open(file, 'r', encoding="utf-8") as fileData:
            settings = load(fileData)
            return {"instruction": settings["instruction"], "description": settings["description"]} 
    except:
        raise Exception(f"Falha ao abrir o arquivo {file}")
def resourcePath(relativePath):
    """Retorna o caminho relativo ao indicado por referencia"""
    basePath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(basePath, relativePath)

def isFile(path):
    return os.path.isfile(path)

def pathExists(path):
    return os.path.exists(path)