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
    
def convert_to_cubic_meters(volume, unit_type):
    if unit_type == DisplayUnitType.DUT_CUBIC_METERS:
        return volume
    elif unit_type == DisplayUnitType.DUT_CUBIC_FEET:
        return volume * 0.0283168  # cubic feet to cubic meters
    elif unit_type == DisplayUnitType.DUT_CUBIC_INCHES:
        return volume * 1.63871e-5  # cubic inches to cubic meters
    else:
        raise ValueError(f"Unsupported unit type: {unit_type}")

# Function to get the volume unit of a material
def get_volume_unit(element):
    for param in element.Parameters:
        if param.Definition.ParameterType == ParameterType.Volume:
            return param.DisplayUnitType
    return None

def get_volume_of_material_in_component(doc, material, component):
    mat_id = get_material_id_from_name(doc, material)

    if component == 'beams':
        elements = get_all_beams(doc)
    elif component == 'columns':
        elements = get_all_columns(doc)
    elif component == 'floors':
        elements = get_all_floors(doc)
    elif component == 'foundations':
        elements = get_all_foundations(doc)
    elif component == 'walls':
        elements = get_all_walls(doc)
    else:
        return None

    total_volume = 0
    for elem in elements:
        volume = elem.GetMaterialVolume(mat_id)
        unit_type = get_volume_unit(elem)
        if unit_type is not None:
            volume_in_cubic_meters = convert_to_cubic_meters(volume, unit_type)
            total_volume += volume_in_cubic_meters
        else:
            print(f"Warning: Could not determine volume unit for element ID {elem.Id}")

    return total_volume

    

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
