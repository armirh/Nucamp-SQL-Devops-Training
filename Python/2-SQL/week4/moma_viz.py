""""Week 4 Workshop Assignment."""

# %% Setup Cell
from typing import Counter
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = psycopg2.connect("dbname=week4 user=postgres host=localhost port=5432")


def sql_to_df(sql_query: str):
    """Get result set of sql_query as a pandas DataFrame."""
    return pd.read_sql(sql_query, con)


# %% Task 1 Cell

def task1():
    """Perform Task 1."""

    title = "Artworks by Department"
    # TODO task 1
    query = '''
        SELECT department AS department, COUNT(id) AS Count 
        FROM moma_works
        GROUP BY department
        ORDER BY COUNT DESC 
    '''

    dataframe = sql_to_df(query)
    _fig, axes = plt.subplots(figsize=(10, 5))
    axes.set_title(title, fontsize=14)

    # get evenly spaced x-axis positions
    xpos = np.arange(len(dataframe))
    # at each x, add bar (height based on count data)
    axes.bar(xpos, dataframe["count"], width=0.50)
    # at each x, add tick mark
    axes.set_xticks(xpos)
    # at each x, add label based on dept data
    axes.set_xticklabels(dataframe["department"])
    # label y-axis
    axes.set_ylabel("Count", fontsize=12)
    # rotate x-axis labels to prevent overlap
    plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.show()


task1()

# %% Task 2 Cell


def task2():
    """Perform Task 2."""

    title = "Artworks by Classification"
    # TODO task 2
    query = '''
        SELECT classification AS classification, COUNT(id) AS count
        FROM moma_works
        GROUP BY classification
        HAVING COUNT(id) < 100
        ORDER BY COUNT DESC
    '''

    dataframe = sql_to_df(query)
    _fig, axes = plt.subplots(figsize=(10, 5))
    axes.set_title(title, fontsize=14)

    xpos = np.arange(len(dataframe))
    axes.bar(xpos, dataframe["count"], width=0.50)
    axes.set_xticks(xpos)
    axes.set_xticklabels(dataframe["classification"])
    axes.set_ylabel("Count", fontsize=12)
    plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.show()


task2()


# %% Task 3 Cell


def task3():
    """Perform Task 3."""

    title = "Artists by Nationality"
    # TODO task 3
    query = """
        WITH nats AS(
            SELECT
            info ->> 'nationality' AS nationality
            FROM moma_artists
        )
        SELECT nationality, COUNT(nationality) AS count
        FROM nats
        WHERE nationality IS NOT NULL
        GROUP BY nationality
        ORDER BY COUNT DESC
        LIMIT 10
    """

    dataframe = sql_to_df(query)
    _fig, axes = plt.subplots(figsize=(10, 5))
    axes.set_title(title, fontsize=14)

    xpos = np.arange(len(dataframe))
    axes.bar(xpos, dataframe["count"], width=0.50)
    axes.set_xticks(xpos)
    axes.set_xticklabels(dataframe["nationality"])
    axes.set_ylabel("Count", fontsize=12)

    plt.show()


task3()

# %% Task 4 Cell


def task4():
    """Perform Task 4."""

    title = "Artists by Gender"
    # TODO task 4
    query = """
        SELECT LOWER(info ->> 'gender') AS gender,
        COUNT(*) AS count 
        FROM moma_artists
        GROUP BY gender
        HAVING LOWER(info ->> 'gender') IS NOT NULL
        ORDER BY gender;
    """

    dataframe = sql_to_df(query)
    fig, axes = plt.subplots(figsize=(10, 5))
    axes.set_title(title, fontsize=14)

    fig.set_facecolor('white')
    axes.pie(
        x=dataframe["count"],
        labels=dataframe["gender"],
        autopct='%1.1f%%',
        colors=['lightcoral', 'skyblue', 'lavender']
    )
    # Equal aspect ratio ensures that pie is drawn as a circle.
    axes.axis('equal')

    plt.show()


task4()

# %% Task 5 Cell: Describe this chart


def task5():
    """Perform Task 5."""

    title = "?"
    # TODO task 5
    query = """
            WITH daily_acquisition_count AS (
                SELECT date_acquired, COUNT(*) FROM moma_works 
                WHERE date_acquired IS NOT NULL 
                GROUP BY date_acquired
            )
            SELECT date_acquired, SUM(count) 
            OVER (ORDER BY date_acquired) FROM daily_acquisition_count;
            """
    dataframe = sql_to_df(query)
    _fig, axes = plt.subplots(figsize=(10, 5))
    axes.set_title(title, fontsize=14)

    xpos = np.arange(len(dataframe))
    axes.bar(xpos, dataframe["sum"], width=0.50)
    axes.set_xticks([
        0,
        len(dataframe) // 2,
        len(dataframe)
    ])
    axes.set_xticklabels(dataframe.iloc[[
        0,
        len(dataframe) // 2,
        -1
    ]]["date_acquired"])
    axes.set_ylabel("Count", fontsize=12)

    plt.show()


task5()

# %%
