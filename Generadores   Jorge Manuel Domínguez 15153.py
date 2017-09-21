# -*- coding: utf-8 -*-
"""
Homework 2 - Generadores

Jorge Manuel Domínguez   15153
"""

# FUNCIONA EN PYTHON 3.6, en Windows 10

# Parte 1

print("Problema #1")
print()

def running_average():
    k = 0.0 #Contador de la cantidad de elementos de la cual se calcula el promedio
    sumatotal = 0.0
    promedio = None
    while True:
        term = yield promedio
        sumatotal += term
        k += 1
        promedio = (sumatotal/k)

ra = running_average()
next(ra)
for value in [7, 13, 17, 231, 12, 8, 3]:
    out_str = "sent: {val:3d}, new average: {avg:6.2f}"
    print(out_str.format(val=value, avg=ra.send(value)))

# Parte 2

print()
print("Problema #2")
print()

# Codificado de manera semejante al reloj que programamos en clase
# minc y hrc representan a los minutos y horas, respectivamente,
# que se deben sumar cuandoel contador de segundos llega a 60, entonces
# al contador de minutos se le debe adicionar un minuto, en el caso de minc

def trange(start, stop, step):
    actual = list(start)
    while actual < list(stop):
        yield tuple(actual)
        sec = step[2] + actual[2]
        minc = 0
        hrc = 0
        if sec < 60:
            actual[2] = sec
        else:
            actual[2] = sec - 60
            minc = 1
        mins = step[1] + actual[1] + minc
        if mins < 60:
            actual[1] = mins
        else:
            actual[1] = mins - 60
            hrc = 1
        hr = step[0] + actual[0] + hrc
        if hr < 24:
            actual[0] = hr 
        else:
            actual[0] = hr - 24

if __name__ == "__main__":           
    for time in trange((10,10,10),(13,50,15),(0,15,12)):
        print(time)

print()
print("Problema #3")
print()

def rtrange(start, stop, step):
    actual = list(start)
    while actual < list(stop):
        # Con las siguientes líneas modifico la función del problema anterior
        # según las intrucciones de este problema, todo lo demás es igual
        new_start = yield tuple(actual)
        if new_start != None:
            actual = list(new_start)
            continue
        sec = step[2] + actual[2]
        minc = 0
        hrc = 0
        if sec < 60:
            actual[2] = sec
        else:
            actual[2] = sec - 60
            minc = 1
        mins = step[1] + actual[1] + minc
        if mins < 60:
            actual[1] = mins
        else:
            actual[1] = mins - 60
            hrc = 1
        hr = step[0] + actual[0] + hrc
        if hr < 24:
            actual[0] = hr
        else:
            actual[0] = hr - 24

if __name__ == "__main__":           
    ts = rtrange((10,10,10),(13,50,15),(0,15,12))  
    for x in range(3):
        print(next(ts))
        
    print(ts.send((8, 5, 50)))
    for y in range(3):
        print(next(ts))

print()
print("Problema #4")
print()

import random

fh = open("Tiempo_vs_Temperatura.txt", "w")
for time in rtrange((6,0,0),(23,0,0),(0,1,30)):
    temp = random.randint(10,25)
    dato = time + (temp,)
    output = "{:02d}:{:02d}:{:02d} {:4.1f}\n".format(*dato)
    fh.write(output)

print()
print("Problema #5")
print()

import random

def random_ones_and_zeros():
    p = 0.5
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message
        
x = random_ones_and_zeros()
next(x)
for p in [0.2,0.5,0.8]:
    x.send(p)
    print("\nprobabiliy: " + str(p))
    for i in range(15):
        print(next(x), end=" ")