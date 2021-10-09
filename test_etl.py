#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='datastream',
    password='euro-21-Stat',
    account='om76184.eu-central-1'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    test=cs.execute ("CREATE OR REPLACE TABLE societyai_raw.public.test_etl AS (SELECT * FROM societyai.public.yearly_gdp_nuts)")
    display = test.fetchall()
    print(one_row[0])
    print(display[20])
#ALWAYS CLOSE THE CONNECTION
finally:
    cs.close()
ctx.close()
