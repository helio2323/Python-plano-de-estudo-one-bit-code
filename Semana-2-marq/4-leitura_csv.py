
with open('courses.csv', 'r') as file:
    for line in file:
      row = line.strip().split(',')
      print(row)