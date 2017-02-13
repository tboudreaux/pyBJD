# pyBJD
convert JD to BJD in a relatively convoluted manner using a very helpful website from Ohio State

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
To use firefox pass ```python FF = True ``` into the GetBJD function call
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
