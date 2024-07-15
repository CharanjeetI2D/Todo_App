file_path = 'Todos.txt'


def get_todos(file_name=file_path):
    """ Reads the file and returns list of to do items"""
    with open(file_name, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path_arg=file_path):
    """Writes to the to do list to the text file"""
    with open(file_path_arg, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print("You are now running the functions file as main.")
