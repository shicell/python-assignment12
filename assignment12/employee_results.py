""" Task 1: Plotting with pandas """

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1.2 connect to db/lessons
with sqlite3.connect("../db/lesson.db") as conn:

    # 1.2 SQL statement to retrieve data from database and read into a dataframe
    sql_statement = """
                        SELECT 
                            last_name
                            , SUM(price * quantity) AS revenue 
                        FROM
                            employees e
                            
                            JOIN orders o
                            ON e.employee_id = o.employee_id 
                            
                            JOIN line_items l 
                            ON o.order_id = l.order_id 
                            
                            JOIN products p 
                            ON l.product_id = p.product_id 
                        GROUP BY e.employee_id;
                    """
    # 1.2 read database into dataframe
    employee_results = pd.read_sql_query(sql_statement, conn)

    # 1.3 - 1.4 create bar graph of last names vs revenue, giving appropiate titles
    # labels and colors
    employee_results.plot(x="last_name", y="revenue", label="Revenue", kind="bar", color="skyblue"
                          , title="Revenue by Employee")
    plt.xlabel("Last Name of Employee")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()

    # 1.5 show plot
    plt.show()
