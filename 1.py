import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="medicines"
)

c = db.cursor()
c.execute("INSERT INTO medicines (name, disease) VALUES (%s, %s);", ('Антифлу Кидс', 'симптоматическое лечение простудных заболеваний, гриппа, ОРВИ'))
db.commit()
c.close()
db.close()