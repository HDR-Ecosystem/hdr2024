#!/usr/bin/env python3

import pandas as pd
import tabulate

columns = ['Name', 'Organizational Affiliation']
df = pd.read_csv('/Users/msn/Downloads/data.csv', usecols=columns)

n_registered = df.Name.count()

tfile = open('./content/about/attendees.md', 'w')
tfile.write("---\n")
tfile.write("draft: false\n")
tfile.write("title: \"Registered Attendees ("+str(n_registered)+")\"\n")
tfile.write("weight: 90\n")
tfile.write("---\n\n")

tfile.write(df.to_markdown(index=False))
tfile.close()

df = pd.read_csv('/Users/msn/Downloads/data.csv')
df = df.rename(columns=df.iloc[0]).drop(df.index[0])

#========= REGISTERED and IN PERSON

df_in_person = df.loc[df.iloc[:,3] == 'In-person']  # in-person

#========= REGISTERED and NEEDS HOTEL 

df_needs_hotel = df.loc[df.iloc[:,31] == 'Yes']  # Needs hotel

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_needs_hotel.iloc[:, [1,2,3,31]].to_string(index=False))

#============== PRINT SUMMARY

n_in_person = df_in_person.iloc[:,1].count()
n_needs_hotel = df_needs_hotel.iloc[:,1].count()

print("\n")
print("Registered: "+str(n_registered))
print("  and in-person  : "+str(n_in_person))
print("  and needs hotel: "+str(n_needs_hotel))
print("\n")

