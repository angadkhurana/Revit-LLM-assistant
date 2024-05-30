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

def get_material_id_from_name(doc, mat_name):
    materials = FilteredElementCollector(doc).OfClass(Material).ToElements()
    for mat in materials:
        if mat.Name == mat_name:
            return mat.Id
    else:
        return None
    
def get_volume_of_material_in_component(doc, material, component):
    mat_id = get_material_id_from_name(doc, material)

    if component == 'beams':
        beams = get_all_beams(doc)
        volume = 0
        for beam in beams:
            volume += beam.GetMaterialVolume(mat_id)
        return volume
    
    elif component == 'columns':
        columns = get_all_columns(doc)
        volume = 0
        for column in columns:
            volume += column.GetMaterialVolume(mat_id)
        return volume
    
    elif component == 'floors':
        floors = get_all_floors(doc)
        volume = 0
        for floor in floors:
            volume += floor.GetMaterialVolume(mat_id)
        return volume
    
    elif component == 'foundations':
        foundations = get_all_foundations(doc)
        volume = 0
        for foundation in foundations:
            volume += foundation.GetMaterialVolume(mat_id)
        return volume

    elif component == 'walls':
        walls = get_all_walls(doc)
        volume = 0
        for wall in walls:
            volume += wall.GetMaterialVolume(mat_id)
        return volume
    
    else:
        return None


    

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



# def call_other_script(target_environment_python, target_script, input):
#     # Build the command to run the script in the target environmentr
#     command = [target_environment_python, target_script,input]

#     # Use subprocess to run the command
#     try:
#         result = subprocess.run(command, capture_output=True, check=True)
#         return "Command Output: " + str(result.stdout)


#         # # Print the return code
#         # print("Return Code:", result.returncode)
#     except subprocess.CalledProcessError as e:
#         return f"Error: {e}"##
