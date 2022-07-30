from unittest import result


import os

def get_output_path(caller):
    script_dir = os.path.dirname(caller)
    result_path = os.path.join(script_dir, 'outputs/')
    if not os.path.isdir(result_path):
        os.makedirs(result_path)
    return result_path