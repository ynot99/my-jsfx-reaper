import os
import glob

src_dir = 'src'
out_file = 'CircleOfFifthAnalyzer.jsfx'
files = [
    '00_header.jsfx-inc',
    '01_init.jsfx-inc',
    '02_slider.jsfx-inc',
    '03_serialize.jsfx-inc',
    '04_block.jsfx-inc'
]

# Add all 05_gfx_* files sorted
gfx_files = sorted([f for f in os.listdir(src_dir) if f.startswith('05_gfx_') and f.endswith('.jsfx-inc')])
files.extend(gfx_files)

compiled = ""
for f_name in files:
    path = os.path.join(src_dir, f_name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            compiled += f.read()

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(compiled)

print(f"Compiled successfully {len(files)} files into {out_file}")
