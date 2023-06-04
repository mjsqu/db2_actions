import sqlalchemy

db2_config = "ibm_db_sa://{}:{}@{}:{}/{}".format(
        "DB2INST1",
        "password",
        "ibm_db2",
        "50000",
        "DB2INST1",
    )        

engine = create_engine(db2_config)

with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text("select * from staff"))
    for row in result:
        print(row)
