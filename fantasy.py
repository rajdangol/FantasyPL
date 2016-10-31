import json, requests
from pprint import pprint
from termcolor import colored

league = 245425

url = 'https://fantasy.premierleague.com/drf/leagues-classic-standings/%s?phase=1&le-page=1&ls-page=1' %(league)

req = requests.get(url)
req.raise_for_status()

data = json.loads(req.text)

def main():
  print (colored('{:<10}'.format('id'),'green') + colored('{:<24}'.format('name'),'green') + colored('{:<22}'.format('team'),'green') 
  + colored('{:<8}'.format('points'),'green') + colored('{:<8}'.format('total'),'green'))

  display()
  # print data.keys()
''' [u'new_entries', u'league', u'standings', u'update_status'] '''


def display():
  for i in range(0,len(data['standings']['results'])):
    standings_data = data['standings']['results'][i]
    
    sign = u'\u25CF'                                      #equlibrium sign
    if standings_data['movement']=='up':
      sign = colored(u'\u25B2','green')                   #up sign
    elif standings_data['movement']=='down':
      sign = colored(u'\u25BC','red')                     #down sign    
 
    # print standings_data.keys()
    '''  [u'rank_sort', u'event_total', u'league', u'rank', u'own_entry', u'entry_name',
    u'stop_event', u'entry', u'player_name', u'start_event', u'total', u'last_rank', u'id', u'movement']'''


    print ('{:<10}'.format(str(standings_data['id'])) + '{:<2}'.format(str(i+1)) + '{:<22}'.format(str(standings_data['player_name'])) + 
    '{:<22}'.format(str(standings_data['entry_name']))  + '{:<8}'.format(str(standings_data['event_total'])) + 
    '{:<8}'.format(str(standings_data['total'])) + sign)
    print ('')
    

if __name__=="__main__":
  main()
