import subprocess

# Specify the path to the Python interpreter in the target environment
target_environment_python = 'C:/Users/angad/anaconda3/envs/revit_llm_env/python.exe'

# Specify the path to the Python script you want to run in the target environment
target_script = 'C:/Users/angad/OneDrive/Desktop/LangChain/Revit-LLM-assistant/qwerty.py'

# Build the command to run the script in the target environment
command = [target_environment_python, target_script,'25']

# Use subprocess to run the command
try:
    result = subprocess.run(command, capture_output=True, check=True)
    print("Command Output:", result.stdout)
    # Print the return code
    print("Return Code:", result.returncode)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")##
