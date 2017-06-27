import simplejson
import pusher
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.files.storage import default_storage
from django.db import IntegrityError
from django.db.models import Count
from django.db.models import Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from main.utils import *
from .forms import *
from .models import *


# def fijoDashboard(request):
#     id = request.POST.get("fijoId")
#     # id = str(id)
#
#
#     # transacciones hechas por hoy
#     transaccionesDiarias = Transacciones.objects.filter(idVendedor=id).values('fecha').annotate(conteo=Count('fecha'))
#     temp_transaccionesDiarias = list(transaccionesDiarias)
#     transaccionesDiariasArr = []
#     for element in temp_transaccionesDiarias:
#         aux = []
#         aux.append(element['fecha'])
#         aux.append(element['conteo'])
#         transaccionesDiariasArr.append(aux)
#     transaccionesDiariasArr = simplejson.dumps(transaccionesDiariasArr)
#
#     # ganancias de hoy
#     gananciasDiarias = Transacciones.objects.filter(idVendedor=id).values('fecha').annotate(ganancia=Sum('precio'))
#     temp_gananciasDiarias = list(gananciasDiarias)
#     gananciasDiariasArr = []
#     for element in temp_gananciasDiarias:
#         aux = []
#         aux.append(element['fecha'])
#         aux.append(element['ganancia'])
#         gananciasDiariasArr.append(aux)
#     gananciasDiariasArr = simplejson.dumps(gananciasDiariasArr)
#
#     # todos los productos del vendedor
#     productos = Comida.objects.filter(idVendedor=id).values('nombre', 'precio')
#     temp_productos = list(productos)
#     productosArr = []
#     productosPrecioArr = []
#     for element in temp_productos:
#         aux = []
#         productosArr.append(element['nombre'])
#         aux.append(element['nombre'])
#         aux.append(element['precio'])
#         productosPrecioArr.append(aux)
#     productosArr = simplejson.dumps(productosArr)
#     productosPrecioArr = simplejson.dumps(productosPrecioArr)
#
#     # productos vendidos hoy con su cantidad respectiva
#     fechaHoy = str(timezone.now()).split(' ', 1)[0]
#     productosHoy = Transacciones.objects.filter(idVendedor=id, fecha=fechaHoy).values('nombreComida').annotate(
#         conteo=Count('nombreComida'))
#     temp_productosHoy = list(productosHoy)
#     productosHoyArr = []
#     for element in temp_productosHoy:
#         aux = []
#         aux.append(element['nombreComida'])
#         aux.append(element['conteo'])
#         productosHoyArr.append(aux)
#     productosHoyArr = simplejson.dumps(productosHoyArr)
#
#     return render(request, 'main/fijoDashboard.html',
#                   {"transacciones": transaccionesDiariasArr, "ganancias": gananciasDiariasArr,
#                    "productos": productosArr, "productosHoy": productosHoyArr, "productosPrecio": productosPrecioArr})
#
#
# def ambulanteDashboard(request):
#     id = request.POST.get("ambulanteId")
#     # id = str(id)
#
#
#     # transacciones hechas por hoy
#     transaccionesDiarias = Transacciones.objects.filter(idVendedor=id).values('fecha').annotate(conteo=Count('fecha'))
#     temp_transaccionesDiarias = list(transaccionesDiarias)
#     transaccionesDiariasArr = []
#     for element in temp_transaccionesDiarias:
#         aux = []
#         aux.append(element['fecha'])
#         aux.append(element['conteo'])
#         transaccionesDiariasArr.append(aux)
#     transaccionesDiariasArr = simplejson.dumps(transaccionesDiariasArr)
#
#     # ganancias de hoy
#     gananciasDiarias = Transacciones.objects.filter(idVendedor=id).values('fecha').annotate(ganancia=Sum('precio'))
#     temp_gananciasDiarias = list(gananciasDiarias)
#     gananciasDiariasArr = []
#     for element in temp_gananciasDiarias:
#         aux = []
#         aux.append(element['fecha'])
#         aux.append(element['ganancia'])
#         gananciasDiariasArr.append(aux)
#     gananciasDiariasArr = simplejson.dumps(gananciasDiariasArr)
#
#     # todos los productos del vendedor
#     productos = Comida.objects.filter(idVendedor=id).values('nombre', 'precio')
#     temp_productos = list(productos)
#     productosArr = []
#     productosPrecioArr = []
#     for element in temp_productos:
#         aux = []
#         productosArr.append(element['nombre'])
#         aux.append(element['nombre'])
#         aux.append(element['precio'])
#         productosPrecioArr.append(aux)
#     productosArr = simplejson.dumps(productosArr)
#     productosPrecioArr = simplejson.dumps(productosPrecioArr)
#
#     # productos vendidos hoy con su cantidad respectiva
#     fechaHoy = str(timezone.now()).split(' ', 1)[0]
#     productosHoy = Transacciones.objects.filter(idVendedor=id, fecha=fechaHoy).values('nombreComida').annotate(
#         conteo=Count('nombreComida'))
#     temp_productosHoy = list(productosHoy)
#     productosHoyArr = []
#     for element in temp_productosHoy:
#         aux = []
#         aux.append(element['nombreComida'])
#         aux.append(element['conteo'])
#         productosHoyArr.append(aux)
#     productosHoyArr = simplejson.dumps(productosHoyArr)
#
#     return render(request, 'main/ambulanteDashboard.html',
#                   {"transacciones": transaccionesDiariasArr, "ganancias": gananciasDiariasArr,
#                    "productos": productosArr, "productosHoy": productosHoyArr, "productosPrecio": productosPrecioArr})
#
#
# def adminEdit(request):
#     nombre = request.POST.get("adminName")
#     contraseña = request.POST.get("adminPassword")
#     id = request.POST.get("adminId")
#     email = request.POST.get("adminEmail")
#     avatar = request.POST.get("adminAvatar")
#     return render(request, 'main/adminEdit.html',
#                   {"nombre": nombre, "contraseña": contraseña, "id": id, "email": email, "avatar": avatar})
#
#
# def signup(request):
#     return render(request, 'main/signup.html', {})
#
#
# def signupAdmin(request):
#     return render(request, 'main/signupAdmin.html', {})
#
#
# def loggedin(request):
#     return render(request, 'main/loggedin.html', {})
#
#
# def loginAdmin(request):
#     id = request.POST.get("userID")
#     email = request.POST.get("email")
#     avatar = "avatars/" + request.POST.get("fileName")
#     nombre = request.POST.get("name")
#     contraseña = request.POST.get("password")
#     return adminPOST(id, avatar, email, nombre, contraseña, request)
#
#
# def adminPOST(id, avatar, email, nombre, contraseña, request):
#     # ids de todos los usuarios no admins
#     datosUsuarios = []
#     i = 0
#     numeroUsuarios = Usuario.objects.count()
#     numeroDeComidas = Comida.objects.count()
#     for usr in Usuario.objects.raw('SELECT * FROM usuario WHERE tipo != 0'):
#         datosUsuarios.append([])
#         datosUsuarios[i].append(usr.id)
#         datosUsuarios[i].append(usr.nombre)
#         datosUsuarios[i].append(usr.email)
#         datosUsuarios[i].append(usr.tipo)
#         datosUsuarios[i].append(str(usr.avatar))
#         datosUsuarios[i].append(usr.activo)
#         datosUsuarios[i].append(usr.formasDePago)
#         datosUsuarios[i].append(usr.horarioIni)
#         datosUsuarios[i].append(usr.horarioFin)
#         datosUsuarios[i].append(usr.contraseña)
#
#         i += 1
#     listaDeUsuarios = simplejson.dumps(datosUsuarios, ensure_ascii=False).encode('utf8')
#
#     # limpiar argumentos de salida segun tipo de vista
#     argumentos = {"nombre": nombre, "id": id, "avatar": avatar, "email": email, "lista": listaDeUsuarios,
#                   "numeroUsuarios": numeroUsuarios, "numeroDeComidas": numeroDeComidas, "contraseña": contraseña}
#     return render(request, 'main/baseAdmin.html', argumentos)
#
#
# def obtenerFavoritos(idVendedor):
#     favoritos = 0
#     for fila in Favoritos.objects.raw('SELECT * FROM favoritos WHERE idVendedor = "' + str(idVendedor) + '"'):
#         favoritos += 1
#     return favoritos
#
#
# def loginReq(request):
#     # inicaliar variables
#     tipo = 0
#     nombre = ''
#     url = ''
#     id = 0
#     horarioIni = 0
#     horarioFin = 0
#     encontrado = False
#     email = request.POST.get("email")
#     avatar = ''
#     contraseña = ''
#     password = request.POST.get("password")
#     listaDeProductos = []
#     formasDePago = []
#     activo = False
#
#     # buscar vendedor en base de datos
#     # MyLoginForm = LoginForm(request.POST)
#     # if MyLoginForm.is_valid():
#     vendedores = []
#     for p in Usuario.objects.raw('SELECT * FROM usuario'):
#         if p.contraseña == password and p.email == email:
#             tipo = p.tipo
#             nombre = p.nombre
#             if (tipo == 0):
#                 url = 'main/baseAdmin.html'
#                 id = p.id
#                 tipo = p.tipo
#                 encontrado = True
#                 avatar = p.avatar
#                 contraseña = p.contraseña
#                 break
#             elif (tipo == 1):
#                 url = 'main/baseAlumno.html'
#                 id = p.id
#                 avatar = p.avatar
#                 tipo = p.tipo
#                 encontrado = True
#                 avatar = p.avatar
#
#                 break
#             elif (tipo == 2):
#                 url = 'main/vendedor-fijo.html'
#                 id = p.id
#                 tipo = p.tipo
#                 encontrado = True
#                 horarioIni = p.horarioIni
#                 horarioFin = p.horarioFin
#                 request.session['horarioIni'] = horarioIni
#                 request.session['horarioFin'] = horarioFin
#                 avatar = p.avatar
#                 activo = p.activo
#                 formasDePago = p.formasDePago
#                 request.session['formasDePago'] = formasDePago
#                 request.session['activo'] = activo
#                 break
#             elif (tipo == 3):
#                 url = 'main/vendedor-ambulante.html'
#                 id = p.id
#                 tipo = p.tipo
#                 encontrado = True
#                 avatar = p.avatar
#                 activo = p.activo
#                 formasDePago = p.formasDePago
#                 request.session['formasDePago'] = formasDePago
#                 request.session['activo'] = activo
#                 break
#
#         # si no se encuentra el usuario, se retorna a pagina de login
#         if encontrado == False:
#             return render(request, 'main/login.html', {"error": "Usuario o contraseña invalidos"})
#
#         # crear datos de sesion
#         request.session['id'] = id
#         request.session['tipo'] = tipo
#         request.session['email'] = email
#         request.session['nombre'] = nombre
#         request.session['avatar'] = str(avatar)
#         # si son vendedores, crear lista de productos
#         for p in Usuario.objects.raw('SELECT * FROM usuario'):
#             if p.tipo == 2 or p.tipo == 3:
#                 vendedores.append(p.id)
#         vendedoresJson = simplejson.dumps(vendedores)
#
#         # obtener alimentos en caso de que sea vendedor fijo o ambulante
#         if tipo == 2 or tipo == 3:
#             i = 0
#             for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
#                 listaDeProductos.append([])
#                 listaDeProductos[i].append(producto.nombre)
#                 categoria = str(producto.categorias)
#                 listaDeProductos[i].append(categoria)
#                 listaDeProductos[i].append(producto.stock)
#                 listaDeProductos[i].append(producto.precio)
#                 listaDeProductos[i].append(producto.descripcion)
#                 listaDeProductos[i].append(str(producto.imagen))
#                 i += 1
#
#         listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
#
#         # limpiar argumentos de salida segun tipo de vista
#         argumentos = {"email": email, "tipo": tipo, "id": id, "vendedores": vendedoresJson, "nombre": nombre,
#                       "horarioIni": horarioIni, "horarioFin": horarioFin, "avatar": avatar,
#                       "listaDeProductos": listaDeProductos}
#         if (tipo == 0):
#             request.session['contraseña'] = contraseña
#             return adminPOST(id, avatar, email, nombre, contraseña, request)
#         if (tipo == 1):
#             argumentos = {"nombresesion": nombre, "tipo": tipo, "id": id, "vendedores": vendedoresJson,
#                           "avatarSesion": avatar}
#         if (tipo == 2):
#             request.session['listaDeProductos'] = str(listaDeProductos)
#             request.session['favoritos'] = obtenerFavoritos(id)
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "horarioIni": horarioIni,
#                           "favoritos": obtenerFavoritos(id), "horarioFin": horarioFin, "avatar": avatar,
#                           "listaDeProductos": listaDeProductos, "activo": activo, "formasDePago": formasDePago,
#                           "activo": activo}
#         if (tipo == 3):
#             request.session['listaDeProductos'] = str(listaDeProductos)
#             request.session['favoritos'] = obtenerFavoritos(id)
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar, "favoritos": obtenerFavoritos(id),
#                           "listaDeProductos": listaDeProductos, "activo": activo, "formasDePago": formasDePago}
#
#         # enviar a vista respectiva de usuario
#         return render(request, url, argumentos)
#
#     # retornar en caso de datos invalidos
#     else:
#         return render(request, 'main/login.html', {"error": "Usuario o contraseña invalidos"})
#
#
# def gestionproductos(request):
#     if request.session.has_key('id'):
#         email = request.session['email']
#         tipo = request.session['tipo']
#         id = request.session['id']
#         if tipo == 3:
#             path = "main/baseVAmbulante.html"
#         if tipo == 2:
#             path = "main/baseVFijo.html"
#     return render(request, 'main/agregar-productos.html', {"path": path})
#
#
# # def vendedorprofilepage(request):
# #     return render(request, 'main/vendedor-profile-page.html', {})
#
#
# def formView(request):
#     if request.session.has_key('id'):
#         email = request.session['email']
#         tipo = request.session['tipo']
#         id = request.session['id']
#         if (tipo == 0):
#             url = 'main/baseAdmin.html'
#         elif (tipo == 1):
#             url = 'main/baseAlumno.html'
#         elif (tipo == 2):
#             url = 'main/vendedor-fijo.html'
#         elif (tipo == 3):
#             url = 'main/vendedor-ambulante.html'
#         return render(request, url, {"email": email, "tipo": tipo, "id": id})
#     else:
#         return render(request, 'main/base.html', {})
#
#
# def productoReq(request):
#     horarioIni = 0
#     horarioFin = 0
#     avatar = ""
#     if request.method == "POST":
#         if request.session.has_key('id'):
#             id = request.session['id']
#             email = request.session['email']
#             tipo = request.session['tipo']
#             if tipo == 3:
#                 path = "main/baseVAmbulante.html"
#                 url = "main/vendedor-ambulante.html"
#             if tipo == 2:
#                 path = "main/baseVFijo.html"
#                 url = "main/vendedor-fijo.html"
#             else:
#                 return render(request, 'main/agregar-productos.html',
#                               {"path": path, "respuesta": "¡Ingrese todos los datos!"})
#
#     # obtener alimentos en caso de que sea vendedor fijo o ambulante
#     i = 0
#     listaDeProductos = []
#     for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
#         listaDeProductos.append([])
#         listaDeProductos[i].append(producto.nombre)
#         categoria = str(producto.categorias)
#         listaDeProductos[i].append(categoria)
#         listaDeProductos[i].append(producto.stock)
#         listaDeProductos[i].append(producto.precio)
#         listaDeProductos[i].append(producto.descripcion)
#         listaDeProductos[i].append(str(producto.imagen))
#         i += 1
#     listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
#
#     for p in Usuario.objects.raw('SELECT * FROM usuario'):
#         if p.id == id:
#             avatar = p.avatar
#             horarioIni = p.horarioIni
#             horarioFin = p.horarioFin
#             nombre = p.nombre
#     return render(request, url, {"email": email, "tipo": tipo, "id": id, "nombre": nombre, "horarioIni": horarioIni,
#                                  "horarioFin": horarioFin, "avatar": avatar, "listaDeProductos": listaDeProductos})
#
#
# def vistaVendedorPorAlumno(request):
#     if request.method == 'POST':
#         id = int(request.POST.get("id"))
#         for p in Usuario.objects.raw('SELECT * FROM usuario'):
#             if p.id == id:
#                 favorito = 0
#                 for f in Favoritos.objects.raw('SELECT * FROM Favoritos'):
#                     if request.session['id'] == f.idAlumno:
#                         if id == f.idVendedor:
#                             favorito = 1
#                 tipo = p.tipo
#                 nombre = p.nombre
#                 avatar = p.avatar
#                 formasDePago = p.formasDePago
#                 horarioIni = p.horarioIni
#                 horarioFin = p.horarioFin
#                 if tipo == 3:
#                     url = 'main/vendedor-ambulante-vistaAlumno.html'
#                     break
#                 if tipo == 2:
#                     url = 'main/vendedor-fijo-vistaAlumno.html'
#                     break
#     # obtener alimentos
#     i = 0
#     listaDeProductos = []
#     for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
#         listaDeProductos.append([])
#         listaDeProductos[i].append(producto.nombre)
#         categoria = str(producto.categorias)
#         listaDeProductos[i].append(categoria)
#         listaDeProductos[i].append(producto.stock)
#         listaDeProductos[i].append(producto.precio)
#         listaDeProductos[i].append(producto.descripcion)
#         listaDeProductos[i].append(str(producto.imagen))
#         i += 1
#     avatarSesion = request.session['avatar']
#     listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
#     return render(request, url, {"nombre": nombre, "nombresesion": request.session['nombre'], "tipo": tipo, "id": id,
#                                  "avatar": avatar, "listaDeProductos": listaDeProductos, "avatarSesion": avatarSesion,
#                                  "favorito": favorito, "formasDePago": formasDePago, "horarioIni": horarioIni,
#                                  "horarioFin": horarioFin, })
#
#
# def vistaVendedorPorAlumnoSinLogin(request):
#     if request.method == 'POST':
#         id = int(request.POST.get("id"))
#         for p in Usuario.objects.raw('SELECT * FROM usuario'):
#             if p.id == id:
#                 tipo = p.tipo
#                 nombre = p.nombre
#                 avatar = p.avatar
#                 formasDePago = p.formasDePago
#                 horarioIni = p.horarioIni
#                 horarioFin = p.horarioFin
#                 activo = p.activo
#                 if tipo == 3:
#                     url = 'main/vendedor-ambulante-vistaAlumno-sinLogin.html'
#                     break
#                 if tipo == 2:
#                     url = 'main/vendedor-fijo-vistaAlumno-sinLogin.html'
#                     break
#                     # obtener alimentos
#     i = 0
#     listaDeProductos = []
#     for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
#         listaDeProductos.append([])
#         listaDeProductos[i].append(producto.nombre)
#         categoria = str(producto.categorias)
#         listaDeProductos[i].append(categoria)
#         listaDeProductos[i].append(producto.stock)
#         listaDeProductos[i].append(producto.precio)
#         listaDeProductos[i].append(producto.descripcion)
#         listaDeProductos[i].append(str(producto.imagen))
#         i += 1
#     listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
#     return render(request, url,
#                   {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar, "listaDeProductos": listaDeProductos,
#                    "formasDePago": formasDePago, "horarioIni": horarioIni, "horarioFin": horarioFin, "activo": activo})
#
#
# @csrf_exempt
# def editarVendedor(request):
#     if request.session.has_key('id'):
#         id = request.session['id']
#         nombre = request.session['nombre']
#         formasDePago = request.session['formasDePago']
#         avatar = request.session['avatar']
#         tipo = request.session['tipo']
#         activo = request.session['activo']
#         listaDeProductos = request.session['listaDeProductos']
#         favoritos = request.session['favoritos']
#         if (tipo == 2):
#             horarioIni = request.session['horarioIni']
#             horarioFin = request.session['horarioFin']
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "horarioIni": horarioIni, "horarioFin": horarioFin,
#                           "avatar": avatar, "listaDeProductos": listaDeProductos, "activo": activo,
#                           "formasDePago": formasDePago, "favoritos": favoritos}
#             url = 'main/editar-vendedor-fijo.html'
#         elif (tipo == 3):
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar,
#                           "listaDeProductos": listaDeProductos,
#                           "activo": activo, "formasDePago": formasDePago, "favoritos": favoritos}
#             url = 'main/editar-vendedor-ambulante.html'
#         return render(request, url, argumentos)
#     else:
#         return render(request, 'main/base.html', {})
#
#
# @csrf_exempt
# def editarDatos(request):
#     id_vendedor = request.POST.get("id_vendedor")
#     usuario = Usuario.objects.filter(id=id_vendedor)
#
#     nombre = request.POST.get("nombre")
#     tipo = request.POST.get("tipo")
#
#     if (tipo == "2"):
#         horaInicial = request.POST.get("horaIni")
#         horaFinal = request.POST.get("horaFin")
#         if (not (horaInicial is None)):
#             usuario.update(horarioIni=horaInicial)
#         if (not (horaFinal is None)):
#             usuario.update(horarioFin=horaFinal)
#             # actualizar vendedores fijos
#         for p in Usuario.objects.raw('SELECT * FROM usuario'):
#             if p.tipo == 2:
#                 hi = p.horarioIni
#                 hf = p.horarioFin
#                 horai = hi[:2]
#                 horaf = hf[:2]
#                 mini = hi[3:5]
#                 minf = hf[3:5]
#                 tiempo = str(datetime.datetime.now().time())
#                 hora = tiempo[:2]
#                 minutos = tiempo[3:5]
#                 estado = ""
#                 if horaf >= hora and hora >= horai:
#                     if horai == hora:
#                         if minf >= minutos and minutos >= mini:
#                             estado = "activo"
#                         else:
#                             estado = "inactivo"
#                     elif horaf == hora:
#                         if minf >= minutos and minutos >= mini:
#                             estado = "activo"
#                         else:
#                             estado = "inactivo"
#                     else:
#                         estado = "activo"
#                 else:
#                     estado = "inactivo"
#                 if estado == "activo":
#                     Usuario.objects.filter(nombre=p.nombre).update(activo=1)
#                 else:
#                     Usuario.objects.filter(nombre=p.nombre).update(activo=0)
#     avatar = request.FILES.get("avatar")
#     formasDePago = ""
#     if not (request.POST.get("formaDePago0") is None) and request.POST.get("formaDePago0") != "":
#         formasDePago += '0,'
#     if not (request.POST.get("formaDePago1") is None) and request.POST.get("formaDePago1") != "":
#         formasDePago += '1,'
#     if not (request.POST.get("formaDePago2") is None) and request.POST.get("formaDePago2") != "":
#         formasDePago += '2,'
#     if not (request.POST.get("formaDePago3") is None) and request.POST.get("formaDePago3") != "":
#         formasDePago += '3,'
#
#     if (nombre is not None and nombre != ""):
#         usuario.update(nombre=nombre)
#     if (formasDePago != ""):
#         usuario.update(formasDePago=formasDePago[:-1])
#     if (avatar is not None and avatar != ""):
#         with default_storage.open('../media/avatars/' + str(avatar), 'wb+') as destination:
#             for chunk in avatar.chunks():
#                 destination.write(chunk)
#         usuario.update(avatar='/avatars/' + str(avatar))
#
#     return redirigirEditar(id_vendedor, request)
#
#
# def redirigirEditar(id_vendedor, request):
#     for usr in Usuario.objects.raw('SELECT * FROM usuario WHERE id == "' + str(id_vendedor) + '"'):
#         id = usr.id
#         nombre = usr.nombre
#         email = usr.email
#         tipo = usr.tipo
#         avatar = usr.avatar
#         activo = usr.activo
#         formasDePago = usr.formasDePago
#         horarioIni = usr.horarioIni
#         horarioFin = usr.horarioFin
#         favoritos = obtenerFavoritos(id_vendedor)
#
#         request.session['id'] = id
#         request.session['nombre'] = nombre
#         request.session['formasDePago'] = formasDePago
#         request.session['avatar'] = str(avatar)
#         request.session['tipo'] = tipo
#         request.session['activo'] = activo
#         request.session['horarioIni'] = horarioIni
#         request.session['horarioFin'] = horarioFin
#         request.session['favoritos'] = favoritos
#
#         listaDeProductos = []
#         i = 0
#         url = ''
#         argumentos = {}
#         for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id_vendedor) + '"'):
#             listaDeProductos.append([])
#             listaDeProductos[i].append(producto.nombre)
#             categoria = str(producto.categorias)
#             listaDeProductos[i].append(categoria)
#             listaDeProductos[i].append(producto.stock)
#             listaDeProductos[i].append(producto.precio)
#             listaDeProductos[i].append(producto.descripcion)
#             listaDeProductos[i].append(str(producto.imagen))
#             i += 1
#
#         listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
#         request.session['listaDeProductos'] = str(listaDeProductos)
#         if (tipo == 2):
#             url = 'main/vendedor-fijo.html'
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "horarioIni": horarioIni, "horarioFin": horarioFin,
#                           "avatar": avatar, "listaDeProductos": listaDeProductos, "activo": activo,
#                           "formasDePago": formasDePago, "favoritos": favoritos}
#         elif (tipo == 3):
#             url = 'main/vendedor-ambulante.html'
#             argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar,
#                           "listaDeProductos": listaDeProductos,
#                           "activo": activo, "formasDePago": formasDePago, "favoritos": favoritos}
#         return render(request, url, argumentos)
#
#
# def inicioAlumno(request):
#     id = request.session['id']
#     vendedores = []
#     # si son vendedores, crear lista de productos
#     for p in Usuario.objects.raw('SELECT * FROM usuario'):
#         if p.id == id:
#             avatar = p.avatar
#         if p.tipo == 2 or p.tipo == 3:
#             vendedores.append(p.id)
#     vendedoresJson = simplejson.dumps(vendedores)
#     return render(request, 'main/baseAlumno.html', {"id": id, "vendedores": vendedoresJson, "avatarSesion": avatar,
#                                                     "nombresesion": request.session['nombre']})
#
#
# @csrf_exempt
# def borrarProducto(request):
#     if request.method == 'GET':
#         if request.is_ajax():
#             comida = request.GET.get('eliminar')
#             Comida.objects.filter(nombre=comida).delete()
#             data = {"eliminar": comida}
#             return JsonResponse(data)
#
#
# @csrf_exempt
# def editarProducto(request):
#     if request.method == 'POST':
#         if request.is_ajax():
#             # form = editarProductosForm(data=request.POST, files=request.FILES)
#             nombreOriginal = request.POST.get("nombreOriginal")
#             nuevoNombre = request.POST.get('nombre')
#             nuevoPrecio = (request.POST.get('precio'))
#             nuevoStock = (request.POST.get('stock'))
#             nuevaDescripcion = request.POST.get('descripcion')
#             nuevaCategoria = (request.POST.get('categoria'))
#             nuevaImagen = request.FILES.get("comida")
#             if nuevoPrecio != "":
#                 Comida.objects.filter(nombre=nombreOriginal).update(precio=int(nuevoPrecio))
#             if nuevoStock != "":
#                 Comida.objects.filter(nombre=nombreOriginal).update(stock=int(nuevoStock))
#             if nuevaDescripcion != "":
#                 Comida.objects.filter(nombre=nombreOriginal).update(descripcion=nuevaDescripcion)
#             if nuevaCategoria != None:
#                 Comida.objects.filter(nombre=nombreOriginal).update(categorias=(nuevaCategoria))
#             if nuevaImagen != None:
#                 filename = nombreOriginal + ".jpg"
#                 with default_storage.open('../media/productos/' + filename, 'wb+') as destination:
#                     for chunk in nuevaImagen.chunks():
#                         destination.write(chunk)
#                 Comida.objects.filter(nombre=nombreOriginal).update(imagen='/productos/' + filename)
#
#             if nuevoNombre != "":
#                 if Comida.objects.filter(nombre=nuevoNombre).exists():
#                     data = {"respuesta": "repetido"}
#                     return JsonResponse(data)
#                 else:
#                     Comida.objects.filter(nombre=nombreOriginal).update(nombre=nuevoNombre)
#
#             data = {"respuesta": nombreOriginal}
#             return JsonResponse(data)
#
#
# def cambiarFavorito(request):
#     if request.method == "GET":
#         if request.is_ajax():
#             favorito = request.GET.get('favorito')
#             agregar = request.GET.get('agregar')
#             if agregar == "si":
#                 nuevoFavorito = Favoritos()
#                 nuevoFavorito.idAlumno = request.session['id']
#                 nuevoFavorito.idVendedor = favorito
#                 nuevoFavorito.save()
#                 respuesta = {"respuesta": "si"}
#             else:
#                 Favoritos.objects.filter(idAlumno=request.session['id']).filter(idVendedor=favorito).delete()
#                 respuesta = {"respuesta": "no"}
#             return JsonResponse(respuesta)
#
#             # return render_to_response('main/baseAdmin.html', {'form':form,'test':test}, context_instance=RequestContext(request))
#
#
# def cambiarEstado(request):
#     if request.method == 'GET':
#         if request.is_ajax():
#             estado = request.GET.get('estado')
#             id_vendedor = request.GET.get('id')
#             if estado == "true":
#                 Usuario.objects.filter(id=id_vendedor).update(activo=True)
#             else:
#                 Usuario.objects.filter(id=id_vendedor).update(activo=False)
#             data = {"estado": estado}
#             return JsonResponse(data)
#
#
# def editarPerfilAlumno(request):
#     avatar = request.session['avatar']
#     id = request.session['id']
#     nombre = request.session['nombre']
#     favoritos = []
#     nombres = []
#     for fav in Favoritos.objects.raw("SELECT * FROM Favoritos"):
#         if id == fav.idAlumno:
#             favoritos.append(fav.idVendedor)
#             vendedor = Usuario.objects.filter(id=fav.idVendedor).get()
#             nombre = vendedor.nombre
#             nombres.append(nombre)
#     return render(request, 'main/editar-perfil-alumno.html',
#                   {"id": id, "avatarSesion": avatar, "nombre": nombre, "favoritos": favoritos, "nombres": nombres,
#                    "nombresesion": request.session['nombre']})
#
#
# def procesarPerfilAlumno(request):
#     if request.method == "POST":
#         nombreOriginal = request.session['nombre']
#         nuevoNombre = request.POST.get("nombre")
#         count = request.POST.get("switchs")
#         aEliminar = []
#         nuevaImagen = request.FILES.get("comida")
#         for i in range(int(count)):
#             fav = request.POST.get("switch" + str(i))
#             if fav != "":
#                 aEliminar.append(fav)
#
#         if nuevoNombre != "":
#             if Usuario.objects.filter(nombre=nuevoNombre).exists():
#                 data = {"respuesta": "repetido"}
#                 return JsonResponse(data)
#             Usuario.objects.filter(nombre=nombreOriginal).update(nombre=nuevoNombre)
#
#         for i in aEliminar:
#             for fav in Favoritos.objects.raw("SELECT * FROM Favoritos"):
#                 if request.session['id'] == fav.idAlumno:
#                     if int(i) == fav.idVendedor:
#                         Favoritos.objects.filter(idAlumno=request.session['id']).filter(idVendedor=int(i)).delete()
#         if nuevaImagen != None:
#             filename = nombreOriginal + ".jpg"
#             with default_storage.open('../media/avatars/' + filename, 'wb+') as destination:
#                 for chunk in nuevaImagen.chunks():
#                     destination.write(chunk)
#             Usuario.objects.filter(id=request.session['id']).update(avatar='/avatars/' + filename)
#
#         return JsonResponse({"ejemplo": "correcto"})
#
#
# @csrf_exempt
# def borrarUsuario(request):
#     if request.method == 'GET':
#         if request.is_ajax():
#             uID = request.GET.get('eliminar')
#             Usuario.objects.filter(id=uID).delete()
#             data = {"eliminar": uID}
#             return JsonResponse(data)
#
#
# @csrf_exempt
# def agregarAvatar(request):
#     if request.is_ajax() or request.method == 'FILES':
#         imagen = request.FILES.get("image")
#         # nuevaImagen = Imagen(imagen=imagen)
#         # nuevaImagen.save()
#         return HttpResponse("Success")
#
#
# def editarUsuarioAdmin(request):
#     if request.method == 'GET':
#         nombre = request.GET.get("name")
#         contraseña = request.GET.get('password')
#         email = request.GET.get('email')
#         avatar = request.GET.get('avatar')
#         userID = request.GET.get('userID')
#
#         if email != None:
#             Usuario.objects.filter(id=userID).update(email=email)
#         if nombre != None:
#             Usuario.objects.filter(id=userID).update(nombre=nombre)
#         if contraseña != None:
#             Usuario.objects.filter(id=userID).update(contraseña=contraseña)
#         if avatar != None:
#             Usuario.objects.filter(id=userID).update(avatar=avatar)
#
#         data = {"respuesta": userID}
#         return JsonResponse(data)
#
#
# def editarUsuario(request):
#     if request.method == 'GET':
#
#         nombre = request.GET.get("name")
#         contraseña = request.GET.get('password')
#         tipo = request.GET.get('type')
#         email = request.GET.get('email')
#         avatar = request.GET.get('avatar')
#         forma0 = request.GET.get('forma0')
#         forma1 = request.GET.get('forma1')
#         forma2 = request.GET.get('forma2')
#         forma3 = request.GET.get('forma3')
#         horaIni = request.GET.get('horaIni')
#         horaFin = request.GET.get('horaFin')
#         userID = request.GET.get('userID')
#
#         nuevaListaFormasDePago = ""
#         if (forma0 != None):
#             nuevaListaFormasDePago += "0"
#         if (forma1 != None):
#             if (len(nuevaListaFormasDePago) != 0):
#                 nuevaListaFormasDePago += ",1"
#             else:
#                 nuevaListaFormasDePago += "1"
#         if (forma2 != None):
#             if (len(nuevaListaFormasDePago) != 0):
#                 nuevaListaFormasDePago += ",2"
#             else:
#                 nuevaListaFormasDePago += "2"
#         if (forma3 != None):
#             if (len(nuevaListaFormasDePago) != 0):
#                 nuevaListaFormasDePago += ",3"
#             else:
#                 nuevaListaFormasDePago += "3"
#
#         litaFormasDePago = (
#             (0, 'Efectivo'),
#             (1, 'Tarjeta de Crédito'),
#             (2, 'Tarjeta de Débito'),
#             (3, 'Tarjeta Junaeb'),
#         )
#         if email != None:
#             Usuario.objects.filter(id=userID).update(email=email)
#         if nombre != None:
#             Usuario.objects.filter(id=userID).update(nombre=nombre)
#         if contraseña != None:
#             Usuario.objects.filter(id=userID).update(contraseña=contraseña)
#         if tipo != None:
#             Usuario.objects.filter(id=userID).update(tipo=tipo)
#         if avatar != None:
#             Usuario.objects.filter(id=userID).update(avatar=avatar)
#         if horaIni != None:
#             Usuario.objects.filter(id=userID).update(horarioIni=horaIni)
#         if horaFin != None:
#             Usuario.objects.filter(id=userID).update(horarioFin=horaFin)
#         Usuario.objects.filter(id=userID).update(formasDePago=nuevaListaFormasDePago)
#
#         data = {"respuesta": userID}
#         return JsonResponse(data)
#
#
# def registerAdmin(request):
#     tipo = request.POST.get("tipo")
#     nombre = request.POST.get("nombre")
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     horaInicial = request.POST.get("horaIni")
#     horaFinal = request.POST.get("horaFin")
#     avatar = request.FILES.get("avatar")
#     formasDePago = []
#     if not (request.POST.get("formaDePago0") is None):
#         formasDePago.append(request.POST.get("formaDePago0"))
#     if not (request.POST.get("formaDePago1") is None):
#         formasDePago.append(request.POST.get("formaDePago1"))
#     if not (request.POST.get("formaDePago2") is None):
#         formasDePago.append(request.POST.get("formaDePago2"))
#     if not (request.POST.get("formaDePago3") is None):
#         formasDePago.append(request.POST.get("formaDePago3"))
#     usuarioNuevo = Usuario(nombre=nombre, email=email, tipo=tipo, contraseña=password, avatar=avatar,
#                            formasDePago=formasDePago, horarioIni=horaInicial, horarioFin=horaFinal)
#     usuarioNuevo.save()
#     id = request.session['id']
#     email = request.session['email']
#     avatar = request.session['avatar']
#     nombre = request.session['nombre']
#     contraseña = request.session['contraseña']
#     return adminPOST(id, avatar, email, nombre, contraseña, request)
#
#
# @csrf_exempt
# def verificarEmail(request):
#     if request.is_ajax() or request.method == 'POST':
#         email = request.POST.get("email")
#         if Usuario.objects.filter(email=email).exists():
#             data = {"respuesta": "repetido"}
#             return JsonResponse(data)
#         else:
#             data = {"respuesta": "disponible"}
#             return JsonResponse(data)
#
#
# def getStock(request):
#     if request.method == "GET":
#         stock = request.GET.get("nombre")
#         for producto in Comida.objects.raw("SELECT * FROM Comida"):
#             if producto.nombre == request.GET.get("nombre"):
#                 stock = producto.stock
#         if request.GET.get("op") == "suma":
#             nuevoStock = stock + 1
#             Comida.objects.filter(nombre=request.GET.get("nombre")).update(stock=nuevoStock)
#         if request.GET.get("op") == "resta":
#             nuevoStock = stock - 1
#             if stock == 0:
#                 return JsonResponse({"stock": stock})
#             Comida.objects.filter(nombre=request.GET.get("nombre")).update(stock=nuevoStock)
#     return JsonResponse({"stock": stock})
#
#
# def createTransaction(request):
#     nombreProducto = request.GET.get("nombre")
#     precio = 0
#     idVendedor = request.GET.get("idUsuario")
#     if Comida.objects.filter(nombre=nombreProducto).exists():
#         precio = Comida.objects.filter(nombre=nombreProducto).values('precio')[0]
#         listaAux = list(precio.values())
#         precio = listaAux[0]
#     else:
#         return HttpResponse('error message')
#     transaccionNueva = Transacciones(idVendedor=idVendedor, precio=precio, nombreComida=nombreProducto)
#     transaccionNueva.save()
#     return JsonResponse({"transaccion": "realizada"})
#

# ------------------------- Refactoring -------------------------#
def getProductos(vendedor):
    productos = Comida.objects.filter(vendedor=vendedor).all()
    listaProductos = []

    for p in productos:
        listaProductos.append(p)
    return listaProductos


class index(View):
    @staticmethod
    def get(request):
        userDj = request.user
        if not userDj.is_authenticated():
            return render(request, 'refactoring/index.html', {'userDj': userDj, 'vendedores': getVendedores(),
                                                              'form': form_filtros()})
        user = Usuario.objects.get(usuario=userDj)
        vendedores = getVendedores()
        return render(request, 'refactoring/index.html', {'user': user, 'userDj': userDj,
                                                          'vendedores': vendedores,
                                                          'vendedores_favoritos': getVendedoresFavoritos(user, vendedores),
                                                          'form': form_filtros()})

    def post(self, request):
        userDj = request.user
        user = Usuario.objects.get(usuario=userDj)
        form = form_filtros(request.POST)
        if form.is_valid():
            filtros = form.cleaned_data['filtros']
            favoritos = form.cleaned_data['favoritos']
            vendedores = getVendedores(filtros)
            if favoritos:
                vendedores = getVendedoresFavoritos(user, vendedores)
            return render(request, 'refactoring/index.html', {'user': user, 'userDj': userDj,
                                                              'vendedores': vendedores,
                                                              'vendedores_favoritos': getVendedoresFavoritos(user, vendedores),
                                                              'form': form_filtros()})
        vendedores = getVendedores()
        return render(request, 'refactoring/index.html', {'user': user, 'userDj': userDj,
                                                          'vendedores': vendedores,
                                                          'vendedores_favoritos': getVendedoresFavoritos(user, vendedores),
                                                          'form': form_filtros()})


class Login(View):
    @staticmethod
    def get(request):
        form = Formulario_Ingreso()
        return render(request, 'refactoring/login.html', {'form': form})

    def post(self, request):
        form = Formulario_Ingreso(request.POST)
        if not form.is_valid():
            self.get(request)
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'refactoring/login.html', {
                'error': 'Usuario o contraseña invalidos', 'form': form, })
        if user.is_active:
            auth.login(request, user)
            usuario = Usuario.objects.get(usuario=user)
            tipo = usuario.tipo
            if tipo == 1:  # alumno
                return redirect('index')
            else:  # vendedor
                print('vendedor')
                return redirect('vendedorprofilepage', vendedor=usuario)
        return render(request, 'refactoring/login.html', {'form': form})


class SignUp(View):
    def get(self, request):
        form = Formulario_Registro()
        return render(request, 'refactoring/signup.html', {'form': form})

    def post(self, request):
        form = Formulario_Registro(request.POST, request.FILES)
        if form.is_valid():
            try:
                tipo = form.cleaned_data['tipo_cuenta']
                crear_usuario(tipo, form)
                return redirect('login')

            except IntegrityError:
                return render(request, 'refactoring/signup.html',
                              {'mensage': 'El usuario ya esta en uso', 'form': form})
            except KeyError as e:
                return render(request, 'refactoring/signup.html', {'message': e.args[0], 'form': form})
        else:
            form = Formulario_Registro()
            return render(request, 'refactoring/signup.html', {'form': form})


def vendedorprofilepage(request, vendedor):
    vendedorUser = Vendedor.objects.get(nombre=vendedor)
    user = request.user
    favorito = False
    metodospago = ''
    favs = 0
    usuario = None
    for m in vendedorUser.formasDePago.all():
        metodospago += m.forma + ' '
    if vendedorUser.usuario.tipo == 2:
        actualizar_actividad(vendedorUser)
    if user.is_authenticated:
        usuario = Usuario.objects.get(usuario=user)
        tipo = usuario.tipo
        if tipo == 1:
            if Favoritos.objects.filter(usuario=usuario, vendedor=vendedorUser).count() != 0:
                favorito = True
        else:
            for fav in Favoritos.objects.all():
                if fav.vendedor == vendedorUser:
                    favs += 1
    data = {
        'userDj': user,
        'user': usuario,
        'vendedor': vendedorUser,
        'vendedor_estado': 'Activo' if vendedorUser.activo else 'Inactivo',
        'vendedor_tipo': 'Vendedor fijo' if vendedorUser.usuario.tipo == 2 else 'Vendedor ambulante',
        'vendedor_metodospago': metodospago,
        'productos': getProductos(vendedorUser),
        'favorito': favorito,
        'vendedor_numero_favs': favs,
    }
    return render(request, 'refactoring/vendedor-profile-page.html', data)


class EditarPerfil(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('index')
        user = request.user
        vendedor = Vendedor.objects.get(usuario=user.usuario)
        inicial = {'nombre': user.username, 'email': user.email}
        if user.usuario.tipo == 1:
            inicial['favoritos'] = Favoritos.objects.filter(usuario=user.usuario)
        else:
            inicial['pagos'] = vendedor.formasDePago.all()
        if user.usuario.tipo == 2:
            inicial['hora_inicio'] = vendedor.horarioIni
            inicial['hora_fin'] = vendedor.horarioFin

        form = Formulario_Actualizar_Perfil(initial=inicial)
        usuario = request.user.usuario
        if request.user.usuario.tipo != 1:
            vendedor = Vendedor.objects.get(usuario=usuario)
            return render(request, 'refactoring/editar-perfil.html', {'form': form, 'userDj': request.user,
                                                                      'user': usuario, 'vendedor': vendedor})
        return render(request, 'refactoring/editar-perfil.html', {'form': form, 'userDj': request.user,
                                                                  'user': usuario})

    def post(self, request):
        form = Formulario_Actualizar_Perfil(request.POST, request.FILES)
        if not request.user.is_authenticated() or not form.is_valid():
            return self.get(request)
        user = User.objects.get(username=request.user)

        if user.check_password(form.cleaned_data['contrasena']):
            editar_usuario(user, form)
            if user.usuario.tipo == 1:
                return redirect('index')
            else:
                vendedor = Vendedor.objects.get(usuario=request.user.usuario)
                return redirect('vendedorprofilepage', vendedor=vendedor)
        return render(request, 'refactoring/editar-perfil.html', {'form': form, 'userDj': request.user, 'user': user})


class AgregarProducto(View):
    def get(self, request):
        form = Formulario_Producto()
        if request.user.usuario.tipo != 1:
            usuario = request.user.usuario
            vendedor = Vendedor.objects.get(usuario=usuario)
            return render(request, 'refactoring/agregar-productos.html', {'form': form, 'userDj': request.user,
                                                                          'user': usuario, 'vendedor': vendedor})
        return render(request, 'refactoring/agregar-productos.html', {'form': form, 'userDj': request.user,
                                                                      'user': Usuario.objects.get(usuario=request.user)})

    def post(self, request):
        form = Formulario_Producto(request.POST, request.FILES)
        if form.is_valid():
            vendedor = Vendedor.objects.get(usuario=request.user.usuario)
            agregar_producto(vendedor, form)
            return redirect('vendedorprofilepage', vendedor=vendedor)
        else:
            form = Formulario_Producto()
            return render(request, 'refactoring/agregar-productos.html', {'form': form, 'userDj': request.user,
                                                                          'user': Usuario.objects.get(usuario=request.user)})


class EditarProducto(View):
    def get(self, request, pid):
        usuario = Usuario.objects.get(usuario=request.user)
        vendedor = Vendedor.objects.get(usuario=usuario)
        productos = Comida.objects.filter(vendedor=vendedor)
        producto_inicial = productos.get(id=pid)
        form = Formulario_Producto(instance=producto_inicial)
        return render(request, 'refactoring/editar-productos.html', {'form': form, 'userDj': request.user,
                                                                     'user': usuario, 'vendedor': vendedor})

    def post(self, request, pid):
        usuario = Usuario.objects.get(usuario=request.user)
        vendedor = Vendedor.objects.get(usuario=usuario)
        productos = Comida.objects.filter(vendedor=vendedor)
        producto_inicial = productos.get(id=pid)
        form = Formulario_Producto(request.POST, request.FILES)
        if form.is_valid():
            editar_producto(producto_inicial, form)
            return redirect('vendedorprofilepage', vendedor=vendedor)
        else:
            form = Formulario_Producto()
            return render(request, 'refactoring/editar-productos.html', {'form': form, 'userDj': request.user,
                                                                         'user': request.user.usuario,
                                                                         'vendedor': vendedor})


def productos_delete(request, pid):
    usuario = Usuario.objects.get(usuario=request.user)
    vendedor = Vendedor.objects.get(usuario=usuario)
    productos = Comida.objects.filter(vendedor=vendedor)
    producto = productos.get(id=pid)
    producto.delete()
    return redirect('vendedorprofilepage', vendedor=vendedor)


def logout(request):
    auth.logout(request)
    return redirect('index')

def getStock(request):
    pid = request.GET.get("id", None)
    vendedor = Vendedor.objects.filter(id=request.GET.get("vendedor", None))
    productos = Comida.objects.filter(vendedor=vendedor)
    producto = productos.get(id=pid)
    stock = producto.stock
    if request.GET.get("op", None) == "suma":
        nuevoStock = stock + 1
        Comida.objects.filter(id=pid).update(stock=nuevoStock)
    if request.GET.get("op", None) == "resta":
        nuevoStock = stock - 1
        if stock == 0:
            return JsonResponse({"stock": stock})
        Comida.objects.filter(id=pid).update(stock=nuevoStock)
    return JsonResponse({"stock": stock})

def crearTransaccion(request):
    nombreProducto = request.GET.get("nombre")
    precio = 0
    idVendedor = request.GET.get("idUsuario")
    if Comida.objects.filter(nombre=nombreProducto).exists():
        precio = Comida.objects.filter(nombre=nombreProducto).values('precio')[0]
        listaAux = list(precio.values())
        precio = listaAux[0]
    else:
        return HttpResponse('error message')
    transaccionNueva = Transacciones(idVendedor=idVendedor, precio=precio, nombreComida=nombreProducto)
    transaccionNueva.save()
    return JsonResponse({"transaccion": "realizada"})

def change_active(request):
    usuario = Usuario.objects.get(usuario=request.user)
    vendedor = Vendedor.objects.get(usuario=usuario)
    lat = request.GET.get('lat', None)
    lng = request.GET.get('long', None)
    if lat is not None and lng is not None:
        vendedor.lat = request.GET.get('lat', None)
        vendedor.long = request.GET.get('long', None)
    vendedor.activo = not vendedor.activo
    vendedor.save()
    return HttpResponse("")


def add_favorite(request):
    user = Usuario.objects.get(nombre=request.user)
    vendedor = Vendedor.objects.get(nombre=request.GET.get('vendedor', None))
    if Favoritos.objects.filter(usuario=user, vendedor=vendedor).count() != 0:
        Favoritos.objects.filter(usuario=user, vendedor=vendedor).delete()
    else:
        nuevoFav = Favoritos(usuario=user, vendedor=vendedor)
        nuevoFav.save()
    vendedor.users.all().count()
    return HttpResponse("")


def alerta_policial(request):
    pusher_client = pusher.Pusher(
        app_id='358730',
        key='43806ba42b9b3916fd09',
        secret='a81c51a9bb4bd6b42287',
        cluster='us2',
        ssl=True
    )
    lat = request.GET.get('lat', None)
    lng = request.GET.get('long', None)
    pusher_client.trigger('canal-alerta', 'evento-alerta', {'message': '¡Cuidado! Hay policías cerca', 'lat': lat, 'lng': lng})
