import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Shang-Chi and the Legend of the Ten Rings','Simu Liu','Awkwafina','Destin Daniel Cretton',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('vikram','kamal','jayanthi ','Denis Villeneuve',2023)")
pointer.execute("INSERT INTO MOVIES VALUES('Master','vijay','mala akka','Jon Watts',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Fifty shades of gray','Jami Darmon','Dakota','Jon Watts',2016)")
pointer.execute("INSERT INTO MOVIES VALUES('No one love me','Jayanthi','Sundar','Jon Watts',2011)")
pointer.execute("INSERT INTO MOVIES VALUES('Avengers','Tonny Stark','Rashmika','Karthishwaren',2023)")
pointer.execute("INSERT INTO MOVIES VALUES('Ashiqui','Syed','Rashmika','Karthishwaren',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('After','Moosa','Rashmika','Karthishwaren',2023)")

allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

name=input("enter the actor name: ")
hell=input("enter the actoress name: ")
print("************************Actor Query************************")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = '"+name+"'and ACTRESS='"+hell+"' ").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
  