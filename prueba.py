import requests
import json

correo =  'javiermunozarcaya@gmail.com'
clave = 'arrayan2020'

def login():
    datos = {
        'username' : correo,
        'password' : clave
        }
    peticion = requests.post('http://18.220.217.118:8080/api/login/', data=datos)

    if peticion.ok:
        token = peticion
        # print(token.text)
        return token
    else:
        print('error de token')

def listado(token):
    valor = 'JWT '+ token.json()["token"]
    datos = {'Authorization' : valor}
           
    peticion = requests.get('http://18.220.217.118:8080/employee/', headers=datos)

    if peticion.ok:
        listado = peticion
        print(listado.json())
    else:
        print('error de listado')


def creacion(token):
    valor = 'JWT '+ token.json()["token"]
    
    datos = {'Authorization' : valor, 'Content-Type' : 'application/json'}
    datoss = {        
        'nombre':'prueba'
        ,'apellido' : 'prueba'
        ,'run':'18846300'
        }
    
    peticion = requests.post('http://18.220.217.118:8080/employee/' , data=json.dumps(datoss), headers = datos  )

    print(peticion.status_code )
    
    if peticion.ok:
        print('creando')
        print(peticion.text)
    else:
        print('error ')



token = login()

listado(token)
creacion(token)
