from datetime import datetime, date

# datetime
print("fecha:", datetime.now())
print("anio: ", datetime.now().year)

print("anio:      ", datetime.now().strftime("%Y"))
print("mes:       ", datetime.now().strftime("%m"))
print("dia:       ", datetime.now().strftime("%d"))
print("mes anio:  ", datetime.now().strftime("%B"))
print("dia semana:", datetime.now().strftime("%A"))
print("hora formato 12h:", datetime.now().strftime("%I"))
print("hora formato 24h:", datetime.now().strftime("%H"))
print("am/pm:     ", datetime.now().strftime("%p"))
print("minutos:   ", datetime.now().strftime("%M"))
print("segundos:  ", datetime.now().strftime("%S"))
print("UTC:       ", datetime.now().strftime("%z"))
print("time zone: ", datetime.now().strftime("%Z"))
print("date:      ", datetime.now().strftime("%x"))
print("time:      ", datetime.now().strftime("%X"))
print("date and time:", datetime.now().strftime("%c"))

print(datetime(2020,5,28))

# date
print("hoy:", date.today())