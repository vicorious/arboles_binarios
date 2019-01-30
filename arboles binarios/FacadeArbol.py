import json
import sys
import logging
import os

from Nodo import Nodo

class FacadeArbol:

    logging.basicConfig(filename="test.log", level=logging.DEBUG)

    def __init__(self):
        pass

    def createTree(self, _json):
        nombre_archivo = "Arbol"
        nombre_archivo_final = ''
        path = "./files"
        try:                        
            files = os.listdir("./files")
            nombre_archivo_final = path+"/"+ str(len(files) + 1) + nombre_archivo
            logging.debug('Nombre archivo: '+path+"/"+nombre_archivo_final)
            logging.debug('Nombre archivo: '+str(len(_json["data"])))
            f = open(nombre_archivo_final, "w")
            for value in _json["data"]:
                f.write(value["value"] + "\n")
                logging.debug('val: '+value["value"])
            f.close()
            return (str(len(files) + 1) + nombre_archivo), id
        except Exception as e:
            logging.debug('Error creando el arbol, por favor intente de nuevo')
            raise Exception('Error creando el arbol, por favor intente de nuevo: {}'.format(e.args[0]))
        finally:
            pass
        return nombre_archivo_final

    def arbol_built(self, _arbol, _valor_1, _valor_2):   
        nodos         = []             
        try:	
            nodo_raiz     = Nodo("",None, None)
            path = "./files"
            file 		  = open(path+"/"+_arbol, "r")
            readlines     = file.readlines()
            i = 0
            nivel = 0
            nodo_raiz = Nodo("",None, None)
            for line in readlines:
                nodo_anterior = Nodo("",None, None)
                split = line.split(",")
                logging.debug('Entro. Linea: '+line)
                if i == 0:
                    nivel = len(split)
                    logging.debug('Nivel: '+str(nivel))
                    nodo_raiz = Nodo(split[0],None, None)
                    nodos.append(nodo_raiz)
                i = 0
                j = 0
                for nodo_i in split:
                    try:
                        if nodos[i].nombre == nodo_i:#Si esta repetido
                            nodo_anterior = nodos[i] 
                            nodo_anterior.nombre = nodo_i
                            continue
                        
                        for nodo_a in nodos : 
                            if nodo_a.nombre == nodo_i:  
                                nodo_anterior = nodo_a 
                                nodo_anterior.nombre = nodo_i
                                j = 1 
                                break                              
                    except Exception:
                        pass
                    if j == 1:
                        j = 0
                        continue
                    nodo_hijo = Nodo(nodo_i,None, None)
                    if nodo_anterior.nombre is None:
                        continue
                    if nodo_anterior.nodo_der is None:
                        nodo_anterior.nodo_der = nodo_hijo 
                        logging.debug('nodo der '+nodo_anterior.nombre+"=>"+nodo_anterior.nodo_der.nombre)    
                    elif nodo_anterior.nodo_izquier is None :#and nodo_anterior.nombre is not nodo_raiz.nombre:
                        nodo_anterior.nodo_izquier = nodo_hijo
                        logging.debug('nodo izquier '+nodo_anterior.nombre+"<="+nodo_anterior.nodo_izquier.nombre)    
                    #nodos[i] = nodo_anterior
                    nodo_anterior = nodo_hijo                  
                    nodos.append(nodo_anterior)
                    i += 1
                file.close()
        except Exception as e:
            logging.debug('Error hallando el ancestor, por favor intente de nuevo')
            raise Exception('Error hallando el ancestor, por favor intente de nuevo: {}'.format(e.args[0]))
        finally:
            nombre_archivo_2 = "Arbol"
            path_2 = "./graphs"        
            files_2 = os.listdir("./graphs")
            nombre_archivo_final_2 = path_2+"/"+str((len(files_2) + 1)) + nombre_archivo_2
            for nodo_b in nodos:
                logging.debug('Nodo_b: '+nodo_b.nombre)
            logging.debug('Nombre archivo final de salida: '+nombre_archivo_final_2)
            with open(nombre_archivo_final_2, 'w') as file:
                for k in range(len(nodos)):
                    try:
                        try:
                            if nodos[k].nodo_der is None:
                                continue
                            file.write("=>"+nodos[k].nodo_der.nombre)
                        except Exception:
                            pass
                        try:
                            if nodos[k].nombre is None:
                                continue
                            file.write("_"+nodos[k].nombre)
                        except Exception:
                            pass
                        try:
                            if nodos[k].nodo_izquier is None:
                                continue
                            file.write("<="+nodos[k].nodo_izquier.nombre)
                        except Exception:
                            pass
                    except Exception as e:
                        logging.debug('Error escribiendo el archivo de salida. intente de nuevo')
                        raise Exception('Error escribiendo el archivo de salida. intente de nuevo{}'.format(e.args[0]))
                    finally:
                        pass
            # algoritmo
            for nodo_a in nodos : 
                if nodo_a.nombre == nodo_raiz.nombre:  
                    nodo_e = nodo_a 
                    nodo_e.nombre = nodo_a.nombre 
                    break
            ### raiz
            l = False
            n = False
            nodo_iz = 0
            nodo_der = 0
            camino_der_1 = []
            camino_iz_1  = []
            camino_der_2 = []
            camino_iz_2  = []
            # si esta 1 Y 2 en el nodo. el uno a la derecha el segundo a la izquierda
            for nodo_i in nodos:
                if nodo_i.nodo_der.nombre == _valor_1:
                    l = True
                    camino_der_1.append(nodo_i.nombre)    
                elif nodo_i.nodo_izquier.nombre == _valor_2:
                    n = True
                    camino_iz_1.append(nodo_i.nombre)

            if not l:
                camino_der_1 = []
                for nodo_p in nodos:
                    if nodo_p.nodo_izquier.nombre == _valor_1:
                        l = True
                        nodo_iz += 1
                        break
            if not n:
                nodo_der = 0
                for nodo_h in nodos:
                    if nodo_h.nodo_der.nombre == _valor_2:
                        n = True
                        nodo_iz += 1
                        break




            
            
        return nodos
            
    

        