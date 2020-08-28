"""

"""


def get_sql_select_symbol_candlesticks(symbol: str):
    """"""
    sql = f"""
SELECT
    *
FROM candlestick AS cs
JOIN symbol AS s ON s.id = cs.symbol_id
WHERE s.symbol='{symbol}'
"""

    return sql


def get_sql_select_sourceid_from_source(source: str) -> str:
    """"""
    sql = f"""
SELECT
    id
FROM source
WHERE name='{source}'""".strip()
    return sql


if __name__ == '__main__':
    print(get_sql_select_symbol_candlesticks('AAPL'))
    pass
