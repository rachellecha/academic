import pandas as pd
import csv

gpa = pd.read_csv("GPA for Study Hours Spring 22 (Responses) - Sheet2.csv")

gpa = gpa.set_index('Name').T.to_dict('list')

hours = pd.read_csv("week9.csv")

hours = hours.groupby(['Name'], as_index = False).sum()

points = {}

#insert names (comma separated and in quotes) exactly how it's spelled on the google forms
#example extrahours = ["Rachelle Cha", "Alyssa Santos", "Camille Romano", "Diana Nguyen"]
extrahours = []


for index, row in hours.iterrows():
    name = row["Name"]
    hour = row["Hours"]
    gpa1 = float(gpa[name][0])


    if name not in extrahours:
        if gpa1 >= 3.5:
            if hour - 1 > 0:
                point = hour - 1
                points[name] = (point*10) + 10
            elif hour - 1 == 0:
                points[name] = 0
            else:
                points[name] = -10

        if gpa1 >= 3.25 and gpa1 < 3.5:
            if hour - 2 > 0:
                point = hour - 2
                points[name] = (point*10) + 10
            elif hour - 2 == 0:
                points[name] = 0
            else:
                deduct = hour - 2
                points[name] = 10*deduct

        if gpa1 >= 3.00 and gpa1 < 3.25:
            if hour - 3 > 0:
                point = hour - 3
                points[name] = (point*10) + 10
            elif hour - 3 == 0:
                points[name] = 0
            else:
                deduct = hour - 3
                points[name] = 10*deduct
        
        if gpa1 >= 3.00 and gpa1 < 3.25:
            if hour - 3 > 0:
                point = hour - 3
                points[name] = (point*10) + 10
            elif hour - 3 == 0:
                points[name] = 0
            else:
                deduct = hour - 3
                points[name] = 10*deduct

        if gpa1 >= 2.75 and gpa1 < 3.00:
            if hour - 4 > 0:
                point = hour - 4
                points[name] = (point*10) + 10
            elif hour - 4 == 0:
                points[name] = 0
            else:
                deduct = hour - 4
                points[name] = 10*deduct

        if gpa1 < 2.75:
            if hour - 5 > 0:
                point = hour - 5
                points[name] = (point*10) + 10
            elif hour - 5 == 0:
                points[name] = 0
            else:
                deduct = hour - 5
                points[name] = 10*deduct 
    else:
        if hour - 10 > 0:
            point = hour - 10
            points[name] = (point*10)
        elif hour - 10 == 0:
            points[name] = 0
        else:
            deduct = hour - 10
            points[name] = 10*deduct

    
#print(points)

with open('points9.csv', 'w') as f:
    for key in points.keys():
        f.write("%s, %s\n" % (key, points[key]))

#GPA's:
#- 3.5 and above: 1 hr/week
#- 3.25 to <3.5: 2 hr/week
#- 3.0 to <3.25: 3 hr/week
#- 2.75 to <3.0: 4 hr/ week
#- Under 2.75: 5 hr/week

#print(gpa)



