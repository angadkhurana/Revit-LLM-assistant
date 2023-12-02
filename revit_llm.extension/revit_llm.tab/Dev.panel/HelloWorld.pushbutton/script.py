#! python3
__title__ = 'wassup'
__author__  = 'angad'
__doc__ = """random"""

uidoc = __revit__.ActiveUIDocument
from snippets.selection import get_selected_elements


# from bs4 import BeautifulSoup 
import subprocess

if __name__ == '__main__':

    # Specify the path to the Python interpreter in the target environment
    target_environment_python = 'C:/Users/angad/anaconda3/envs/revit_llm_env/python.exe'

    # Specify the path to the Python script you want to run in the target environment
    target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/qwerty.py'

    # Build the command to run the script in the target environment
    command = [target_environment_python, target_script,'6']

    # Use subprocess to run the command
    try:
        result = subprocess.run(command, capture_output=True, check=True)
        # Print the output
        print("Command Output:")
        print(result.stdout)

        # Print the return code
        print("Return Code:", result.returncode)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")##

    
    print(get_selected_elements(uidoc))

    x = [uidoc.Document.GetElement(x) for x in uidoc.Selection.GetReferences()]
    print(x[0].Name)
    # selected_element_ids = get_selected_elements(uidoc)
    # dimension_element = uidoc.Document.GetElement(selected_element_ids[0])
    # print(dimension_element.Value)