##Development by Gustavo Arteaga 
## 4 22 2023

from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask,jsonify,redirect, make_response
# from flask_cors import CORS
# from flask_cors import cross_origin
from pulp import LpVariable, LpProblem, lpSum, value, LpMinimize

app = Flask(__name__)
# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/solve-sudoku", methods = ['POST'])
def sudoku():
    # input_data:
    jsonInput = request.get_json()
    puzzle = jsonInput['puzzle']

    print(puzzle)

    # solution = initialProblem
    
    # Initialize the problem
    prob = LpProblem("Sudoku Problem", LpMinimize)
    
    # Create the decision variables
    choices = LpVariable.dicts("Choice", (range(9), range(9), range(1, 10)), cat='Binary')
    
    # Add the objective function (not needed for solving Sudoku)
    prob += 0
    
    # Add the constraints
    for r in range(9):
        for c in range(9):
            prob += lpSum(choices[r][c][n] for n in range(1, 10)) == 1
            
    for r in range(9):
        for n in range(1, 10):
            prob += lpSum(choices[r][c][n] for c in range(9)) == 1
            
    for c in range(9):
        for n in range(1, 10):
            prob += lpSum(choices[r][c][n] for r in range(9)) == 1
            
    for br in range(3):
        for bc in range(3):
            for n in range(1, 10):
                prob += lpSum(choices[r+3*br][c+3*bc][n] for r in range(3) for c in range(3)) == 1
    
    # Set the initial values for the known cells
    known_values = [(r, c, puzzle[r][c]) for r in range(9) for c in range(9) if puzzle[r][c] != 0]
    for r, c, n in known_values:
        prob += choices[r][c][n] == 1
        
    # Solve the problem
    prob.solve()
    
    # Print the solution
    solution = [[0 for c in range(9)] for r in range(9)]
    for r in range(9):
        for c in range(9):
            for n in range(1, 10):
                if value(choices[r][c][n]) == 1:
                    solution[r][c] = n
    print(solution)

   

    res = make_response(jsonify(solution), 200)
    return res

@app.route("/vlesim", methods = ['GET'])
def vlesim():
    return "<p>VLESIM POWER </p>"


@app.route("/")
def hello_world():
    return "<p>Welcome to solver Sudoku 🐉</p>"


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = 3000)
