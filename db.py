import pymysql.cursors

def connectDB():
  return pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              db='collca',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)

def getPrimaryCordData(id):
  # Connect to the database
  connection = connectDB()

  try:
      #with connection.cursor() as cursor:
          # Create a new record
      #    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
      #    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

      # connection is not autocommit by default. So you must commit to save
      # your changes.
      #connection.commit()

      with connection.cursor() as cursor:
          # Read a single record
          sql = "SELECT `KHIPU_ID`, `PCORD_ID`, `PCORD_LENGTH`, `BEGINNING`, `TERMINATION`, `TWIST` FROM `primary_cord` WHERE `KHIPU_ID`=%s"
          cursor.execute(sql, (id,))
          result = cursor.fetchone()
          #print(type(result))
          #print(result['KHIPU_ID'])
          return result
  finally:
      connection.close()

def getClusterCords(id):
  connection = connectDB()
  try:
      with connection.cursor() as cursor:          
          sql = "SELECT `CLUSTER_ID`, `START_POSITION`, `END_POSITION`, `NUM_CORDS` FROM `cord_cluster` WHERE `CORD_ID`=%s"
          cursor.execute(sql, (id,))
          result = cursor.fetchall()
          return result
  finally:
      connection.close()

def getCords(id):
  connection = connectDB()
  try:
      with connection.cursor() as cursor:
          sql = "SELECT `CORD_ID`,`CORD_LENGTH` FROM `cord` WHERE `CLUSTER_ID`=%s"
          cursor.execute(sql, (id,))
          result = cursor.fetchall()
          return result
  finally:
      connection.close()

if __name__ == "__main__":
    result = getPrimaryCordData("1000000")
    print(result)

    cluster = getClusterCords("1000000")
    print(len(cluster))
