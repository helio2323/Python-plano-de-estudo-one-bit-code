from pathlib import Path
from datetime import datetime

root_dir = Path('./Modulo 2/Semana 1/Dia1')

for path in root_dir.glob('**/*'):
    if path.is_file():
        if path.suffix == '.txt':
            print(path)
            stats = path.stat()
            second_created = stats.st_ctime
            date_created = datetime.fromtimestamp(second_created)
            date_created_str = date_created.strftime('%d-%m-%Y %H:%M:%S')
            new_filename = f'{path.stem}-{date_created_str}{path.suffix}'
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)