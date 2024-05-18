# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *
import subprocess
from pyrevit import  DB

# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory



uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_all_walls(doc):
    walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
    return walls

def get_all_columns(doc):
    structural_type_filter = DB.ElementStructuralTypeFilter(DB.Structure.StructuralType.Column)
    collector = DB.FilteredElementCollector(doc).WherePasses(structural_type_filter)
    structural_columns = list(collector)
    return structural_columns

def get_all_beams(doc):
    structural_type_filter = DB.ElementStructuralTypeFilter(DB.Structure.StructuralType.Beam)
    collector = DB.FilteredElementCollector(doc).WherePasses(structural_type_filter)
    structural_beams = list(collector)
    return structural_beams

def get_all_floors(doc):
    floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()
    return floors

def get_all_foundations(doc):
    foundations = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFoundation).WhereElementIsNotElementType().ToElements()
    return foundations

def get_material_id_by_name(doc, mat_name):
    mat_name = "Post-Tensioned Concrete Beams" # Replace with the actual material name

    # Get all materials in the document
    materials = FilteredElementCollector(doc).OfClass(Material).ToElements()

    # Find the material with the given name
    for mat in materials:
        if mat.Name == mat_name:
            mat_id = mat.Id
            print(f"The ID of the material '{mat_name}' is: {mat_id}")
            break
    else:
        print(f"Material with name '{mat_name}' not found in the current document.")

def get_selected_elements(uidoc):
    return [uidoc.Document.GetElement(x) for x in uidoc.Selection.GetElementIds()]


def get_selected_elements_ids(uidoc):
    return uidoc.Selection.GetElementIds()


def is_wall(element):
    # Check if the element is a wall
    if element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Walls):
        return True
    else:
        return False



def call_other_script(target_environment_python, target_script, input):
    # Build the command to run the script in the target environmentr
    command = [target_environment_python, target_script,input]

    # Use subprocess to run the command
    try:
        result = subprocess.run(command, capture_output=True, check=True)
        return "Command Output: " + str(result.stdout)


        # # Print the return code
        # print("Return Code:", result.returncode)
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"##
