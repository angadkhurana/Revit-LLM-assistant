#! python3
__title__ = 'wassup'
__author__  = 'angad'
__doc__ = """random"""


from Autodesk.Revit.DB import *

import subprocess
from pyrevit import  DB

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
from snippets.selection import get_selected_elements, call_other_script, is_terrace, is_wall, floor_area


# from bs4 import BeautifulSoup 
import subprocess

if __name__ == '__main__':

    target_environment_python = 'C:/Users/angad/anaconda3/envs/revit_llm_env/python.exe'
    target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/qwerty.py'
    #print(call_other_script(target_environment_python, target_script, 'London'))

    # print(are_walls_surrounding_floor(doc))

    elements = get_selected_elements(uidoc)
    materials = FilteredElementCollector(doc).OfClass(Material).ToElements()
    x = doc.GetElement(elements[0].GetMaterialIds(False)[0])
    print(x.MaterialCategory)
    print(x.MaterialClass)
    print(x.Name)
    # are_walls_surrounding_floor(doc)
    
   