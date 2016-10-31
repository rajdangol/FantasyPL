import json, requests
from pprint import pprint
from termcolor import colored

league = 245482               #league code

url = 'https://fantasy.premierleague.com/drf/leagues-h2h-standings/%s?phase=1&le-page=1&ls-page=1' %(league)

req = requests.get(url)
req.raise_for_status()

data = json.loads(req.text)

# print data.keys()          #dictionary keys
'''[u'new_entries', u'league', u'standings', u'matches_next', u'matches_this']'''


# print data['matches_this']['results'][0].keys()       #dictionary keys
''' [u'entry_2_draw', u'entry_2_entry', u'entry_1_name', u'entry_1_total', u'entry_2_loss', 
u'id', u'tiebreak', u'entry_1_player_name', u'entry_1_points',
u'entry_2_points', u'winner', u'event', u'entry_2_win', u'entry_2_name', u'entry_1_win', u'entry_1_loss',
u'entry_2_player_name', u'seed_value', u'is_knockout', u'entry_1_entry', u'own_entry', u'entry_1_draw', u'entry_2_total']'''



def main():
  print (colored('{:<20}'.format('player'),'green') + colored('{:<8}'.format('points'),'green') +  colored('{:<8}'.format('points'),'green')
    + colored('{:<20}'.format('player'),'green'))
  
  display_matches()         #matches display call

  print '\n'

  print (colored('{:<10}'.format('id'),'green') + colored('{:<24}'.format('name'),'green') + colored('{:<22}'.format('team'),'green')
  + colored('{:<8}'.format('score'),'green') + colored('{:<10}'.format('points'),'green'))

  display_league()          #league display call


def display_matches():
  def formatted_display():

    print (colored('{:<20}'.format(h2h_data['entry_1_player_name']),'green' if h2h_data['entry_1_points'] == max_points 
    else 'red' if (h2h_data['entry_1_points'] == max_points or h2h_data['entry_1_points'] == min_points) else 'white') + 
    colored('{:<8}'.format(str(h2h_data['entry_1_points'])), 'green' if h2h_data['entry_1_points'] == max_points
    else 'red' if (h2h_data['entry_1_points'] == max_points or h2h_data['entry_1_points'] == min_points) else 'white') + 
    colored('{:<8}'.format(str(h2h_data['entry_2_points'])),'green' if h2h_data['entry_2_points'] == max_points
    else 'red' if (h2h_data['entry_2_points'] == max_points or h2h_data['entry_2_points'] == min_points) else 'white') + 
    colored('{:<20}'.format(h2h_data['entry_2_player_name']),'green' if h2h_data['entry_2_points'] == max_points
    else 'red' if (h2h_data['entry_2_points'] == max_points or h2h_data['entry_2_points'] == min_points) else 'white'))

  for i in range(0, len(data['matches_this']['results'])):
    h2h_data = data['matches_this']['results'][i]
    formatted_display()

  # print h2h_data.keys()
  '''[u'entry_2_draw', u'entry_2_entry', u'entry_1_name', u'entry_1_total', u'entry_2_loss',
   u'id', u'tiebreak', u'entry_1_player_name', u'entry_1_points',
    u'entry_2_points', u'winner', u'event', u'entry_2_win', u'entry_2_name', u'entry_1_win', u'entry_1_loss',
     u'entry_2_player_name', u'seed_value', u'is_knockout', u'entry_1_entry', u'own_entry', u'entry_1_draw', u'entry_2_total']'''




def display_league():
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
    '{:<22}'.format(str(standings_data['entry_name']))  + '{:<8}'.format(str(standings_data['points_for'])) + 
    '{:<8}'.format(str(standings_data['points_total'])) + sign)
    print ('')

points_list=[]
for i in range(0,len(data['matches_this']['results'])):
  h2h_data = data['matches_this']['results'][i]
  points_list.append(h2h_data['entry_1_points'])
  points_list.append(h2h_data['entry_2_points'])
# print points_list

max_points = max(points_list)
min_points = min(points_list)

if __name__=="__main__":
  main()
