"""

"""


# varchar_short = 'VARCHAR(200)'


def sql_create_table_symbol(table_name='symbol') -> str:
    """"""
    sql = f"""
CREATE TABLE "{table_name}" (
    "id"	INTEGER NOT NULL UNIQUE,
    "symbol"	TEXT NOT NULL UNIQUE,
    "name"	TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT)
)""".strip()

    return sql


def sql_create_table_candlestick(table_name='candlestick') -> str:
    """"""
    sql = f"""
CREATE TABLE "{table_name}" (
    "id"	INTEGER NOT NULL UNIQUE,
    "symbol_id"	INTEGER NOT NULL,
    "high"	NUMERIC NOT NULL,
    "open"	NUMERIC NOT NULL,
    "close"	NUMERIC NOT NULL,
    "low"	NUMERIC NOT NULL,
    PRIMARY KEY("symbol_id"),
    FOREIGN KEY("symbol_id") REFERENCES "symbol"("id")
)""".strip()

    return sql


if __name__ == '__main__':
    print(sql_create_table_symbol())
    print(sql_create_table_candlestick())
    pass



"""
CREATE TABLE "candlestick" (
	"id"	INTEGER UNIQUE,
	"symbol_id"	INTEGER NOT NULL,
	"high"	NUMERIC NOT NULL,
	"open"	NUMERIC NOT NULL,
	"close"	NUMERIC NOT NULL,
	"low"	NUMERIC NOT NULL,
	FOREIGN KEY("symbol_id") REFERENCES "symbol"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)"""