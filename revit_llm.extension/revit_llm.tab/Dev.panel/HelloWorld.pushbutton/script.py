#! python3
__title__ = 'wassup'
__author__  = 'angad'
__doc__ = """random"""


from Autodesk.Revit.DB import *
import subprocess
from pyrevit import  DB

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
from snippets.selection import get_selected_elements, call_other_script, is_terrace, is_wall


# from bs4 import BeautifulSoup 
import subprocess

if __name__ == '__main__':

    target_environment_python = 'C:/Users/angad/anaconda3/envs/revit_llm_env/python.exe'
    target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/qwerty.py'
    # print(call_other_script(target_environment_python, target_script, '6'))

    # elements = get_selected_elements(uidoc)
    # if is_wall(elements[0]):
    #     print(elements[0].BoundingBox())

    wall_list= FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
    wall_instance = wall_list[0]
    options = Options()
    print(wall_instance.Name)
    print(wall_instance.get_Geometry(options))

    # print(is_wall(get_selected_elements(uidoc)[0]))


    # print(get_selected_elements(uidoc))

    # x = [uidoc.Document.GetElement(x) for x in uidoc.Selection.GetReferences()]
    # print(x[0].Name)
   