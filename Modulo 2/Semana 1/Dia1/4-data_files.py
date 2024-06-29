from pathlib import Path
from datetime import datetime

path = Path('./Modulo 2/Semana 1/Dia1', 'c.txt')

stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)

date_created_str = date_created.strftime('%d-%m-%Y %H:%M:%S')

print(date_created_str)
