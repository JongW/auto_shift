#!/usr/bin/env python3
import re

import i3ipc


def tidy_workspaces(i3):

    for workspace_index, workspace in enumerate(i3.get_tree().workspaces()):

        old_name = workspace.name

        # If the workspace is in the wrong number assign it to the correct num
        if(workspace.num != workspace_index + 1):
            workspace.num = workspace_index + 1

        new_name = rename_workspace(workspace)

        # Command i3 to recorrect the workspaces
        i3.command('rename workspace "%s" to "%s"' % (old_name, new_name))


def rename_workspace(workspace):
    """Change the workspace name to reflect the correct workspace number"""
    workspace.name = re.sub('^\d*', str(workspace.num), workspace.name)
    return workspace.name


if __name__ == '__main__':
    i3 = i3ipc.Connection()

    tidy_workspaces(i3)
