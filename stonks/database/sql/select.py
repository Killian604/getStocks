"""

"""


def sql_select_symbol_candlesticks(symbol: str):
    """"""
    sql = f"""
SELECT
    *
FROM candlestick AS cs
JOIN symbol AS s ON s.id = cs.symbol_id
WHERE s.symbol='{symbol}'
"""

    return sql


if __name__ == '__main__':
    print(sql_select_symbol_candlesticks('AAPL'))
    pass
