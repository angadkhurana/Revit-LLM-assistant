#! python3
__title__ = 'wassup'
__author__  = 'angad'
__doc__ = """random"""


from Autodesk.Revit.DB import *

import subprocess
from pyrevit import  DB

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
from snippets.selection import *


# from bs4 import BeautifulSoup 
import subprocess

if __name__ == '__main__':

    # target_environment_python = 'C:/Users/angad/anaconda3/envs/revit_llm_env/python.exe'
    # target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/qwerty.py'
    # print(call_other_script(target_environment_python, target_script, 'London'))

    walls = get_all_walls(doc)
    print("num walls", len(walls))

    beams = get_all_beams(doc)
    print(beams)

    columns = get_all_columns(doc)
    print(columns)

    column_filter = DB.ElementStructuralTypeFilter(DB.Structure.StructuralType.Wall)
    collector = DB.FilteredElementCollector(doc).WherePasses(column_filter)
    columns = list(collector)
    print("walls2")
    print(len(columns))
    print("HUMMD")



    
   