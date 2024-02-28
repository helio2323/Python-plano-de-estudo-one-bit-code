#args - utilizamos quando nao temos certeza de quantos argumentos queremos na funcao
#argmentos sao passados como uma tupla

#kwargs - alem dos valores podemos passar as respectivas chaves para cada argumento - sao passados como dict


# 1 - soma de numeros

def sum(*nume):
    sum_total = 0
    
    for n in nume:
        sum_total += n
    print(f"Soma total: {sum_total}")

sum(7, 5, 10, 20, 30)

# 2 - apresentacao de cursos

def presentation_course(**course):
    for key, value in course.items():
        print(f"{key}: {value}")
        
presentation_course(name="Python", duration=20, level="beginner", open_course=True)