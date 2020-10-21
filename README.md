# Investment App

This programme scraps data from the internet and analyses to suggest which shares to purchase. To run the programme:
```
python run.py
```
The data will be saved in a database with each company's data saved to it's own table.

Once the programme has run, the data will be analysed and a csv file will be produced with a list of potential companies to invest in based on certain metrics. If you do no want to run the analysis, run the programme with the "noanalysis" argument:
```
python run.py --noanalysis
```
Or, alternatively:
```
python run.py -na
```

There are a number of command line arguments the user can use. To view all these:
```
python run.py -h
```

It is possible to see the analysis of stocks for the current day by running:
```
python checkout_analysis.py
```
This script takes two arguments:
--path for declaring the path in which the file csv you want to look at is saved
--file for declaring the name of the csv file you want to look at