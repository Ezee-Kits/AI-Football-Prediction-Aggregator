from func import main_date
import pandas as pd
import os


csv_files_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),f'CSV FILES/{str(main_date())} Files')

path_files = os.listdir(csv_files_path)
while True:
    #user = int(input('\n \t OPEN ROW 0 TO :'))
    sort_list = ['HOME WIN', 'AWAY WIN', 'OVER 2.5', 'BTS', 'OTS']
    sort_list2 = ['HOME WIN [1]', 'AWAY WIN [2]', 'OVER 2.5 [3] ', 'BTS[4]', 'OTS [5]']
    print('\n',sort_list2)
    #print(sort_list2)
    value = int(input('\n \t SORT BY :'))
    print(f'\t \t SORTED BY USING :[[[[[ {sort_list[value-1]} ]]]]')
    app_df = pd.DataFrame()
    for all_files in path_files:
        df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)),f'CSV FILES/{str(main_date())} Files/{all_files}'))
        df = df.sort_values(by=df.columns[1+value],ascending=False)
        sel_row = df.iloc[:3,:]
        app_df = pd.concat([app_df,sel_row],ignore_index=True)

    print(app_df.sort_values(by=['HOME TEAM'], ascending=True)[['HOME TEAM', 'AWAY TEAM',sort_list[value-1],'NAME']].to_string())
    df = app_df
    while True:
        search_match = input('\n  >>>>>>>>> Search [[ HOME OR AWAY TEAM ]] Name Here >>>>>>>> :')
        if search_match == '':
            break
        else:
            filtered_df = df[(df['HOME TEAM'].str.contains(search_match,case=False) | (df['AWAY TEAM'].str.contains(search_match,case=False)) )]
            print(filtered_df.sort_values(by=['HOME TEAM'], ascending=True)[['HOME TEAM', 'AWAY TEAM',sort_list[value-1],'NAME']].to_string())

