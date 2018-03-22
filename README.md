# pyBJD
## Note that pyBJD is no longer activly supported, as astroSynth now has built in BJD conversion supported
convert JD to BJD in a relatively convoluted manner using a very helpful website from Ohio State

# Installation
```sh
$ git clone https://github.com/tboudreaux/pyBJD.git
$ cd pyBJD
$ python setup.py install
```



# Docstring
    """
    Gets BJD from returned result at:
    
        http://astroutils.astronomy.ohio-state.edu/time/utc2bjd.html
        
    Ohio State University IDL based UTC to BJD code
    
    Sateless function
    
    Params:
        iJD - list or single UTC JD value [string]
        iRA - hh:mm:ss Right Ascension for target [string]
        iDEC - dd:mm:ss Declination for target [string]
        iLAT - decimal degrees of latitude for observation location [string]
        iLON - decimal degrees of longitude for observation location [string]
        iALT - elevation of obvsevation from sea level in meters [string]
        
    Returns:
        BJDs - list of returnes BJDs as floats of length n = length iJD
        
    Exeptions:
        BAD_JD - JD formated incorrectly, will raise an assertation error showing JDs
                    all JDs should be castable to a float            
    Prerequisits:
        Selinium - Webserver interaction
        PhantomJS - invisible webdriver
        numpy - array handeling
    """
# Examples

- Single JD
```python
from pyBJD import GetBJD
if __name__ == '__main__':
	kwargs = {
    	"iJD": "2457796.500000",
    	"iRA": "12:00:00.0",
    	"iDEC": "60:00:00.0",
    	"iLAT": "-30.1716", 
    	"iLON": "-70.8009", 
    	"iALT": "2172"
   	}
	BJDs = getBJD(**kwargs)
```
- List of JD
```python
from pyBJD import GetBJD
if __name__ == '__main__':
	kwargs = {
    	"iJD": ["2457796.500000", "2457797.500000", "2457798.500000", "2457799.500000"],
    	"iRA": "12:00:00.0",
    	"iDEC": "60:00:00.0",
    	"iLAT": "-30.1716", 
    	"iLON": "-70.8009", 
    	"iALT": "2172"
   	}
	BJDs = getBJD(**kwargs)
```
# Requirements
1. numpy
2. selinium (pip install selinium)
..1. phantomJS (or Firefox) 
..2. Installation Instructions for PhantomJS (http://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python)

# Instructions for using Firefox
To use firefox pass ```FF = True ``` into the GetBJD function call
as an example see below
```python
from pyBJD import GetBJD
if __name__ == '__main__':
	kwargs = {
    	"iJD": ["2457796.500000", "2457797.500000", "2457798.500000", "2457799.500000"],
    	"iRA": "12:00:00.0",
    	"iDEC": "60:00:00.0",
    	"iLAT": "-30.1716", 
    	"iLON": "-70.8009", 
    	"iALT": "2172",
		"FF" = True
   	}
	BJDs = getBJD(**kwargs)
```
