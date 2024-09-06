from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to perform the calculation
def calculate(operation, number_1, number_2):
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
        
        if operation == '+':
            result = number_1 + number_2
        elif operation == '-':
            result = number_1 - number_2
        elif operation == '*':
            result = number_1 * number_2
        elif operation == '/':
            if number_2 != 0:
                result = number_1 / number_2
            else:
                return "Erro: Divisão por zero não é permitida."
        else:
            return "Erro: Operador inválido."

        return result
    except ValueError:
        return "Erro: Entrada inválida. Por favor forneceça números."

# Route to render the calculator page
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Route to handle the calculation
@app.route('/calculate', methods=['POST'])
def handle_calculation():
    data = request.get_json()
    
    operation = data.get('operation')
    number_1 = data.get('number_1')
    number_2 = data.get('number_2')
    
    result = calculate(operation, number_1, number_2)
    
    return jsonify(result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
