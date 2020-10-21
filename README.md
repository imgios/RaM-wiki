<img src="https://i.imgur.com/qXFzp8d.png" align="right">

# 📺 Rick and Morty Wiki
Rick and Morty Wiki is a Web Application project for academic purposes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python >=3.8
- pip
- venv
- Flask
- Neo4j

### Installing

1. Clone the repository
```bash
$ git clone https://github.com/imgios/RaM-wiki.git
$ cd RaM-wiki
```
2. Create a new virtualenv and activate it:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
3. Install dependencies:
```bash
$ pip3 install -r requirements.txt
```
4. Create a new Neo4j database and edit database username and password in `utilities.py`:
```python
def getConnection():
    dbUsername = 'neo4j' # replace neo4j with your database username
    dbPassword = 'ramwiki' # replace ramwiki with your database password
    ... 
```
5. Run the script `createdb.py` in order to populate the database:
```bash
$ python3 ramwiki/createdb.py
```
6. Run the application:
```bash
$ python3 run.py
```

## Built With

* [Python 3.8](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Bulma](https://bulma.io/)
* [Neo4j](https://neo4j.com/)

## Acknowledgments

Thanks to [rickandmortyapi.com](https://rickandmortyapi.com/), used for the dataset creation.
