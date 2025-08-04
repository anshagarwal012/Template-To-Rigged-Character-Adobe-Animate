from split import *
from create_fla import *

name = "girl"
output_folder = f"output/{name}"
exported = slice_character(f"characters/{name}.png", output_folder, target_size=(4096, 4096))
print("✅ Exported files:", exported)
create_xfl_project(output_folder, output_folder)