# -*- coding: utf-8 -*-

import sys as sys
import pandas as pd
import numpy as np


def method_preparedataframe():
    try:

        global df_movies
        global df_tvshows

        # df_ebr = pd.read_csv('ebrsheet.csv',encoding='utf-8',engine='python')
        df_movies = pd.read_csv('Assets/movies.csv')
        df_tvshows = pd.read_csv("Assets/tvshows.csv")

        df_tvshows['No_of_Episodes'] = df_tvshows['No_of_Episodes'].replace('unknown', np.nan)

    except Exception as exception:
        print('Error: ', exception, sys.exc_info()[-1].tb_lineno)


def method_pandas_commonfunctions():
    global df_tvshows
    try:
        print('\n## PANDAS COMMON FUNCTIONS ##')

        print('## Drop rows based on condition ##')
        df_tvshows = df_tvshows[df_tvshows.No_of_Episodes != 'No_of_Episodes']
        print('## Set Column Data Type')
        df_tvshows.No_of_Episodes = df_tvshows.No_of_Episodes.astype('float')

        print('## FUNCTION: head - top rows ##')
        print(df_tvshows.head(3))
        print('## FUNCTION: tail - last rows ##')
        print(df_tvshows.tail(3))
        print('## FUNCTION: shape ##')
        print(df_tvshows.shape)
        print('## FUNCTION: size ##')
        print(df_tvshows.size)
        print('## FUNCTION: info ##')
        print(df_tvshows.info)
        print('## FUNCTION: isna - null values##')
        print(df_tvshows.isna().sum())
        print('## FUNCTION: describe ##')
        df_describe = df_tvshows.describe()
        print(df_tvshows.describe())
        print('## FUNCTION: columns ##')
        print(df_tvshows.columns)
        print('## FUNCTION: nunique - count of unique##')
        df_describe = df_tvshows.nunique()
        print(df_tvshows.nunique())
        print('## FUNCTION: value_counts - count of values ##')
        print(df_tvshows['No_of_Seasons'].value_counts())
        print('## FUNCTION: add column##')
        df_tvshows['Genre_dup'] = df_tvshows['Genre']
        df_tvshows['Premiere_dup'] = df_tvshows['Premiere']
        print('## FUNCTION: drop - delete ##')
        df_tvshows = df_tvshows.drop(columns=['Genre_dup', 'Premiere_dup'])
        print('## FUNCTION: len ##')
        print(len(df_tvshows))
        print('## FUNCTION: query - filter data ##')
        df_describe = df_tvshows.query('No_of_Episodes == 20')
        print('## FUNCTION: iloc - index location ##')
        print(df_tvshows.iloc[10:100, 1:10])
        print('## FUNCTION: loc - column name location##')
        print(df_tvshows.loc[[10, 21, 30, 14], ['Title', 'Genre', 'Premiere']])
        print('## FUNCTION: dtypes ##')
        print(df_tvshows['No_of_Episodes'].dtypes)
        print('## FUNCTION: select_dtypes ##')
        print(df_tvshows.select_dtypes(include='int64'))
        print('## FUNCTION: insert column ##')
        ramdom_col = np.random.randint(100, size=len(df_tvshows))
        df_tvshows.insert(3, 'random_col', ramdom_col)
        print(df_tvshows.iloc[0:10, 0:4])
        print('## FUNCTION: sample - take random sample ##')
        df_describe = df_tvshows.sample(n=100)  # based on count
        df_describe = df_tvshows.sample(frac=0.15)  # based on percentage
        print('## FUNCTION: where - query all rows matching condition others with else value ##')
        df_tvshows['Genre'] = df_tvshows['Genre'].where(df_tvshows['No_of_Episodes'] > 50, df_tvshows['Genre'])
        print('## FUNCTION: rank - rank column based on another column ##')
        df_tvshows['Login ID'] = df_tvshows['No_of_Episodes'].rank()
        print('## FUNCTION: isin - get data exist in a datastructure ##')
        lst_genre = ['Crime Drama', 'Fantasy']
        df_describe = df_tvshows[df_tvshows['Genre'].isin(lst_genre)]
        print('## FUNCTION: replace - replace values ##')
        df_tvshows['Genre'] = df_tvshows['Genre'].replace('Teen Drama Fantasy', 'Teen Drama')
        print('## FUNCTION: rename - rename column ##')
        df_tvshows = df_tvshows.rename(columns={'No_of_Episodes': 'No_of_Episodes'})
        print('## FUNCTION: fillna - fill na with alternate text ##')
        df_tvshows['No_of_Episodes'].fillna(1000, inplace=True)
        print('## FUNCTION: groupby - group by values ##')
        print(df_tvshows.groupby('Genre')['No_of_Episodes'].sum())
        print('## FUNCTION: pct_change - percentage difference between previous and current ##')
        print(df_tvshows['No_of_Episodes'].pct_change())
        print('## FUNCTION: count - count data in col/row ##')
        print(df_tvshows.count(0))  # 0 for col 1 for row
        print('## FUNCTION: crosstab - pd.crosstab count of combination ##')
        print(pd.crosstab(df_tvshows['Genre'], df_tvshows['No_of_Seasons']))
        print('## FUNCTION: pd.qcut - segment the portions ##')
        print(pd.qcut(df_tvshows['random_col'], q=12).value_counts().sort_index())
        print('## FUNCTION: nlargest & nsmallest - get n number of largest and smallest ##')
        print(df_tvshows.nlargest(5, 'No_of_Episodes'))
        print(df_tvshows.nsmallest(5, 'No_of_Episodes'))

    except Exception as exception:
        print('Error: ', exception, sys.exc_info()[-1].tb_lineno)


method_preparedataframe()
method_pandas_commonfunctions()
