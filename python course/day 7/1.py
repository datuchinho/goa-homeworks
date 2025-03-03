password = input("sheiyvanet paroli: ")  

correct_password = "datvi12"
cda = 1  

while password != correct_password and cda < 3:
    password = input("paroli arasworia, cadet xelaxla: ")  
    cda += 1  

if password == correct_password:
    print("paroli sworia")  

else:
    print("3 cda amoiwura,scadet mogvianebit")