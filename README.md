# Manga Cork
Manga Cork is an annotation website for mangas. Users can pin a comment on a 
strip of manga for others to see, a bit like posting a note on a notice or 
pin board. 

### Steps:
Get basic website with users and pictures up 
* Get a website for manga cork
	X  Get a domain 
	X  Set it up with nginx
	* Create a website using jinja and flask
* Host picture files
	* Upload pictures onto nginx image folder
	* Link to them with flask
* Move between pictures
	* Enable caching to avoid downloading the same picture over and over

Enable comments
* Add field for signing up, logging and out
* Add forgot password
* Setup a database 
	* Save user and password 
	* Save comments

* Allow users to comment on a particular page
* Find API which tags/pins pictures 
* Connect pins with comment

Enable upvotes
* Setup database query to handle upvotes

![Mock_screens](/images/mock_screens.jpg)
