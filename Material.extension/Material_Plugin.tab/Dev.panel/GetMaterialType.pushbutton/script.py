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
    # target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/target_script.py'
    # print(call_other_script(target_environment_python, target_script, 'London'))

    material_list = ["WAL_Concrete_RF"]

    volume_of_materials_in_beams = {material:get_volume_of_material_in_component(doc, material, "beams") for material in material_list}
    volume_of_materials_in_columns = {material:get_volume_of_material_in_component(doc, material, "columns") for material in material_list}
    volume_of_materials_in_floors = {material:get_volume_of_material_in_component(doc, material, "floors") for material in material_list}
    volume_of_materials_in_foundations = {material:get_volume_of_material_in_component(doc, material, "foundations") for material in material_list}
    volume_of_materials_in_walls = {material:get_volume_of_material_in_component(doc, material, "walls") for material in material_list}



    print(volume_of_materials_in_beams)
    print(volume_of_materials_in_columns)
    print(volume_of_materials_in_floors)
    print(volume_of_materials_in_foundations)
    print(volume_of_materials_in_walls)



    
    



    



    
   