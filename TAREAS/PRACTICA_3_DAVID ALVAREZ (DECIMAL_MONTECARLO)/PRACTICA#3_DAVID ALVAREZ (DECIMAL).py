print("PROGRAMA QUE TRANSFORMA DE BINARIO A DECIMAL Y VICEVERSA")
print("Seleccione si es binario o decimal:")
###########modificar el conversor#############
conversor=input()
##############################################

if conversor=="decimal":
  print("Teclee el numero decimal:")
  ##########modificar el numero########
  numero=int(input())
  ####################################
  print("El numero",numero)
  deci=[]
  while numero>0:
    residuo=numero%2
    numero=numero//2
    deci.append(residuo)
  else:
    num_bin=deci[::-1]
    print("En binario es:",num_bin)
    
    
else:
  if conversor=="binario":
    print("Teclee el numero binario")
    ############modificar el numero###########
    Bin=int(input())
    #############modificar el numero############
    print("El numero binario:",Bin)
    bina=list(str(Bin))
    largo=len(bina)
    reverso=bina[::-1]
    lista_bin=[]
    for i in range(largo):
      num_bin=(2**i)*(int(reverso[i]))
      lista_bin.append(num_bin)
    print("En numero decimal es:",sum(lista_bin))
  else:
    print("Teclee de nuevo la opcion")
