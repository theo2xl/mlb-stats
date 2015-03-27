# Summary
This solution works best when using [Docker](https://www.docker.com/)

There are two components:
* Python3 app that scrapes a given tabular html url which contains 2014 batting leaders.
  * Uses sqlalchemy ORM to access player, team, position and yearly stats.
  * Uses alembic to track database migrations
  * Uses beautifulsoup to parse the html
  * Uses urllib to download the file.
   * **Python2 issue**: urllib is the only package which restricts backwards compatibility to Python2. If you need to run with Python2, please modify the [model.py](model.py) file.
     * Import `urllib` instead of `urllib.request`.
     * Change the ```urllib.request.urlretrieve(self.url, self.filename)``` call in the `download` method to ```urllib.urlretrieve(self.url, self.filename)```)
* Postgres DB to contain player, team, position and yearly stats

## Docker Instructions
1. `docker-compose build` : Build docker container for pythong app
2. `docker-compose run web` : Run migrations to setup db
3. `docker-compose run web python etl.py` : Run script to generate top 50 wOBA

## Non-Docker instructions
* Please `pip install` the necessary requirements from [requirements.txt](requirements.txt)
* Setup a postgres db.
 * change etl.py and alembic.ini to match new db information
* Run `alembic upgrade head` to migrate and seed db
* Run `python etl.py` to load information from the 2014 leaders HTML
* A file named `'source_'+self.created_at.strftime("%m-%d-%y_%H:%M:%S")+'.html'` will be created to keep a history of what information was used for the import.
* You will also receive an output of the top 50 mlb avg leaders ranked by their their 2014 [wOBA](http://www.fangraphs.com/library/offense/woba/)

## Error Handling
Currently there is no error handling as we have clean data and a fresh db.
Some initial thoughts about issues that could arise:
* Players with same first initial and last name
* Missing fields (do you do a partial import)
* Matching existing players to new data
* Players that played partial seasons with different teams
* General corrupt data (strings instead of ints, malformed html)

## TODO
Currently duplicate players and stats would be created if the script is run more than once.

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
