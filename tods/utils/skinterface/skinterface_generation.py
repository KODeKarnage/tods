
import re
import os

with open('tods/utils/skinterface/entry_points.txt','r',encoding='utf-8') as f:
    entry_file = f.read()

output_dir = 'tods/utils/skinterface/primitiveSKI'


primitive_folder_start_loc_buf = [i.start()+2 for i in re.finditer('=', entry_file)]
primitive_start_loc_buf = [i.start()+1 for i in re.finditer(':', entry_file)]
primitive_end_loc_buf = [i.start() for i in re.finditer('\n', entry_file)]

for primitive_index, primitive_start_loc in enumerate(primitive_start_loc_buf):

    primitive_folder_start_loc = primitive_folder_start_loc_buf[primitive_index]
    primitive_end_loc = primitive_end_loc_buf[primitive_index]

    primitive_folder = entry_file[primitive_folder_start_loc:primitive_start_loc-1]
    primitive_name = entry_file[primitive_start_loc:primitive_end_loc]
    # print(entry_file[primitive_folder_start_loc:primitive_start_loc-1])
    # print(entry_file[primitive_start_loc:primitive_end_loc])

    import_line1 = 'import numpy as np \nfrom .Base_skinterface import BaseSKI\n'
    import_line2 = 'from ' + primitive_folder + ' import ' + primitive_name + '\n\n'
    # print(import_line)

    class_name = primitive_name.replace('Primitive', 'SKI')
    class_line1 = 'class ' + class_name + '(BaseSKI):\n\tdef __init__(self, **hyperparams):\n\t\tsuper().__init__(primitive='
    class_line2 = primitive_name + ', **hyperparams)\n\n'

    python_content = import_line1 + import_line2 + class_line1 + class_line2
    python_name = primitive_name.replace('Primitive', '_skinterface.py')
    with open(os.path.join(output_dir, python_name), 'w', encoding='utf-8') as f:
        f.write(python_content)
    #print(os.path.join(output_dir, python_name))
    print(python_content)


# import numpy as np
# from test_interface import SKInterface
# from tods.detection_algorithm.AutoRegODetect import AutoRegODetectorPrimitive
#
# class AutoRegODetect(SKInterface):
# def __init__(self, **hyperparams):
# super().__init__(primitive=AutoRegODetectorPrimitive, hyperparams)


