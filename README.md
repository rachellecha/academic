# academic

## computer set up

first make sure you have python downloaded

https://www.python.org/downloads/

then make sure you have VSCODE[https://code.visualstudio.com/download] or your preferred IDE

then download `calculate.py` onto your computer

## form set up

for the GPA form, make sure to download the google sheets as a .csv
make sure the first column is called **Name** and the second column is called **GPA** this is case sensitive

for the hours form, make sure to download the google sheets as a .csv
make sure the first column is called **Name** and the second column is called **Hours** this is case sensitive

## using calculate.py

on this line `gpa = pd.read_csv("GPA for Study Hours Spring 22 (Responses) - Sheet2.csv")` 
change out *GPA for Study Hours Spring 22 (Responses) - Sheet2.csv* with the name of your csv file that holds the GPAs

on this line `hours = pd.read_csv("week9.csv")`
change out *week9* with the name of your csv file that holds the hours for the week

## extra hours

the president or vice president will tell you if anyone has to do extra hours. 
on this line `extrahours = []`
insert the names **in quotes** and **comma separated** 
this must be done **exactly as you see their name spelled in the google form**

## running it

in your command line/terminal, run `python calculate.py`

