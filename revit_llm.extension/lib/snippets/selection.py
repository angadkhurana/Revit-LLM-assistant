# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_selected_elements(uidoc):
    return [uidoc.Document.GetElement(x) for x in uidoc.Selection.GetElementIds()]
