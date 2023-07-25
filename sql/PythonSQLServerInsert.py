import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'

        'Server=.;'

        'Database=poc;'

        'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('INSERT INTO [dbo].[stat] ([Sample],[DataValue]) VALUES (1, 12.5)')

conn.commit()