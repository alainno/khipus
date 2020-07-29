import pymysql.cursors

class DB:

  connection = None

  def connectDB(self):
    self.connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='collca',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

  def getPrimaryCordData(self, id):
    try:
        #with connection.cursor() as cursor:
            # Create a new record
        #    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        #connection.commit()

        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `KHIPU_ID`, `PCORD_ID`, `PCORD_LENGTH`, `BEGINNING`, `TERMINATION`, `TWIST` FROM `primary_cord` WHERE `KHIPU_ID`=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            #print(type(result))
            #print(result['KHIPU_ID'])
            return result
    finally:
        #connection.close()
      pass
  
  def getClusterCords(self, id):
    try:
        with self.connection.cursor() as cursor:          
            sql = "SELECT `CLUSTER_ID`, `START_POSITION`, `END_POSITION`, `NUM_CORDS` FROM `cord_cluster` WHERE `CORD_ID`=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return result
    finally:
        #connection.close()
      pass

  def getCords(self, id):
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT `CORD_ID`,`CORD_LENGTH`,`TWIST`,`TERMINATION` FROM `cord` WHERE `CLUSTER_ID`=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return result
    finally:
        #connection.close()
      pass

  def getKnotClusters(self, cord_id):
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT `CLUSTER_ID`,`START_POS` FROM `knot_cluster` WHERE `cord_id`=%s"
            cursor.execute(sql, (cord_id,))
            result = cursor.fetchall()
            return result
    finally:
        #connection.close()
      pass

  def getKnotCluster(self, cluster_id):
    try:
        with self.connection.cursor() as cursor:
            sql = "SELECT `KNOT_ID`,`NUM_TURNS` FROM `knot` WHERE `cluster_id`=%s"
            cursor.execute(sql, (cluster_id,))
            result = cursor.fetchall()
            return result
    finally:
        #connection.close()
      pass

  def close(self):
    self.connection.close()

if __name__ == "__main__":
    result = getPrimaryCordData("1000000")
    print(result)

    cluster = getClusterCords("1000000")
    print(len(cluster))
