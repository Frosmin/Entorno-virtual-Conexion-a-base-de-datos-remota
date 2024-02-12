import psycopg2

try:
    connection = psycopg2.connect(
        user="pruebasql_user",
        password="ID98dNJyzjw5vkpsRS73IUzDd0tHb5wV",
        host="dpg-cn4ov1la73kc738ks4jg-a.oregon-postgres.render.com",
        port="5432",    
        database="pruebasql"
    )
    print("Connection established")
    
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM persona")
    
    rows = cursor.fetchall()
    for row in rows:
       print(row)
    
    
    
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)