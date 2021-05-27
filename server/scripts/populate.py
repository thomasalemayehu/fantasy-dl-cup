from main import db, Players, Dept, Users, userPlayers

def populate():
    userPlayers.query.delete()
    Players.query.delete()
    Dept.query.delete()
    Users.query.delete()


    dept1 = Dept(id=1, dName='IT')
    dept2 = Dept(id=2, dName='Mech')
    dept3 = Dept(id=3, dName='Elec')
    dept4 = Dept(id=4, dName='SE')
    dept5 = Dept(id=5, dName='Chemical')
    dept6 = Dept(id=6, dName='BioMed')

    p1 = Players(id=1,fname="Manu", lname="GK", position="goalkeeper", dept_id=1)
    p2 = Players(id=2,fname="Fanny", lname="Gk", position="goalkeeper", dept_id=2)
    p3 = Players(id=3,fname="Lola", lname="DF", position="defender", dept_id=1)
    p4 = Players(id=4,fname="Abe", lname="DF", position="defender", dept_id=2)
    p5 = Players(id=5,fname="Dube", lname="DF", position="defender", dept_id=3)
    p6 = Players(id=6,fname="Ni", lname="MD", position="midfielder", dept_id=1)
    p7 = Players(id=7,fname="Chang", lname="MD", position="midfielder", dept_id=2)
    p8 = Players(id=8,fname="Meh", lname="MD", position="striker", dept_id=3)
    p9 = Players(id=9,fname="Dude", lname="ST", position="striker", dept_id=1)
    p10 = Players(id=10,fname="Sportsguy", lname="ST", position="striker", dept_id=2)
    p11 = Players(id=11,fname="Sportsguys'sBrother", lname="MD", position="midfielder", dept_id=4)
    p12 = Players(id=12,fname="Ranjit", lname="GK", position="goalkeeper", dept_id=4)
    p13 = Players(id=13,fname="Kumal", lname="GK", position="goalkeeper", dept_id=5)
    p14 = Players(id=14,fname="Dud", lname="DF", position="defender", dept_id=4)
    p15 = Players(id=15,fname="Kman", lname="DF", position="defender", dept_id=5)
    p16 = Players(id=16,fname="Malik", lname="DF", position="defender", dept_id=6)
    p17 = Players(id=17,fname="Jman", lname="MD", position="midfielder", dept_id=5)
    p18 = Players(id=18,fname="Q", lname="MD", position="midfielder", dept_id=6)
    p19 = Players(id=19,fname="Pla", lname="ST", position="striker", dept_id=4)
    p20 = Players(id=20,fname="Finally", lname="ST", position="striker", dept_id=5)

    u1 = Users(id=1, fname="User1",lname="first",teamname="hope")
    u2 = Users(id=2, fname="User2",lname="second",teamname="cope")
    u3 = Users(id=3, fname="Users3",lname="third",teamname="rope")


    up1 = userPlayers(id=1,user_id=1,players_id=4)
    up2 = userPlayers(id=2,user_id=1,players_id=5)
    up3 = userPlayers(id=3,user_id=1,players_id=6)
    up4 = userPlayers(id=4,user_id=1,players_id=7)
  


    up5 = userPlayers(id=6,user_id=2,players_id=4)
    up6 = userPlayers(id=7,user_id=2,players_id=5)
    up7 = userPlayers(id=8,user_id=2,players_id=6)
    up8 = userPlayers(id=9,user_id=3,players_id=7)
    up9 = userPlayers(id=10,user_id=3,players_id=8)








    db.session.add_all([dept1, dept2, dept3, dept4, dept5, dept6, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,u1,u2,u3,up1,up2,up3,up4,up5,up6,up7,up8,up9])
    # up1,up2,up3,up4,up5,up6,up7,up8,up9
    db.session.commit()