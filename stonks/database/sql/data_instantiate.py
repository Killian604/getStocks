"""
Basic data which should be instantiated on DB-creation should reside here.
For table specs, it should be written in another file (not here!).
"""


sql_insert_finnhub_to_source = """INSERT INTO source (name) VALUES ('Finnhub');""".strip()

