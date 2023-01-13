from datetime import datetime, date

# print(datetime.utcnow())

hora_fecha_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(type(hora_fecha_str))
print(hora_fecha_str)

hora_fecha_dat = datetime.strptime(hora_fecha_str, "%Y-%m-%d %H:%M:%S")
print(type(hora_fecha_dat))
print(hora_fecha_dat)

print(date.today())