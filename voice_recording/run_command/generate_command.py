import os
import re
import ctypes

mapping_drive = {
    'Ц': {
        'permission': 'Users',
        'directory': 'C:\\'
    },
    'ц': {
        'permission': 'Users',
        'directory': 'C:\\'
    },
    'це': {
        'permission': 'Users',
        'directory': 'C:\\'
    },
    'C': {
        'permission': 'Users',
        'directory': 'C:\\'
    },
    'Д': {
        'permission': 'Users',
        'directory': 'D:\\'
    },
    'Рабочем столе': {
        'permission': None,
        'directory': 'C:\\Users\\aleksandr\Desktop'
    },
}

exclude_dir = ['AppData', 'Application Data', 'VKR']

def parse_command(command: str):

    pattern = r"(открой|удали) ([a-я]+) на (диске|диски) ([а-я])"

    match = re.search(pattern, command)

    method = match.group(1)
    item_name = match.group(2)
    drive = match.group(4)

    find_directory = mapping_drive.get(drive)

    return method, item_name, find_directory


def find_recursion(filename: str, directory: str, permission: str | None):
    try:
        for item in os.listdir(directory):

            if (permission and not (item == permission)):
                continue

            if item.startswith('.') or item in exclude_dir:
                continue

            path = os.path.join(directory, item)

            if os.path.isdir(path):
                result =  find_recursion(filename, path, None)

                if isinstance(result, str):
                    return result

            if os.path.isfile(path):
                lower_item = item.lower()
                if lower_item.startswith(filename):
                    return os.path.join(directory, item)

    except PermissionError as e:
        print(e)


def generate(command: str):
    item_type, filename, find_directory = parse_command(command)

    directory = find_directory['directory']
    permission = find_directory['permission']

    absolute_path = find_recursion(filename, directory, permission)

    return item_type, absolute_path


def execute_open(absolute_path: str):

    SHELL_EXECUTE_FUNC = ctypes.windll.shell32.ShellExecuteW
    SW_SHOWNORMAL = 1

    SHELL_EXECUTE_FUNC(None, "open", absolute_path, None, None, SW_SHOWNORMAL)


def start_execute_command(command: str):
    mapping_method = {
        'открыть': execute_open,
        'открой': execute_open,
    }

    item_type, absolute_path = generate(command)

    method = mapping_method[item_type]

    method(absolute_path)


start_execute_command("открой без на диске це")













