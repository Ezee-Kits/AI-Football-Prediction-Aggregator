from func import requests_init,saving_files,drop_duplicate,sorting_values,save_daily_csv,match_day_date
from bs4 import BeautifulSoup
import requests


def footballsupertips_func():
    full_path = save_daily_csv()
    path = f'{full_path}/footballsupertips.csv'
    if match_day_date ==1:
        url = 'https://www.footballsuper.tips/tomorrows-free-football-super-tips/'
    else:
         url = 'https://www.footballsuper.tips/todays-free-football-super-tips/'

    soup,_ = requests_init(url=url)
    #   GETTING LINK SECTION
    links = [name.get('href') for name in soup.findAll('a')]
    # print(links)

    all_link = []
    for link in links:
        try:
            if link.startswith('https://www.footballsuper.tips/predictions-tips-') and link not in all_link:
                all_link.append(link)
        except:
            pass
    # USING LINKS TO GET ELEMENT IN THAT TEAMS
    # print(all_link)
    print('LENGHT OF ALL LINKS = ',len(all_link))
    # ###all_link = all_link[170:]

    for i,x in enumerate(all_link[:]):
        print('\n url = ',x)
        data = {
                'HOME TEAM': [],
                'AWAY TEAM': [],

                'HOME WIN':[],
                #'DRAW':[],
                'AWAY WIN':[],

                #'UNDER 2.5':[],
                'OVER 2.5':[],
                'BTS':[],
                'OTS':[],
                'NAME':[]
                }

        index_pos = i
        print(f'>>>>>>>>>>>>>>>>>>>>  NUMBER = {index_pos} HAS STARTED TO RUN, WITH TOTAL RUNS OF {len(all_link)}  & REMANING OF {len(all_link) - (index_pos+1)} <<<<<<<<<<<<<<<<<<<< \n')
       
        try:
            res = requests.get(x)
            soup = BeautifulSoup(res.content,"html.parser")
            
            teams = soup.find('h1',class_ = 'teamnamesh1').text.strip().split('vs')
            home_team = teams[0]
            away_team = teams[-1]
            
            preds = [x.text.strip().replace('%','').split() for x in soup.find_all('div',class_ = 'percdiv')]
            hw = int(preds[0][0])
            draw = int(preds[0][1])
            aw = int(preds[0][2])

            under = int(preds[1][1])
            over = int(preds[1][0])

            bts = int(preds[2][0])
            ots = int(preds[2][1])

            print(home_team,away_team,hw,draw,aw,under,over,bts,ots)
            

            data['HOME TEAM'].append(home_team)
            data['AWAY TEAM'].append(away_team)

            data['HOME WIN'].append(hw)
            #data['DRAW'].append(draw)
            data['AWAY WIN'].append(aw)
            
            #data['UNDER 2.5'].append(under)
            data['OVER 2.5'].append(over)

            data['BTS'].append(bts)
            data['OTS'].append(ots)
            data['NAME'].append('FST')

            saving_files(path=path,data=data)

        except:
            print('\n \n SORRY AN ERROR OCCURED \n')
            pass

    drop_duplicate(path=path)
    sorting_values(path=path,value='OVER 2.5',ascending_mode=False)

footballsupertips_func()