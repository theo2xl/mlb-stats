# Status
The code currently works on a sqlite in memory db.

* Please `pip install` the necessary requirements from [requirements.txt](requirements.txt)
* Run `python etl.py` you will create, seed and load the in-memory db.
* A file named `'source_'+self.created_at.strftime("%m-%d-%y_%H:%M:%S")+'.html'` will be created to keep a history of what information was used for the import.
* You will also receive an output of the top 50 mlb avg leaders ranked by their their 2014 [wOBA](http://www.fangraphs.com/library/offense/woba/)

## TODO
* Version control db and information. Run migrations to easily revert improper loads.
* Error Handling
* Tests
* Proper class mapping, currently foreign keys exist, but I would like to be able to do things like see a player's last name directly from a call to the stats table.

# Initial Problem is below

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
