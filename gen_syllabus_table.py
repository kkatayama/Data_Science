# coding: utf-8
a = '''Week 1
1/6–2/12
DATA SCIENCE OVERVIEW
Data use in public policy, public administration, and decision making; Analysis
tools, data types, and data use cases; Basic statistics; (Multi-)Linear Regression;
Introduction to Python
Use case: Sea-level Rise
Week 2
1/13–1/19
THE OPEN DATA ECOSYSTEM AND REPRODUCIBILITY
Public/Private/Academic Sector data availability and access; URL handling,
munging, cleaning, missing data; version control with GitHub
Use case: Social Media and Public Sentiment
Week 3
1/20–1/26
DATA VISUALIZATION
Visualization types including plotting choice and visual representation of data;
Interactive and web-based graphics; Mapping and color schemes
Use case: Social Factors Affecting Energy Consumption and Use
Week 4
1/27–2/2
TIME SERIES ANALYSIS
Identifying and removing trends; Anomaly detection; Interpolation and
extrapolation; Correlation and structure functions; Introduction to R and Tableau
Use case: Ride-hailing Apps, Taxis, and Public Transportation
Week 5
2/3–2/9
SIMULATION AND (UN)CERTAINTY IN DECISION MAKING
Monte Carlo methods; Drawing from distributions; Independent and identically
distributed samples; Error bars and weighted regression
Use Case: Gerrymandering and redistricting
'''.splitlines()
print('| Week | Topic |')
print('| :-- | :-- |')

for i, l in enumerate(a):
    if 'Week' in l:
        first = '| ' + l + ' | '
        if i:
            print(second + '|')
    elif '/' in l and '–' in l:
        second = '| ' + l + ' | '
    elif l.isupper():
        first += l + ' |'
        print(first)
    else:
        if 'Use ' in l:
            second += '<br />' + l + ' '
        elif ';' in l and len(l) > 50:
            second += '; <br />'.join(l.rsplit(';', 1))
        else:
            second += l + ' '
print(second + '|')
