#Usually, calsses names start with upercase letter
#CLASS DEFINITION
class FootballPlayer:
    #Class attribute
    sport = 'football'

    #CONSTRUCTOR FUNCTION - This is called immediately when you create an object
    #self must be the 1st arguement,the rest are used as values for OBJECT ATTRIBUTES
    def __init__(self,name,club,number,nationality,goals):
        self.name = name
        self.club = club
        self.number = number
        self.nationality = nationality
        self.goals = goals

#--------------------------------------------------------------

#CREATING AN OBJECT
player1 = FootballPlayer("Lionel Messi","Inter Miami",10,"Argentina",928)
print(player1.name)
print(player1.club)
print(player1.number)
print(player1.nationality)
print(player1.goals)

print(player1.sport)

player2 = FootballPlayer("Kylian Mbappe","Real Madrid",10,"France",420)
print(player2.name)
print(player2.club)
print(player2.number)
print(player2.nationality)
print(player2.goals)