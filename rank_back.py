from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def space():
    with open('./data/rank.csv') as file:
        data = file.readlines()
        table = '<table  class="table table-condensed table-hover table-striped">'
        
        first = '<thead>'
        first += '<tr>'
        for colname in data[0].strip().split(','):
            first += '<th>'
            first += colname
            first += '</th>'
        first += '</tr>'
        first += '</thead>'

        table += first
        table += '<tbody>'
        for line in data[1:]:
            table += '<tr>'
            for col in line.strip().split(','):
                table += '<td>';
                table += col;
                table += '</td>';
            table += '</tr>'

        table += '</tbody>'
        table += '</table>'

    html = """<html>
                    <head>
                        <title>Welcome</title>
                    </head>
                    <style>
                        table {
                        border-collapse: collapse;
                        }

                        table, th, td {
                        border: 1px solid black;
                        }
                    </style>
                    <body>
                        <h1>Ranking Table</h1>"""
    html += table
    html += """
                </body>
            </html>"""
    return html

if __name__ == "__main__":
    app.run()