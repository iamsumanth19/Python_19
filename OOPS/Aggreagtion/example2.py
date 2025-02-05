class Player():
    def __init__(self,pn,pa,pc,pnom,pr,pw):
        self.player_name=pn
        self.player_age=pa
        self.player_country=pc
        self.number_of_matches=pnom
        self.player_runs=pr
        self.player_wickets=pw
    
    def playersInfo(self):
        print(f'player name is {self.player_name}')
        print(f'player age is {self.player_age}')
        print(f'player country is {self.player_country}')
        print(f'player no.of matches are {self.number_of_matches}')
        print(f'player runs are {self.player_runs}')
        print(f'player wickets are {self.player_wickets}')

class Team():
    def __init__(self,np):
        self.LOP=[]
        self.number_of_players=np
        for i in range(1,np+1):
            pn=input('Enter Player Name:')
            pa=int(input('Enter Player age:'))
            pc=input('Enter Player Country:')
            pnom=int(input('No.of Matches player Played:'))
            pr=int(input('Enter no.of runs player scored:'))
            pw=int(input('Enter no.of wickets player taken:'))
            PCO=Player(pn,pa,pc,pnom,pr,pw)
            self.player=PCO
            self.LOP.append(self.player)

    def getMaxRunsScrorer(self):
        max_runs=0
        max_runs_scorer=''
        for i in range(len(self.LOP)):
           if self.LOP[i].player_runs>max_runs:
               max_runs=self.LOP[i].player_runs
               max_runs_scorer= self.LOP[i].player_name
        print(f'Highest run scorer is {max_runs_scorer} with {max_runs} runs!!')
    
    def getMaxWicketsScorer(self):
        max_wickets=0
        max_wickets_taker=''
        for i in range(len(self.LOP)):
           if self.LOP[i].player_wickets>max_wickets:
               max_wickets=self.LOP[i].player_wickets
               max_wickets_taker= self.LOP[i].player_name
        print(f'Highest wickets taker is {max_wickets_taker} with {max_wickets} wickets!!')
    
India=Team(5)
India.getMaxRunsScrorer()
India.getMaxWicketsScorer() 