# mlb-stats
## JavaScript/UI/UX Coding Exercise

For this exercise you will be developing a mini web application for viewing the Cubs MLB
team roster.

Use the [roster.json](static/roster.json) file that describes the Cubs current roster to
drive your application.

### Required Features:
* The user must be able to save and view short text notes on any player.

### Upon completion you will deliver the following:
* JavaScript, HTML and other resources required to run your application.
* At least one screenshot of your application
* An explanation of the technologies used
* directions for starting your web app

### Notes
* Your application does not need to utilize an application server. Ideally it
will run simply by opening an HTML file in a web browser.
* Specify the browser you tested with. Either Chrome or Firefox is fine.
* For this simple exercise you should use HTML5 web storage to save the notes
on a player.

## Python/SQL Coding Exercise

For this exercise you will be writing Python code to parse HTML and insert it into a PostgreSQL database that you will create.

### Upon completion you will deliver the following
* Python code that does the following:
 * downloads the [Leaderboard HTML](static/leaderboard.html) found in this repository
 * parses all stats for players and inserts it into a database table or tables

* SQL statements to:
 * Create the table or tables that your Python code needs
 * A query that ranks these same players according to their 2014 [wOBA](http://www.fangraphs.com/library/offense/woba/)

### Notes

* Your Python code can assume the tables it uses have already been created. That is, it doesn't need to
automatically create the tables.
* Feel free to use any modules available via a ```pip install```. Include a ```requirements.txt``` file that
lists the dependencies.
