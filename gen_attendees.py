#!/usr/bin/env python3

import pandas as pd
import tabulate

columns = ['Name', 'Organizational Affiliation']
df = pd.read_csv('/Users/msn/Downloads/data.csv', usecols=columns)

tfile = open('./content/about/attendees.md', 'w')
tfile.write("---\n")
tfile.write("draft: false\n")
tfile.write("title: \"Registered Attendees ("+str(df.Name.count())+")\"\n")
tfile.write("weight: 90\n")
tfile.write("---\n\n")

tfile.write(df.to_markdown(index=False))
tfile.close()

#========= IN PERSON AND NEEDS HOTEL 

df = pd.read_csv('/Users/msn/Downloads/data.csv')
df = df.rename(columns=df.iloc[0]).drop(df.index[0])

df = df.loc[df.iloc[:,31] == 'Yes']

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df.iloc[:, [1,2,3,31]].to_string(index=False))