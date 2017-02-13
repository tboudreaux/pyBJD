from selenium import webdriver                                                                                                      
from selenium.webdriver.common.keys import Keys 
from numpy import array, ndarray

def GetBJD(iJD=0, iRA=0, iDEC=0, iLAT=0, iLON=0, iALT=0):
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
    URL = 'http://astroutils.astronomy.ohio-state.edu/time/utc2bjd.html'
    
    if not isinstance(iJD, (list, ndarray)):
        iJD = [iJD]    # make all JDs into list
        
    JD_send = ''
    for i,e in enumerate(iJD):
        if i != len(iJD):
            JD_send += "{}\n".format(e)    #format JDs for webserver
        else:
            JD_send += "{}".format(e)

    #interact with webserver        
    driver = webdriver.PhantomJS()   # phantomJS required
    driver.get(URL)
    ra = driver.find_element_by_name('ra')
    ra.send_keys(iRA)
    dec = driver.find_element_by_name('dec')
    dec.send_keys(iDEC)
    jd = driver.find_element_by_name('jds')
    jd.send_keys(JD_send)
    lat = driver.find_element_by_name('lat')
    lat.send_keys(iLAT)
    lon = driver.find_element_by_name('lon')
    lon.send_keys(iLON)
    alt = driver.find_element_by_name('elevation')
    alt.send_keys(iALT)
    submit = driver.find_element_by_name('submit').click()
    source = driver.page_source.split('\n')
    driver.close
    
    # check for JD conversion fail
    try:
        assert '<pre>The 0th date' not in source[5]
    except AssertionError as e:
        e.args += ('BAD JD', 'Error in input - check JDs for validity (are they all capable of being cast to floats?)', 
                   'JDs inputed: ', iJD, 'JDs sent', JD_send)
        raise
    
    #Bracket the BJDs (based on the knonw formating of the output HTML)
    index_val = source.index('<pre>The following are the BJD_TDBs for each of your input dates:')
    close_val = source.index('</pre></body></html>')
    BJDs = source[index_val+2:close_val-3]  # retrive BJDs based on braket
    BJDs = [float(x) for x in BJDs]         # cast BJDs to float
    
    return BJDs
