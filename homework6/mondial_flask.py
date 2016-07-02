## Country information server
#   curl http://localhost:5000/countries?lookup_name=France
#   Returns the population of country
#   France, Paris, 64933400

# display info for all countries
# importing jsonify to transform python dictionaries into json
from flask import Flask, request, render_template, jsonify
import numbers, decimal, fractions
from numbers import Number
from decimal import Decimal
#from fractions import Fraction




import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user="Monica")

@app.route("/lakes")
def get_lakes():
    cursor = conn.cursor()
    # can set a population_gt to say how large the population may be .
    type = str(request.args.get('type', 0))

    if type:
        cursor.execute(
            """
        SELECT name, altitude, area, type
        FROM lake
        WHERE type = %s
        ORDER BY name
        """, [type])
    else:
        cursor.execute(
            """SELECT name, altitude, area, type
            FROM lake
            ORDER BY name""")
    output = []
    for item in cursor.fetchall():
        # for value in item:
        #     print(value)
        #     if isinstance(value, Number):
        #         value = int(value)
        #         print("Converted", value)
        #         print(type(value))
        #     #else:
        #     #    value = str(value)
        #
        #     if isinstance(value, decimal.Decimal):
        #         value = float(value)
        #         value = int(value)
        #         print("Converted", value)
        #         print(type(value))


        # This will use 0 in the case when you provide any value that
        #Python considers False, such as None, 0, [], "",
        # etc. Since 0 is False, you should only use 0 as the
        # alternative value (otherwise you will find your 0s turning into that value).

        output.append({'name': item[0],
        'altitude': float(item[1] or 0),
        'area': float(item[2] or 0),
        'type': item[3]})

    # return all of the rivers
    return jsonify(output)


app.run(debug=True)
