# ------ SQL to DataFrame

import mysql.connector

host = 'example.rds.amazonaws.com'
database = 'dbname'
user = 'admin'
password = 'password'
port = 3306

# Conectando
con = mysql.connector.connect(user=user, 
                              password=password,
                              host=host,
                              database=database)

# Puxando as informações para um dataframe
df = pd.read_sql_query("SELECT * from sales_data", con)

# Fechando a conexão
con.close()



# ------ DataFrame to SQL

from sqlalchemy import create_engine

textEngine = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(user,password,host,3306,database)
engine = create_engine(textEngine, echo=False)

df.to_sql('Produtos', con=engine, if_exists='append')
con.close()

