import os

def find_py_files_without_comments(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r') as f:
                        first_line = f.readline().strip()
                        if not first_line.startswith('#'):
                            print(filepath)
                except:
                    pass

find_py_files_without_comments('/workspaces/DSA_Bundled')