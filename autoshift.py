import re

import i3ipc


""" 1) Establish connection to i3
    2) Store the workspace data in a data structure
    3) Split the variables in the data structure into 
        > number + anything after (use regex)
        > maybe a dictionary could be suitable for this
        > or double-linked list????
    4) Perform a shift down 
    5) Send back data to i3 to recreate workspaces
"""

""" @workspace_details : dictionary containing i3 workspace data
    Shift the workspaces in the dictionary where the name does not match 
    the current index"""
def shift_workspaces(workspace_details):
    for x in workspace_details:
        index = list(workspace_details.keys()).index(x)
        if (x != index + 1):
            workspace_details[index + 1] = workspace_details.pop(x)
       
    return workspace_details
# def perform_shift(workspace_details):
#     for x in workspace_details:

def rename_workspaces(shifted_workspaces):
    for x in shifted_workspaces:
        print(re.match('^\d*',shifted_workspaces[x]))
        re.sub('^\d*',shifted_workspaces[x],str(x))
    
    return shifted_workspaces

# Main function to shift workspaces
def tidy_workspaces(i3):
    workspace_details = {}

    # Store workspace information in a dictionary [number, name]
    for workspace_index, workspace in enumerate(i3.get_tree().workspaces()):
        workspace_details[workspace.num] = workspace.name
    
    print(workspace_details)
    shifted_workspaces = shift_workspaces(workspace_details)
    renamed_workspaces = rename_workspaces(shifted_workspaces)
    print(shifted_workspaces)
    print(renamed_workspaces)

# Basically void args from java
if __name__ == '__main__':
    i3 = i3ipc.Connection()

    tidy_workspaces(i3)
