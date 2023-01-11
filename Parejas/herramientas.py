from django.urls import path, include
from django.urls import path

def importarApp(nombre: str) -> str:
    primeraMayuscula = nombre[0].upper() + nombre[1:]
    respuesta = '{}.apps.{}Config'.format(nombre, primeraMayuscula)
    respuesta = '{}'.format(nombre)
    return respuesta

def agregarURL(URL, nombreDeApp):
    archivoURL = "{}.urls".format(nombreDeApp)
    return path(URL, include(archivoURL))

def agregarViewURL(ruta ,view, nombre):
    return path(ruta, view, name=nombre)


def calcularMatch(usuarioBase, usuarios) -> list:
    usuarioBase = usuarioBase[0]
    print(usuarioBase.user)
    resultado = []


    for usuario in usuarios:
        ocupacion = usuario.ocupacion
        mas_importancia = usuario.mas_importancia
        edad = usuario.edad
        nivel_educativo = usuario.nivel_educativo
        introvertido_extrovertido = usuario.introvertido_extrovertido
        calmado_nervioso = usuario.calmado_nervioso
        deporte = usuario.deporte
        viajar = usuario.viajar
        videojuegos = usuario.videojuegos
        leer = usuario.leer
        cine = usuario.cine
        amistad = usuario.amistad
        mascotas = usuario.mascotas
        apariencia = usuario.apariencia
        salud = usuario.salud
        experimentar = usuario.experimentar
        hijos = usuario.hijos
        sueño = usuario.sueño

        musica = usuario.musica


        # ///////////////////////////////////////////////////////

        if ocupacion != usuarioBase.ocupacion:
            if 1 in [ocupacion, usuarioBase.ocupacion]:
                if 0 in [ocupacion, usuarioBase.ocupacion] or 3 in [ocupacion, usuarioBase.ocupacion]:
                    ocupacion = 0
                else:
                    ocupacion = 1
            else:
                ocupacion = 2
        else:
            ocupacion = 3

        if 3 in [mas_importancia, usuarioBase.mas_importancia]:
            if mas_importancia != usuarioBase.mas_importancia:
                mas_importancia = 0
            else:
                mas_importancia = 1
        else:
            mas_importancia = 2

        musica = 0 if musica != usuarioBase.musica else 1

        edad = diferencia(edad, usuarioBase.edad, 80)

        nivel_educativo = diferencia(nivel_educativo, usuarioBase.nivel_educativo, 4)

        introvertido_extrovertido = diferencia(introvertido_extrovertido, usuarioBase.introvertido_extrovertido, 9)

        calmado_nervioso = diferencia(calmado_nervioso, usuarioBase.calmado_nervioso, 9)

        deporte = diferencia(deporte, usuarioBase.deporte, 4)

        viajar = diferencia(viajar, usuarioBase.viajar)

        videojuegos = diferencia(videojuegos, usuarioBase.videojuegos)

        leer = diferencia(leer, usuarioBase.leer)

        cine = diferencia(cine, usuarioBase.cine)

        amistad = diferencia(amistad, usuarioBase.amistad)

        mascotas = diferencia(mascotas, usuarioBase.mascotas)

        apariencia = diferencia(apariencia, usuarioBase.apariencia)

        salud = diferencia(salud, usuarioBase.salud)

        experimentar = diferencia(apariencia, usuarioBase.apariencia)

        hijos = diferencia(hijos, usuarioBase.hijos, 2)

        sueño = diferencia(sueño, usuarioBase.sueño, 2)

        suma = edad + nivel_educativo + introvertido_extrovertido + calmado_nervioso + deporte + viajar + videojuegos + leer + cine + amistad + mascotas + apariencia + salud + experimentar + hijos + sueño + musica + ocupacion + mas_importancia
        suma = 19 - suma
        suma = suma*100/19
        suma = round(suma)
        usuario.match = suma
        resultado.append(usuario)


    return resultado


def diferencia(valor1, valor2, rango = 3):
    valor1 = discretizar(valor1, rango)
    valor2 = discretizar(valor2, rango)
    resultado = valor1 - valor2
    resultado = abs(resultado)
    return resultado

def discretizar(valor, rango):
    return valor/rango



