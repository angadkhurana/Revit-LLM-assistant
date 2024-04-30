# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *
import subprocess
from pyrevit import  DB

# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory



uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_selected_elements(uidoc):
    return [uidoc.Document.GetElement(x) for x in uidoc.Selection.GetElementIds()]


def is_terrace(uidoc):
    from pyrevit import revit, DB



def floor_area(floor):
    geom = floor.get_Geometry(Options()) # list of solids
    # assuming number of solids=1
    for solid in geom:
        return max([face.Area for face in solid.Faces])



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
