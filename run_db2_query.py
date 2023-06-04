import sqlalchemy
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('ibm_db2',50000))
if result == 0:
   print "Port is open"
else:
   print "Port is not open"
sock.close()

db2_config = "ibm_db_sa://{}:{}@{}:{}/{}".format(
        "DB2INST1",
        "password",
        "ibm_db2",
        "50000",
        "DB2INST1",
    )        

engine = sqlalchemy.create_engine(db2_config)

with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text("select * from staff"))
    for row in result:
        print(row)
