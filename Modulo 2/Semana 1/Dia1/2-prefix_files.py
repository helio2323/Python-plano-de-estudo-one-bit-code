from pathlib import Path

p1 = Path('./Modulo 2/Semana 1/Dia1')

root_dir = Path('./Modulo 2/Semana 1/Dia1')
file_paths = root_dir.iterdir()
#print(list(file_paths))

for path in file_paths:
    suf = path.suffix
    new_filename = f'new-{path.stem}{path.suffix}'
    if suf == '.txt':
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)