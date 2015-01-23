Reaktor Summer Job demonstration
================================

This is a public code demonstration exercise for a simple URL shortening service. Done in python for study purposes.
The HTTP POST /shorten returns the shortened version of a URL, and HTTP GET /[short_version} redirects to the original
URL if found in the database.

To run, first run initialize.py and then test_urls.py. Running requires
    
    pip install requests
    pip install bottle
    pip install bottle_sqlite
 
The exercise details taken from [Reaktor](http://reaktor.fi/careers/summerjob/): 

    Create a URL shortening service. You are free to choose any programming language. Persistent storage is not required 
    for this exercise (i.e. in-memory database is fine). Your service must provide the following API (all POST requests use
    Content-Type: application/x-www-form-urlencoded unless otherwise mentioned):
    
    POST /shorten
    Parameters: Parameter link should contain the link to shorten.
    Returns: Id for the shortened link in text/plain format.
    
    GET /{id}
    Returns: 301 redirects the user agent to a previously stored URL. 404 error if no link stored with given id.