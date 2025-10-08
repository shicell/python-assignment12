""" Task 2: A Line Plot with Pandas """

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 2.1 connect to db/lessons
with sqlite3.connect("../db/lesson.db") as conn:

    # 2.1 SQL statement to retrieve data from database and read into a dataframe
    sql_statement = """
                        SELECT 
                            o.order_id
                            , SUM(p.price * l.quantity) AS total_price 
                        FROM
                            orders o
                            
                            JOIN line_items l
                            ON o.order_id = l.order_id
                            
                            JOIN products p 
                            ON l.product_id = p.product_id 
                        GROUP BY o.order_id;
                    """
    # 2.1 read database into dataframe
    df = pd.read_sql_query(sql_statement, conn)

    # 2.2 add a cumulative column to dataframe
    df = df.sort_values(by="order_id")
    df['cumulative'] = df['total_price'].cumsum()
    print(df.head(5))

    # 2.3 create a line plot of cumulative rev vs order id
    df.plot(x="order_id", y="cumulative", label="Cumulative Revenue", kind="line"
            , title="Cumulative Revenue vs Order ID")
    plt.xlabel("Order ID")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()

    # 2.4 show plot
    plt.show()
