from database import Database
from experiment import Experiment
from config import DB_POSTGRES_PASSWORD


Database.initialise(
    database="experiments_db",
    host="localhost",
    port="5444",
    user="hello_viewer",
    password=DB_POSTGRES_PASSWORD
)


data = [(1, 3, 5), (2, 5, 7)]
Experiment.insert_data(data)
# Experiment.delete_data()
data = Experiment.execute("SELECT * FROM experiment1")
print(data)
