#Utility Module
#Module Date/Time

import datetime
result=datetime.datetime.now() # Current
print(result)
print(result.day)
print(result.month)
print(result.year)

appointment=datetime.datetime(2020,2,25,15,30) #yyyy,m,d,time hr,time min,time sec
# print(appointment)

#จัดรูปแบบการแสดงผล
#Date
print(result.strftime("%x")) # m/d/y
print(result.strftime("%X")) # Time
print(result.strftime("%c")) # Sun_Feb_date:21_time_year
print(result.strftime("%d")) # Date
print(result.strftime("%a")) # Show day %a or %A(Full)
print(result.strftime("%b")) # Show mouth %b or %B(Full)
print(result.strftime("%y")) # year %y or %Y(Full)

# date/mouth/year
print(result.strftime("%d/%b/%y"))

#Time
print(result.strftime("%M")) #show time only minute "%M"
print(result.strftime("%H : %M : %S : %p")) # Hr:Min:Sec:AM or PM
