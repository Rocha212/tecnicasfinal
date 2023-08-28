dia= int(input("ingrese el dia de la fecha: "))
mes= int (input ("ingrese el mes de la fecha: "))
ano= int (input("ingrese el año de la fecha: "))
messig=0
diasig=0
anosig=0
fechaAct= (dia, mes, ano)



if mes == 1 or 3 or 5 or 7 or 8 or 10:

    if dia == 31:
        messig= mes+1
        diasig +=1
        anosig= ano
    else:
        diasig= dia+1
        messig= mes
        anosig= ano
else:
    if dia == 30:
        messig= mes+1
        diasig +=1
        anosig= ano
    else:
        diasig= dia+1
        messig= mes
        anosig= ano

if mes == 12:
    if dia==31:
        messig = 1
        diasig =1
        anosig=ano +1
    else:
        diasig= dia+1
        messig= mes
        anosig= ano

if mes == 2:
    if dia==28:
        messig= 3
        diasig =1
        anosig=ano
    else:
        diasig= dia+1
        messig= mes
        anosig= ano

fechaSig = diasig, messig, anosig

print("La fecha actual es: ", fechaAct[0], fechaAct[1], fechaAct[2])
print("La fecha siguiente es: ", fechaSig[0], fechaSig[1], fechaSig[2])