from os.path import abspath, dirname, join

def get_abspath(relative_path, from_path):
    return abspath(join(dirname(from_path), relative_path))
