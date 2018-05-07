#!/usr/bin/python 2.7

import psycopg2

DBNAME = "news"


def get_popular_articles():
    """Return most popular three articles of all time, most popular on top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as views from articles,\
              log where articles.slug=substr(log.path, 10, 100) \
              group by articles.title order by views desc limit 3")
    r_articles = c.fetchall()
    for row in r_articles:
        print row[0], "|", row[1], "views"
    db.close()


def get_popular_authors():
    """Return most popular three articles of all time, most popular on top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as views from slugauthor,\
              log where slugauthor.slug=substr(log.path, 10, 100)\
              group by name order by views desc limit 4")
    r_authors = c.fetchall()
    for row in r_authors:
        print row[0], "|", row[1], "views"
    db.close()


def get_err_days():
    """Return days when more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select badreqts.date,\
              cast(badreqts.errreqts as float)/totreqts.reqts * 100\
              as errpercent from totreqts, badreqts\
              where totreqts.date=badreqts.date and\
              cast(badreqts.errreqts as float)/totreqts.reqts * 100 > 1")
    r_days = c.fetchall()
    for row in r_days:
        print row[0], "|", ('%.2f' % row[1]), "% errors"
    db.close()

print(" \nMost popular three articles of all time -  \n ")
get_popular_articles()
print("\nMost popular authors of all time -  \n ")
get_popular_authors()
print("\nDays when more than 1% of requests lead to errors - \n ")
get_err_days()
