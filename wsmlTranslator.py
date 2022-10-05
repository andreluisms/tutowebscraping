import webscraping as ws

instanceTeams = set()
instanceDates = set()
instanceGames = []
def generatewsml():
   instances = ''
   for instance in instanceTeams:
      instances += instance + '\n\n'
   for instance in instanceDates:
      instances += instance + '\n\n'
   for instance in instanceGames:
      instances += instance + '\n\n'
   return instances

def generateInstanceTeams(data):
   team1 = 'instance ' + data[2].replace(' ', '').replace('-', '') + ' memberOf Team'
   team1 += '\n   name hasValue ' + '"'+ data[2].strip() + '"' 
   team2 = 'instance ' + data[4].replace(' ', '').replace('-', '') + ' memberOf Team'
   team2 += '\n   name hasValue ' + '"'+ data[4].strip() + '"' 
   return (team1, team2)

def generateInstanceDates(splitData):
   instanceData = 'instance date' + splitData[0]
   instanceData += splitData[1] + splitData[2] + ' memberOf Date \n'
   instanceData += '   day hasValue ' + splitData[0] + '\n'
   instanceData += '   month hasValue "' + splitData[1] + '"\n'
   instanceData += '   year hasValue ' + splitData[2]
   return instanceData

def generateInstanceGames(splitData, data, i):
   instanceGame = 'instance game' + str(i) + ' memberOf HockeyGame\n'
   instanceGame+= '   season hasValue "' + data[0] + '"\n'
   instanceGame+= '   date hasValue ' + "date" + splitData[0] 
   instanceGame+= splitData[1] + splitData[2] + '\n'
   instanceGame+= '   homeTeam hasValue ' + data[2].replace(' ', '').replace('-', '') + '\n'
   instanceGame+= '   awayTeam hasValue ' + data[4].replace(' ', '').replace('-', '') + '\n'
   instanceGame+= '   htScore hasValue ' + data[3] + '\n'
   instanceGame+= '   atScore hasValue ' + data[5]
   return instanceGame

dataset = ws.webscrapingFlyerhistory()
#instruções
#Criar instância dos times
#Criar instâncias das datas dos jogos
#Criar instância dos jogos
i = 0
for data in dataset[1:]:
   teams = generateInstanceTeams(data)
   instanceTeams.add(str(teams[0]))
   instanceTeams.add(str(teams[1]))
   splitData = data[1].split('-')
   instanceDates.add(generateInstanceDates(splitData))
   instanceGames.append(generateInstanceGames(splitData, data, i))
   i+=1

print(generatewsml())
