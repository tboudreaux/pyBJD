# pyBJD
convert JD to BJD in a relatively convoluted manner using a very helpful website from Ohio State

# Examples
- Single JD
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
  
  
- List of JD
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
