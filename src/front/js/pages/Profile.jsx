//leer el token de localStorage localStorage.getItem("token")
//hacer un fetch "GET", header (aqui tengo mmandar el token)
//tenemos q preguntarnos cuales de los endpoints necesitan token y cuales no. Y eso lo defino en el back en routes.py (si tiene el decorador "@jwt_required" necesita token)
//