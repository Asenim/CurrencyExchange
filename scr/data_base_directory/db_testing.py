import sqlite3
from scr.Get_Package import Get_Class_Console_Output


db = sqlite3.connect('admin_db.db')


getter = Get_Class_Console_Output.GetOutput(db)

getter.get_all_currency('Currencies')

db.close()
