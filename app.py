from flask import Flask, request, jsonify, render_template
import requests

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

        return round((result),10)
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
    try:
        unitvalue_1 = float(unitvalue_1)
        
        # Dicionário para armazenar as conversões de 'g' para outras unidades
        g_conversions = {
            'kg': unitvalue_1 / 1000,
            'g': unitvalue_1,
            'ton': unitvalue_1 / 1000000,
            'lbs': unitvalue_1 / 453.592,
            'oz': unitvalue_1 / 28.34952
        }
        
        # Dicionário para armazenar as conversões de 'kg' para outras unidades
        kg_conversions = {
            'g': unitvalue_1 * 1000,
            'ton': unitvalue_1 / 1000,
            'lbs': unitvalue_1 * 2.204623,
            'oz': unitvalue_1 * 35.27396,
            'kg': unitvalue_1
        }
        
        # Dicionário para armazenar as conversões de 'ton' para outras unidades
        ton_conversions = {
            'g': unitvalue_1 * 1000000,
            'kg': unitvalue_1 * 1000,
            'lbs': unitvalue_1 * 2204.6,
            'oz': unitvalue_1 * 35274,
            'ton': unitvalue_1
        }
        
        # Dicionário para armazenar as conversões de 'lbs' para outras unidades
        lbs_conversions = {
            'g': unitvalue_1 * 453.592,
            'ton': unitvalue_1 / 2204.6,
            'kg': unitvalue_1 / 2.2046,
            'oz': unitvalue_1 * 16,
            'lbs': unitvalue_1
        }
        
        # Dicionário para armazenar as conversões de 'oz' para outras unidades
        oz_conversions = {
            'g': unitvalue_1 * 28.34952,
            'ton': unitvalue_1 / 35273.96,
            'kg': unitvalue_1 / 35.27396,
            'lbs': unitvalue_1 / 16,
            'oz': unitvalue_1
        }
        # Dicionário para armazenar as conversões de 'm/s' para outras unidades
        m_s_conversions = {
            'm/s': unitvalue_1,
            'km/h': unitvalue_1 * 3.6,
            'mi/s': unitvalue_1 / 1609.34,
            'mi/h': unitvalue_1 * 2.23694,
            'ft/s': unitvalue_1 * 3.28084,
            'ft/h': unitvalue_1 * 11811.02,
            'yd/s': unitvalue_1 * 1.09361,
            'yd/h': unitvalue_1 * 3937.00787
        }

        # Dicionário para armazenar as conversões de 'km/h' para outras unidades
        km_h_conversions = {
            'km/h': unitvalue_1,
            'm/s': unitvalue_1 / 3.6,
            'mi/s': unitvalue_1 / 5793.64,
            'mi/h': unitvalue_1 / 1.60934,
            'ft/s': unitvalue_1 / 1.09728,
            'ft/h': unitvalue_1 * 3280.84,
            'yd/s': unitvalue_1 / 3.281,
            'yd/h': unitvalue_1 * 1093.61
        }

        # Dicionário para armazenar as conversões de 'mi/s' para outras unidades
        mi_s_conversions = {
            'mi/s': unitvalue_1,
            'm/s': unitvalue_1 * 1609.34,
            'km/h': unitvalue_1 * 5793.64,
            'mi/h': unitvalue_1 * 3600,
            'ft/s': unitvalue_1 * 5280,
            'ft/h': unitvalue_1 * 19008000,
            'yd/s': unitvalue_1 * 1760,
            'yd/h': unitvalue_1 * 6336000
        }

        # Dicionário para armazenar as conversões de 'mi/h' para outras unidades
        mi_h_conversions = {
            'mi/h': unitvalue_1,
            'm/s': unitvalue_1 / 2.23694,
            'km/h': unitvalue_1 * 1.60934,
            'mi/s': unitvalue_1 / 3600,
            'ft/s': unitvalue_1 * 1.46667,
            'ft/h': unitvalue_1 * 5280,
            'yd/s': unitvalue_1 / 3,
            'yd/h': unitvalue_1 * 1760
        }

        # Dicionário para armazenar as conversões de 'ft/s' para outras unidades
        ft_s_conversions = {
            'ft/s': unitvalue_1,
            'm/s': unitvalue_1 / 3.28084,
            'km/h': unitvalue_1 * 1.09728,
            'mi/s': unitvalue_1 / 5280,
            'mi/h': unitvalue_1 / 1.46667,
            'ft/h': unitvalue_1 * 3600,
            'yd/s': unitvalue_1 / 3,
            'yd/h': unitvalue_1 * 1200
        }

        # Dicionário para armazenar as conversões de 'ft/h' para outras unidades
        ft_h_conversions = {
            'ft/h': unitvalue_1,
            'm/s': unitvalue_1 / 11811.02,
            'km/h': unitvalue_1 / 3280.84,
            'mi/s': unitvalue_1 / 19008000,
            'mi/h': unitvalue_1 / 5280,
            'ft/s': unitvalue_1 / 3600,
            'yd/s': unitvalue_1 / 10800,
            'yd/h': unitvalue_1 / 3
        }

        # Dicionário para armazenar as conversões de 'yd/s' para outras unidades
        yd_s_conversions = {
            'yd/s': unitvalue_1,
            'm/s': unitvalue_1 / 1.09361,
            'km/h': unitvalue_1 * 3.6,
            'mi/s': unitvalue_1 / 1760,
            'mi/h': unitvalue_1 * 2.04545,
            'ft/s': unitvalue_1 * 3,
            'ft/h': unitvalue_1 * 10800,
            'yd/h': unitvalue_1 * 3600
        }

        # Dicionário para armazenar as conversões de 'yd/h' para outras unidades
        yd_h_conversions = {
            'yd/h': unitvalue_1,
            'm/s': unitvalue_1 / 3937.00787,
            'km/h': unitvalue_1 / 1093.61,
            'mi/s': unitvalue_1 / 6336000,
            'mi/h': unitvalue_1 / 1760,
            'ft/s': unitvalue_1 / 1200,
            'ft/h': unitvalue_1 * 3,
            'yd/s': unitvalue_1 / 3600
        }
        # Dicionário para armazenar as conversões de 'mL' para outras unidades
        mL_conversions = {
            'mL': unitvalue_1,
            'L': unitvalue_1 / 1000,
            'm³': unitvalue_1 / 1e6,
            'km³': unitvalue_1 / 1e15,
            'cm³': unitvalue_1,
            'gal': unitvalue_1 / 3785.41
        }

        # Dicionário para armazenar as conversões de 'L' para outras unidades
        L_conversions = {
            'mL': unitvalue_1 * 1000,
            'L': unitvalue_1,
            'm³': unitvalue_1 / 1000,
            'km³': unitvalue_1 / 1e12,
            'cm³': unitvalue_1 * 1000,
            'gal': unitvalue_1 / 3.78541
        }

        # Dicionário para armazenar as conversões de 'm³' para outras unidades
        m3_conversions = {
            'mL': unitvalue_1 * 1e6,
            'L': unitvalue_1 * 1000,
            'm³': unitvalue_1,
            'km³': unitvalue_1 / 1e9,
            'cm³': unitvalue_1 * 1e6,
            'gal': unitvalue_1 * 264.172
        }

        # Dicionário para armazenar as conversões de 'km³' para outras unidades
        km3_conversions = {
            'mL': unitvalue_1 * 1e15,
            'L': unitvalue_1 * 1e12,
            'm³': unitvalue_1 * 1e9,
            'km³': unitvalue_1,
            'cm³': unitvalue_1 * 1e15,
            'gal': unitvalue_1 * 2.64172e11
        }

        # Dicionário para armazenar as conversões de 'cm³' para outras unidades
        cm3_conversions = {
            'mL': unitvalue_1,
            'L': unitvalue_1 / 1000,
            'm³': unitvalue_1 / 1e6,
            'km³': unitvalue_1 / 1e15,
            'cm³': unitvalue_1,
            'gal': unitvalue_1 / 3785.41
        }

        # Dicionário para armazenar as conversões de 'gal' para outras unidades
        gal_conversions = {
            'mL': unitvalue_1 * 3785.41,
            'L': unitvalue_1 * 3.78541,
            'm³': unitvalue_1 / 264.172,
            'km³': unitvalue_1 / 2.64172e11,
            'cm³': unitvalue_1 * 3785.41,
            'gal': unitvalue_1
        }
        # Dicionário para armazenar as conversões de 'cm²' para outras unidades
        cm2_conversions = {
            'cm²': unitvalue_1,
            'm²': unitvalue_1 / 10000,
            'km²': unitvalue_1 / 1e10,
            'ha': unitvalue_1 / 1e8,
            'ac': unitvalue_1 / 40468564.224
        }

        # Dicionário para armazenar as conversões de 'm²' para outras unidades
        m2_conversions = {
            'cm²': unitvalue_1 * 10000,
            'm²': unitvalue_1,
            'km²': unitvalue_1 / 1e6,
            'ha': unitvalue_1 / 10000,
            'ac': unitvalue_1 / 4046.856
        }

        # Dicionário para armazenar as conversões de 'km²' para outras unidades
        km2_conversions = {
            'cm²': unitvalue_1 * 1e10,
            'm²': unitvalue_1 * 1e6,
            'km²': unitvalue_1,
            'ha': unitvalue_1 * 100,
            'ac': unitvalue_1 * 247.105
        }

        # Dicionário para armazenar as conversões de 'ha' (hectares) para outras unidades
        ha_conversions = {
            'cm²': unitvalue_1 * 1e8,
            'm²': unitvalue_1 * 10000,
            'km²': unitvalue_1 / 100,
            'ha': unitvalue_1,
            'ac': unitvalue_1 * 2.47105
        }

        # Dicionário para armazenar as conversões de 'ac' (acres) para outras unidades
        ac_conversions = {
            'cm²': unitvalue_1 * 40468564.224,
            'm²': unitvalue_1 * 4046.856,
            'km²': unitvalue_1 / 247.105,
            'ha': unitvalue_1 / 2.47105,
            'ac': unitvalue_1
        }
        # Dicionário para armazenar as conversões de 'cm' para outras unidades
        cm_conversions = {
            'cm': unitvalue_1,
            'm': unitvalue_1 / 100,
            'km': unitvalue_1 / 100000,
            'yd': unitvalue_1 / 91.44,
            'ft': unitvalue_1 / 30.48,
            'in': unitvalue_1 / 2.54
        }

        # Dicionário para armazenar as conversões de 'm' para outras unidades
        m_conversions = {
            'cm': unitvalue_1 * 100,
            'm': unitvalue_1,
            'km': unitvalue_1 / 1000,
            'yd': unitvalue_1 * 1.09361,
            'ft': unitvalue_1 * 3.28084,
            'in': unitvalue_1 * 39.3701
        }

        # Dicionário para armazenar as conversões de 'km' para outras unidades
        km_conversions = {
            'cm': unitvalue_1 * 100000,
            'm': unitvalue_1 * 1000,
            'km': unitvalue_1,
            'yd': unitvalue_1 * 1093.61,
            'ft': unitvalue_1 * 3280.84,
            'in': unitvalue_1 * 39370.1
        }

        # Dicionário para armazenar as conversões de 'yd' para outras unidades
        yd_conversions = {
            'cm': unitvalue_1 * 91.44,
            'm': unitvalue_1 / 1.09361,
            'km': unitvalue_1 / 1093.61,
            'yd': unitvalue_1,
            'ft': unitvalue_1 * 3,
            'in': unitvalue_1 * 36
        }

        # Dicionário para armazenar as conversões de 'ft' para outras unidades
        ft_conversions = {
            'cm': unitvalue_1 * 30.48,
            'm': unitvalue_1 / 3.28084,
            'km': unitvalue_1 / 3280.84,
            'yd': unitvalue_1 / 3,
            'ft': unitvalue_1,
            'in': unitvalue_1 * 12
        }

        # Dicionário para armazenar as conversões de 'in' para outras unidades
        in_conversions = {
            'cm': unitvalue_1 * 2.54,
            'm': unitvalue_1 / 39.3701,
            'km': unitvalue_1 / 39370.1,
            'yd': unitvalue_1 / 36,
            'ft': unitvalue_1 / 12,
            'in': unitvalue_1
        }
        # Dicionário para armazenar as conversões de 'K' (Kelvin) para outras unidades
        K_conversions = {
            'K': unitvalue_1,
            '°C': unitvalue_1 - 273.15,
            '°F': (unitvalue_1 - 273.15) * 9/5 + 32,
            '°R': unitvalue_1 * 1.8
        }
        # Dicionário para armazenar as conversões de '°C' (Celsius) para outras unidades
        C_conversions = {
            'K': unitvalue_1 + 273.15,
            '°C': unitvalue_1,
            '°F': unitvalue_1 * 9/5 + 32,
            '°R': (unitvalue_1 + 273.15) * 1.8
        }
        # Dicionário para armazenar as conversões de '°F' (Fahrenheit) para outras unidades
        F_conversions = {
            'K': (unitvalue_1 - 32) * 5/9 + 273.15,
            '°C': (unitvalue_1 - 32) * 5/9,
            '°F': unitvalue_1,
            '°R': unitvalue_1 + 459.67
        }
        # Dicionário para armazenar as conversões de '°R' (Rankine) para outras unidades
        R_conversions = {
            'K': unitvalue_1 / 1.8,
            '°C': (unitvalue_1 - 491.67) * 5/9,
            '°F': unitvalue_1 - 459.67,
            '°R': unitvalue_1
        }
        # Dicionário para mapeamento de conversão de unidades
        conversion_map = {
            'g': g_conversions,
            'kg': kg_conversions,
            'ton': ton_conversions,
            'lbs': lbs_conversions,
            'oz': oz_conversions,
            'm/s': m_s_conversions,
            'km/h': km_h_conversions,
            'mi/s': mi_s_conversions,
            'mi/h': mi_h_conversions,
            'ft/s': ft_s_conversions,
            'ft/h': ft_h_conversions,
            'yd/s': yd_s_conversions,
            'yd/h': yd_h_conversions,
            'mL': mL_conversions,
            'L': L_conversions,
            'm³': m3_conversions,
            'km³': km3_conversions,
            'cm³': cm3_conversions,
            'gal': gal_conversions,
            'cm²': cm2_conversions,
            'm²': m2_conversions,
            'km²': km2_conversions,
            'ha': ha_conversions,
            'ac': ac_conversions,
            'cm': cm_conversions,
            'm': m_conversions,
            'km': km_conversions,
            'yd': yd_conversions,
            'ft': ft_conversions,
            'in': in_conversions,
            'K': K_conversions,
            '°C': C_conversions,
            '°F': F_conversions,
            '°R': R_conversions
        }
    
        # Realiza a conversão utilizando o mapeamento
        unitResult = conversion_map.get(unit1, {}).get(unit2, "Erro: Conversão inválida.")
        
        return round((unitResult),10)
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


import requests

#Em desenvolvimento

def get_currency_value(base_currency='BTC', target_currencies=['BTC', 'BRL', 'EUR', 'JPY', 'GBP','USD']):
    try:
        # URL para busca das taxas de conversão para USD
        #url = 'https://api.exchangerate-api.com/v4/latest/USD'
                # URL para busca das taxas de conversão para BTC
        url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
        response = requests.get(url)
        data = response.json()
        
        # Extraí os rates das moedas da API
        rates = data.get('data', {}).get('rates', {})
        
        # Inicializa o dicionário para armazenar os valores
        values = {}
        
        for currency in target_currencies:
                value = rates.get(currency.upper(), 'Moeda não encontrada')
                values[currency] = value
                
        return values
    except Exception as e:
        print(f"Erro na busca dos valores de moeda: {str(e)}", flush=True)
        return None

def coin_conversion(coin1, coin2, coinvalue_1): 
    print(f"coinvalue_1 (before conversion): {coinvalue_1}")
    try:
        # Garante que coinvalue_1 é um número válido
        try:
            coinvalue_1 = float(coinvalue_1)
        except ValueError:
            return "Erro: Entrada inválida para o valor da moeda. Por favor forneça um número válido."
        
        # Busca os valores de moeda
        currency_values = get_currency_value(base_currency='BTC', target_currencies=[coin1, coin2])
        
        if not currency_values:
            return "Erro: Valores de moeda não puderam ser buscados."
        
        # Checa se os valores de coin1 e coin2 existem
        coin1_value = currency_values.get(coin1.upper())
        coin2_value = currency_values.get(coin2.upper())
        
        if coin1_value is None or coin2_value is None:
            return "Erro: Uma ou ambas moedas não estão disponíveis na resposta da API."
        
        print(f"coin1_value (before cleaning): {coin1_value}")
        print(f"coin2_value (before cleaning): {coin2_value}")
        
        coin1_value = float(coin1_value.replace(",", "").strip()) if isinstance(coin1_value, str) else float(coin1_value)
        coin2_value = float(coin2_value.replace(",", "").strip()) if isinstance(coin2_value, str) else float(coin2_value)
        
        # Converte o coinvalue_1 de coin1 para BTC e então de BTC para coin2
        value_in_usd = coinvalue_1 / coin1_value
        converted_value = value_in_usd * coin2_value
        
        return round(converted_value, 4)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/coin_conversion', methods=['POST'])
def handle_coin_conversion():
    data = request.get_json()
    
    coin1 = data.get('coin1')
    coin2 = data.get('coin2')
    coinvalue_1 = data.get('coinvalue_1')
    
    coinResult = coin_conversion(coin1, coin2, coinvalue_1)
    
    return jsonify(coinResult=str(coinResult))


if __name__ == '__main__':
    app.run(debug=True)
