from datetime import date, datetime
import csv
carga=True
with open('Gastos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    ct = datetime.now()
    print(ct)
    field = ["FECHA", "MONTO", "TIPO"]
    writer.writerow(field)
    while carga:
        print("Ingrese Fecha: (AA-MM-DD)")
        ano = int(input('AÑO: '))
        mes = int(input('MES: '))
        dia = int(input('DIA: '))
        fecha = date(ano, mes, dia)
        print("Ingrese Monto €:$$$.¢¢")
        monto = (input("{:.2f}"))
        print("Ingrese Tipo Gasto: (Super-Otro-Etc)")
        gasto = str(input())
        writer.writerow([fecha,monto,gasto])
        carga = bool(input('Carga otro dato y/n?:'))
        