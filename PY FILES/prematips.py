from func import requests_init,saving_files,drop_duplicate,match_day_date,main_date,save_daily_csv,sorting_values
from bs4 import BeautifulSoup
import requests



#x='https://primatips.com/tip/central-coast-mariners-yokohama-f-marinos-afc-champions-league-849775'
#res = requests.get(x)
#soup = BeautifulSoup(res.content,"html.parser")
##_,tree = requests_init(url=x)

def prematips_func():
    full_path = save_daily_csv()
    path = f'{full_path}/prematips.csv'
    if match_day_date == 1:
        url = 'https://primatips.com/tips/'+str(main_date(1))
    else:
        url = 'https://primatips.com/tips/'+str(main_date(0))

    soup,_ = requests_init(url)

    #   GETTING LINK SECTION
    links = [name.get('href') for name in soup.findAll('a')]
    all_link = []
    for link in links:
        try:
            if link.startswith('/tip/') and link not in all_link:
                all_link.append('https://primatips.com'+link)
        except:
            pass
    # USING LINKS TO GET ELEMENT IN THAT TEAMS
    print('LENGHT OF ALL LINKS = ',len(all_link))
    # # all_link = all_link[170:]

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

            # date_time = soup.find('div',class_ = 'game-time').text.strip().split()
            home_team = soup.find('div',class_ = 'team-flag-left').text.strip()
            away_team = soup.find('div',class_ = 'team-flag-right').text.strip()
            preds = [x.text.strip().split() for x in soup.find_all('div',class_ = 'games-stat-wrapper')]
            all_preds = []
            for x in preds:
                for y in x:
                    if '%' in y:
                        all_preds.append(y)
            # print(all_preds)

            hw = int(all_preds[-13].replace('%',''))
            draw = int(all_preds[-12].replace('%',''))
            aw = int(all_preds[-11].replace('%',''))

            under = int(all_preds[-5].replace('%',''))
            over = int(all_preds[-6].replace('%',''))

            bts = int(all_preds[-2].replace('%',''))
            ots = int(all_preds[-1].replace('%',''))

            print(home_team,away_team,hw,draw,aw,under,over,bts,ots)
            
            # data['DATE'].append(date_time[1][:-5])
            # data['TIME'].append(date_time[1][-5:])

            data['HOME TEAM'].append(home_team)
            data['AWAY TEAM'].append(away_team)

            data['HOME WIN'].append(hw)
            # data['DRAW'].append(draw)
            data['AWAY WIN'].append(aw)
            
            #data['UNDER 2.5'].append(under)
            data['OVER 2.5'].append(over)

            data['BTS'].append(bts)
            data['OTS'].append(ots)
            data['NAME'].append('PRE')

            saving_files(path=path,data=data)

        except:
            print('\n \n SORRY AN ERROR OCCURED \n')
            pass
    drop_duplicate(path=path)
    # sorting_values(path=path,value='OVER 2.5',ascending_mode=False)

prematips_func()
