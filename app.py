from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Função que realizará o cálculo
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

        return result
    except ValueError:
        return "Erro: Entrada inválida. Por favor forneceça números."
    
#Rota para renderizar a página "calculator"
@app.route('/')
def calculator():
    return render_template('calculator.html')

#Rota para manipular o calculo
@app.route('/calculate', methods=['POST'])
def handle_calculation():
    data = request.get_json()
    
    operation = data.get('operation')
    number_1 = data.get('number_1')
    number_2 = data.get('number_2')
    
    result = calculate(operation, number_1, number_2)
    
    return jsonify(result=str(result))

# Função que realizará a conversão de unidade de medida
def unitConversion(unit1, unit2, unitvalue_1):
    print(f'unit1: {unit1}')
    print(f'unit2: {unit2}')
    print(f'unitvalue_1: {unitvalue_1}')
    
    try:
        unitvalue_1 = float(unitvalue_1)
        
        # Dictionary to store conversions from 'g' to other units
        g_conversions = {
            'kg': unitvalue_1 / 1000,
            'g': unitvalue_1,
            'ton': unitvalue_1 / 1000000,
            'lbs': unitvalue_1 / 453.592,
            'oz': unitvalue_1 / 28.34952
        }
        
        # Dictionary to store conversions from 'kg' to other units
        kg_conversions = {
            'g': unitvalue_1 * 1000,
            'ton': unitvalue_1 / 1000,
            'lbs': unitvalue_1 * 2.204623,
            'oz': unitvalue_1 * 35.27396,
            'kg': unitvalue_1
        }
        
        # Dictionary to store conversions from 'ton' to other units
        ton_conversions = {
            'g': unitvalue_1 * 1000000,
            'kg': unitvalue_1 * 1000,
            'lbs': unitvalue_1 * 2204.6,
            'oz': unitvalue_1 * 35274,
            'ton': unitvalue_1
        }
        
        # Dictionary to store conversions from 'lbs' to other units
        lbs_conversions = {
            'g': unitvalue_1 * 453.592,
            'ton': unitvalue_1 / 2204.6,
            'kg': unitvalue_1 / 2.2046,
            'oz': unitvalue_1 * 16,
            'lbs': unitvalue_1
        }
        
        # Dictionary to store conversions from 'oz' to other units
        oz_conversions = {
            'g': unitvalue_1 * 28.34952,
            'ton': unitvalue_1 / 35273.96,
            'kg': unitvalue_1 / 35.27396,
            'lbs': unitvalue_1 / 16,
            'oz': unitvalue_1
        }
        
        # Dictionary for unit conversion maps
        conversion_map = {
            'g': g_conversions,
            'kg': kg_conversions,
            'ton': ton_conversions,
            'lbs': lbs_conversions,
            'oz': oz_conversions
        }
        
        # Perform the conversion using the map
        unitResult = conversion_map.get(unit1, {}).get(unit2, "Erro: Conversão inválida.")
        
        return unitResult
    except ValueError:
        return "Erro: Entrada inválida. Por favor forneça números."
    

#Rota para manipular o calculo
@app.route('/unitConversion', methods=['POST'])
def handle_conversion():
    data = request.get_json()
    
    unit1 = data.get('unit1')
    unit2 = data.get('unit2')
    unitvalue_1 = data.get('unitvalue_1')
    
    unitResult = unitConversion(unit1, unit2, unitvalue_1)
    
    return jsonify(unitResult=str(unitResult))


if __name__ == '__main__':
    app.run(debug=True)
