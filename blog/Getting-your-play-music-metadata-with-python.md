title: Getting your play music metadata with python
published: 2017-01-04
category: python

### Background ###
Play Music is an online streaming service that allows the user to upload his/her songs for listening through the Play Music platform. It also provides a large library of songs available for streaming at a monthly fee.

Unfortunately, Google doesn't provide an API for Play Music. This means that, if you would like to collect your library's metadata, you would need to use an unofficial  API. [gmusicapi](http://unofficial-google-music-api.readthedocs.io/en/latest/index.html "gmusicapi") is the API that I chose, it has all the functionality that I need, and its documentation is quite nice.

### What you need to start ###
gmusicapi doesn't officially support versions of Python below 2.7.9 , and support for Python 3 is experimental. So, If you go with **Python 2.7.9** or a higher version of Python 2.7 you shouldn't get any problems.

Make sure you also have pip, if you don't have it follow the instructions on this **[page](https://packaging.python.org/installing/#install-pip-setuptools-and-wheel "install pip")** to get it. Once you have Python and pip installed run the following line of code to install gmusicapi and all of its dependencies.

    :::bash
    pip install gmusicapi

### How to do it ###
First lets import the Mobile client from the gmusicapi package, initialise the Mobileclient, and log-in.

    :::python
    from gmusicapi import Mobileclient
    api = Mobileclient()
    logged_in = api.login('your_username@gmail.com', 'your_password',
                          Mobileclient.FROM_MAC_ADDRESS)

Now `logged_in` will be True if you logged in successfully and False otherwise. If you are having trouble logging in it is probably because you have two-factor authentication enabled. **If you have two-factor authentication enabled for your Google account generate and use an app password for this script.**

    :::python
    library = api.get_all_songs()

Once logged in the authenticated `MobileClient()` instance pointed to by the variable `api` will be able to perform operations on your Google Play Music data. In the above snippet the call to member function `get_all_songs()` should return a list of dictionary objects, with each dictionary containing each song's metadata. 

    :::python
    logged_out = api.logout()

It's probably a good idea to log out before saving the data we've retrieved. I chose to save the data as a Json file. This can be easily done using Python's built in `json` module. Also, since I'm running this script periodically I wanted to give the file a unique name that tells me when the data was collected, so I used Python's built in `time` module to set the file-name as milliseconds since the epoch. Lets import `json` and `time` into our script. The top of your script should look something like this:

    :::python
    from gmusicapi import Mobileclient
    import json
    import time

Now lets build the file name. To get the time since the epoch in seconds call `time.time()`.

    :::python
    milliseconds = int(time.time() * 1000)
    file_name = str(milliseconds) + ".json"

Lets convert the list of dictionaries to a Json object and save it to a file.

    :::python
    library_json = json.dumps(library, ensure_ascii=True, 
                              indent=4, sort_keys=True)
    with open(file_name, "w") as json_file:
        json_file.write(library_json)

We're done, you should now have a file in your script directory that contains all of your songs' metadata. Below you'll find the script that I used, the core functionality is the same, but the script below is more descriptive when run from the command line. It also terminates if log-in wasn't successful.

    :::python
    from gmusicapi import Mobileclient
    import json
    import time
    
    def get_library(api):
        library = api.get_all_songs()
        milliseconds = int(time.time() * 1000)
        file_name = str(milliseconds) + ".json"
    
        library_json = json.dumps(library, ensure_ascii=True, 
                                  indent=4, sort_keys=True)
        with open(file_name, "w") as json_file:
            json_file.write(library_json)
            print "library saved to %s successfully" % file_name
    
        logged_out = api.logout()
        if logged_out:
            print "logged out successfully"
        else:
            print "log out unsuccessful, cache not cleaned"
    
	if __name__ == '__main__':
		api = Mobileclient()

		logged_in = api.login('your_username@gmail.com', 'your_password',
							  Mobileclient.FROM_MAC_ADDRESS)
		if logged_in:
			print "logged in successfully"
			get_library(api)
		else:
			print "invalid log in credentials"