
from datetime import date, timedelta
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests
import time
import os


match_day_date = 0

def main_date(day = match_day_date):
    last_date = date.today() + timedelta(day)
    return last_date


def save_daily_csv():
    outcome_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'CSV FILES')
    todays_dir = str(main_date(match_day_date))+' Files'
    full_path = os.path.join(outcome_dir,todays_dir)
    try:
        os.makedirs(full_path)
    except:
        print('\n PATH ALREADY EXIST BUT WAS CREATED SUCCESFULLY \n')
    return full_path
    
    
def save_daily_csv2(main_dir,second_dir_path_name):
    outcome_dir = main_dir
    todays_dir = second_dir_path_name
    full_path = os.path.join(outcome_dir,todays_dir)
    try:
        os.makedirs(full_path)
    except:
        print('\n PATH ALREADY EXIST BUT WAS CREATED SUCCESFULLY \n')
    return full_path
    

def requests_init(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    tree = html.fromstring(res.content)
    return soup,tree


def tree_init(optional):
    tree = html.fromstring(optional)


def saving_files(data,path):
    df = pd.DataFrame(data)
    print(df.to_string())

    try:
        df2 = pd.read_csv(path)
        all_df = pd.concat([df2, df], ignore_index=True)
        all_df.to_csv(path, index=False)
        print(' ------------------------------------ ALL FILES SAVED  ------------------------------------- \n \n')

    except:
        df.to_csv(path, index=False)
        print('============================= SECOND FILE SAVED ==========================')



def drop_duplicate(path):
    all_df = pd.read_csv(path)
    all_df = all_df.drop_duplicates(keep='first')
    all_df = all_df.reset_index()
    all_df.drop(['index'], axis=1, inplace=True)
    all_df.to_csv(path, index=False)


def sorting_values(path,value,ascending_mode):
    df = pd.read_csv(path)
    df = df.sort_values(by=value,ascending=ascending_mode)
    df.to_csv(path, index=False)


def sorting_values_path_to_save(path,value,path_to_save,ascending_mode):
    df = pd.read_csv(path)
    df = df.sort_values(by=value,ascending=ascending_mode)
    df.to_csv(path_to_save, index=False)



def new_col_with2_vals(path,new_col_name,col_val1,col_val2,operator,new_col_index):
    df = pd.read_csv(path)
    new_data = []
    for i,x in enumerate(df[df.columns[0]]):
        if operator == '+':
            new_data.append( float(str(df[col_val1][i]).replace('-','')) + float(str(df[col_val2][i]).replace('-','')) )
        if operator == '-':
            new_data.append( float(str(df[col_val1][i]).replace('-','')) - float(str(df[col_val2][i]).replace('-',''))  )
        if operator == '*':
            new_data.append( float(str(df[col_val1][i]).replace('-','')) * float(str(df[col_val2][i]).replace('-',''))  )

    df[new_col_name] = new_data
    col = df.pop(new_col_name)
    df.insert(new_col_index,col.name,col)
    df.to_csv(path, index=False)


def new_col_with4_vals(path,new_col_name,col_val1,col_val2,col_val3,col_val4,operator,new_col_index):
    df = pd.read_csv(path)
    new_data = []
    for i,x in enumerate(df[df.columns[0]]):
        if operator == '+':
            new_data.append( (df[col_val1][i] + df[col_val2][i]) + (df[col_val3][i] + df[col_val4][i]) )
        if operator == '-':
            new_data.append( (df[col_val1][i] + df[col_val2][i]) - (df[col_val3][i] + df[col_val4][i]) )
        if operator == '*':
           new_data.append( (df[col_val1][i] + df[col_val2][i]) * (df[col_val3][i] + df[col_val4][i]) )

    df[new_col_name] = new_data
    col = df.pop(new_col_name)
    df.insert(new_col_index,col.name,col)
    df.to_csv(path, index=False)


def change_col_value(path,col,value,op_sign):
    df = pd.read_csv(path)
    for i,x in enumerate(df[df.columns[0]]):
        if op_sign == '==':
            if df[col][i] == value:
                df[col][i] = value

        if op_sign == '>':
            if df[col][i] > value:
                df[col][i] = value

        if op_sign == '<':
            if df[col][i] < value:
                df[col][i] = value

        if op_sign == '>=':
            if df[col][i] >= value:
                df[col][i] = value

        if op_sign == '<=':
            if df[col][i] <= value:
                df[col][i] = value
    df.to_csv(path, index=False)


def scrolling(driver):
    total_page_height = driver.execute_script("return document.body.scrollHeight")
    total_page_height = int(total_page_height) * 3
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')

    ap = []
    count = 0
    run = True
    while run:  # total_page_height - current_position > browser_window_height:
        time.sleep(1)
        driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position} );")
        current_position = driver.execute_script('return window.pageYOffset')
        print(current_position)

        ap.append(current_position)
        count += 1
        if count >= 2:
            if ap[-1] == ap[-2]:
                print('breaking ')
                run = False


def getting_tmr_match(data,match_date):
    url = 'https://www.statarea.com/predictions/date/' + str(match_date) + '/competition'

    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    def_match_date = str(match_date)
    for one_match_info in soup.find_all('div',class_ = 'match'):

        def_match_time = one_match_info.find('div',class_ = 'date').text.strip()
        def_host_team = one_match_info.find('div',class_ = 'hostteam').find('div',class_ = 'name').text.strip()
        def_guess_team = one_match_info.find('div',class_ = 'guestteam').find('div',class_ = 'name').text.strip()
        def_pred_list = []
        for all_pred_value in  one_match_info.find('div',class_ = 'inforow').find('div',class_ = 'coefrow').find_all('div',class_ = 'coefbox'):
            try:
                def_pred_list.append(all_pred_value.find('div',class_ = 'value').text.strip())
            except:
                pass
        print(def_pred_list)
        data['DATE'].append(def_match_date)
        data['TIME'].append(def_match_time)
        data['HOME TEAM'].append(def_host_team)
        data['AWAY TEAM'].append(def_guess_team)

        data['HOME WIN'].append(def_pred_list[6])
        data['DRAW'].append(def_pred_list[6])
        data['AWAY WIN'].append(def_pred_list[6])
        
        data['BTS'].append(def_pred_list[6])
        data['OTS'].append(def_pred_list[6])

        data['OVER 1.5'].append(def_pred_list[6])
        data['OVER 2.5'].append(def_pred_list[7])
        data['UNDER 2.5'].append(100 - int(def_pred_list[7]))
        data['OVER 3.5'].append(def_pred_list[8])
        data['NAME'].append('STATAREA')

