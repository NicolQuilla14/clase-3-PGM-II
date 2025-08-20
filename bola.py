from vpython import *
import asyncio
import random

scene = canvas(title="Combinación de Conceptos en VPython", width=800, height=600)

#colores
colores = [color.red, color.green, color.blue, color.yellow, color.orange]

def crear_cubos(posicion, tamaño, n):
    if n == 0:
        return  
    cubo = box(pos=posicion, size=vector(tamaño, tamaño, tamaño), color=random.choice(colores))
    crear_cubos(posicion + vector(0, 1.5 * tamaño, 0), tamaño * 0.8, n - 1)

crear_cubos(vector(0, -5, 0), 1, 5)

#limites en x y
x_lim = 5
y_lim = 4

async def mover_objeto(objeto, velocidad):
    while True:
        objeto.pos += velocidad
        #rebote
        if abs(objeto.pos.x) > x_lim:
            velocidad.x *= -1
        if abs(objeto.pos.y) > y_lim:
            velocidad.y *= -1
        await asyncio.sleep(0.01)

cubo = box(pos=vector(-x_lim, 4, 0), size=vector(1,1,1), color=color.red)
esfera = sphere(pos=vector(-x_lim, -4, 0), radius=1, color=color.green)

vel_cubo = vector(0.02, -0.02, 0)
vel_esfera = vector(0.02, 0.02, 0)

async def main():
    task1 = asyncio.create_task(mover_objeto(cubo, vel_cubo))    
    task2 = asyncio.create_task(mover_objeto(esfera, vel_esfera)) 
    await asyncio.gather(task1, task2)

asyncio.run(main())
