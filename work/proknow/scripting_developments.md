
## Developments to ProKnow scripting

This is just a place to keep ideas for development of Python/[c# scripting](../../esapi/README.md) for Proknow 

### Rewriting the scrips to allocate patients to collections

The main problem with the original scripts was that they allocated _patients_ to collections ratherr that _dose_ objects. This means that the scorcards did not work.  These are currently being [rewritten](https://github.com/GrahamArden/Hull_tandf_scripts)

### Modifying the [modules](https://github.com/nhs-proknow/proknow-scripting-tandf/tree/main/modules) to use Pandas dataframes in addition to csv files.

The modules written by Liam use .csv files as a way of storing data. Using Pandas dataframes might be more useful in order to automate some of the processing

The first step would be to modify the method in the class "NHSProknow" (which is contained in the module "nhs_collctions.py). This must be done whilst maintaining backwards compatability for those that want to use csv files:
- modify "get_patients" (which currently extracts the patient data from a csv file or python list) to also extract data from a Pandas dataframe.
- there is a "write_csv" method which writes a list of dicts, It might be worth adding a "write_pd" to do the same to a Pandas dataframe
- check the other modules to ensure nothing breaks!

### Integrating ARIA and ProKnow
   - There is a _lot_ of information available in ARIA which is not transmitted to ProKnow. One example is the Prescription which, in our case contains information about the dose, fractionation and, for some sites, laterality.
   - This is accesible using [ESAPI scripting](../../esapi/README.md)
   - Another option, suggested by Aditi, would be to do an SQL query on ARIA. It is possible to embed an SQL query within a Pandas command:

``` python
import pandas as pd
import sqlite3  # You can use another database library if needed, like sqlalchemy

# Create a connection to your database
conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your actual database file

# Write your SQL query
sql_query = "SELECT * FROM your_table;"  # Replace 'your_table' with the name of your table

# Execute the query and create a DataFrame
df = pd.read_sql(sql_query, conn)

# Close the connection
conn.close()

# Now you have a Pandas DataFrame 'df' containing the result of your SQL query
```

Possible steps:

1. Query Proknow and return a list of patient _plans_ which have been added since the last time the program was run.
2.  For each plan returned in step 1, query ARIA via an ESAPI script or SQL query to find the prescription which the plan is attached to
3.  Using the returned prescription, allocate each _plan_ to an appropriate national collection based on the dose, fractionation and laterality (if appropriate).
