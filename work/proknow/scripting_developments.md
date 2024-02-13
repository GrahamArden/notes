
## Developments to ProKnow scripting

This is just a place to keep ideas for development of Python/c# scripting for Proknow 

### Integrating ARIA and ProKnow
   - There is a _lot_ of information available in ARIA which is not transmitted to ProKnow. One example is the Prescription which, in our case contains information about the dose, fractionation and, for some sites, laterality.
   - This is accesible using [ESAPI scripting](../../esapi/README.md)

Possible steps:

1. Query Proknow and return a list of patient _plans_ which have been added since the last time the program was run.
2.  For each plan returned in step 1, query ARIA via an ESAPI scriptto find the prescription which the plan is attached to
3.  Using the returned prescription, allocate each _plan_ to an appropriate national collection based on the dose, fractionation and laterality (if appropriate).
