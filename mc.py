import random
import math
#import pprint

#cantidad de preguntas que tiene el multiple choice - cambiar las veces que se quiera para probar la hipotesis
qty = 50
#en un futuro, la idea es que sea con input para el usuario: int(input('Cuantas preguntas tendrá el multiple choice?(en números): '))
print('Cantidad de preguntas en el multiple choice: ',qty, '\n')

a = 0
b = 0
c = 0
d = 0

'''
#para limpiar los arrays, y volver a probar la hipotesis con otro número(qty), descomentar esto
a_array =[]
b_array =[]
c_array =[]
d_array =[]

'''

for i in range(qty):
    opcion = random.randint(1,4)
    if opcion == 1:
        a=a+1
    elif opcion == 2:
        b=b+1
    elif opcion == 3:
        c=c+1    
    elif opcion == 4:
        d=d+1    

if 'a_array' in locals() or 'a_array' in globals():
    a_array=a_array
else: a_array=[]

if 'b_array' in locals() or 'b_array' in globals():
    b_array=b_array
else: b_array=[]

if 'c_array' in locals() or 'c_array' in globals():
    c_array=c_array
else: c_array=[]
    
if 'd_array' in locals() or 'd_array' in globals():
    d_array=d_array
else: d_array=[]
 

print('Probabilidad de cada opción en la corrida actual:\n')

if a != 0:
    probabilidad_a = round((a/qty)*100)
    a_array.append(probabilidad_a)
    print('a= ',probabilidad_a,'%')

if b!= 0:
    probabilidad_b = round((b/qty)*100)
    b_array.append(probabilidad_b)
    print('b= ',probabilidad_b,'%')

if c!= 0:
    probabilidad_c = round((c/qty)*100)
    c_array.append(probabilidad_c)
    print('c= ',probabilidad_c,'%')

if d!=0:
    probabilidad_d = round((d/qty)*100)
    d_array.append(probabilidad_d)
    print('d= ',probabilidad_d,'%')

    
print('\nProbabilidad de cada opción en cada una de las corridas realizadas:\n')
print(a_array)
print(b_array)
print(c_array)
print(d_array)

sum_a=0
sum_b=0
sum_c=0
sum_d=0

for num in a_array:
    sum_a=sum_a+num

a_promedio = round(sum_a/len(a_array))

for num in a_array:
    sum_b=sum_b+num

b_promedio = round(sum_b/len(b_array))

for num in c_array:
    sum_c=sum_c+num

c_promedio = round(sum_c/len(c_array))

for num in d_array:
    sum_d=sum_d+num

d_promedio = round(sum_d/len(d_array))

print('\nProbabilidad total de cada opción:\n')
print('Probabilidad de que la respuesta sea la opcion a: ',a_promedio,'%')
print('Probabilidad de que la respuesta sea la opcion b: ',b_promedio,'%')
print('Probabilidad de que la respuesta sea la opcion c: ',c_promedio,'%')
print('Probabilidad de que la respuesta sea la opcion d: ',d_promedio,'%')
