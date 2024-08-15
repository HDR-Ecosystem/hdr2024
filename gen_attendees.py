#!/usr/bin/env python3

import pandas as pd
import tabulate

columns = ['Name', 'Organizational Affiliation']
df = pd.read_csv('/Users/msn/Downloads/data.csv', usecols=columns)
print(df.to_markdown(index=False))
print(df.Name.count())

tfile = open('./content/about/attendees.md', 'w')
tfile.write("---\n")
tfile.write("draft: false\n")
tfile.write("title: \"Registered Attendees ("+str(df.Name.count())+")\"\n")
tfile.write("weight: 90\n")
tfile.write("---\n\n")

tfile.write(df.to_markdown(index=False))
tfile.close()
