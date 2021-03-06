from consumo_api import get_weather_city


print("BIENENIDO A LA APP DE CLIMA")



print("Ingresar 1 para buscar por ciudad ")
print("Ingresar 2 para buscar por lat y long")
print("Ingresar un valor distinto para salir")  
print()

user = input("Porfavor, Ingrese su opcion:" )


while ( user == "1" or user== "2" ):

    print("Ingresar 3 para ver pronostico de ahora")
    print("Ingresar 4 para ver pronostico dentro de 5 dias")
    
    print()
    pronostico =  input ("Porfavor, Ingrese su opcion:")   


    # pronostico de ahora por ciudad
    if user == "1" and pronostico == "3":
        city = input("Ingresar una ciudad: ")
        params  = {}
        params["q"] = city
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"
        params["units"] = "metric"
        
        url = "https://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url,params)

       
        clima2 = (clima["main"])

        print ("El clima de la ciudad de",clima["name"],"es: " )
        # clima2_ordenado = sorted(clima2.items()) 
        
        for i in clima2:
            print(i, ":",clima2[i])



    # pronostico de ahora porlat lon  
    elif user == "2" and pronostico == "3":
        lat= input("Ingresar la latitud: ")
        lon= input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"

        url_coordenadas = "http://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url_coordenadas,params)

        clima2 = (clima["main"])

        print ("El clima de la ciudad de",clima["name"],"es: " )
        for i in clima2:
            print(i, ":",clima2[i])
        

    # ver pronostico 4 dias ciudad
    if user == "1" and pronostico == "4":
        city = input("Ingresar una ciudad para pronostico de 5 dias: ")
        params  = {}
        params["q"] = city
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"
        params["units"] = "metric"
        

        url = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url,params)

        print()

        fecha = clima["list"][1]["dt_txt"]
        # datos = clima["list"][1]["cloud"]   swind visibility rain
        datos = clima["list"][1]["main"]
        print("El tiempo para",city, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])


        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]["main"]
        print()
        print("El tiempo para",city, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])



        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]["main"]
        print()
        print("El tiempo para",city, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])


        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]["main"]
        print()
        print("El tiempo para",city, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])
       

        fecha = clima["list"][35]["dt_txt"]
        datos = clima["list"][35]["main"]
        print()
        print("El tiempo para",city, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])


    # ver pronostico 4 dias por lat lon
    elif user == "2" and pronostico == "4":
        lat= input("Ingresar la latitud: ")
        lon=  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"

        url_coordenadas = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url_coordenadas,params)

        print()
       
        fecha = clima["list"][1]["dt_txt"]
        datos = clima["list"][1]["main"]

        print("El tiempo para la latitud",lat,"y la longitud",lon,"en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])


        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]["main"]
        print()
        print("El tiempo para la latitud",lat,"y la longitud",lon,"en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])

        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]["main"]
        print()
        print("El tiempo para la latitud",lat,"y la longitud",lon,"en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])

        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]["main"]
        print()
        print("El tiempo para la latitud",lat,"y la longitud",lon, "en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])

        fecha = clima["list"][35]["dt_txt"]
        datos = clima["list"][35]["main"]
        print()
        print("El tiempo para la latitud",lat,"y la longitud",lon,"en el dia",fecha, "es de: ")
        for i in datos:
            print(i, ":",datos[i])

    print()
    print("Ingresar 1 para buscar por ciudad ")
    print("Ingresar 2 para buscar por lat y long")
    print("Ingresar un valor distinto para salir") 
    
    print()

    user = input("Porfavor, Ingrese su opcion:" )

print("Gracias por usar nuestra app")