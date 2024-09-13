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

        # Dictionary to store conversions from 'km/h' to other units
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

        # Dictionary to store conversions from 'mi/s' to other units
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

        # Dictionary to store conversions from 'mi/h' to other units (identical to 'mi/s')
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

        # Dictionary to store conversions from 'ft/s' to other units
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

        # Dictionary to store conversions from 'ft/h' to other units
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

        # Dictionary to store conversions from 'yd/s' to other units
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

        # Dictionary to store conversions from 'yd/h' to other units
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
        # Dictionary to store conversions from 'mL' to other units
        mL_conversions = {
            'mL': unitvalue_1,
            'L': unitvalue_1 / 1000,
            'm³': unitvalue_1 / 1e6,
            'km³': unitvalue_1 / 1e15,
            'cm³': unitvalue_1,
            'gal': unitvalue_1 / 3785.41
        }

        # Dictionary to store conversions from 'L' to other units
        L_conversions = {
            'mL': unitvalue_1 * 1000,
            'L': unitvalue_1,
            'm³': unitvalue_1 / 1000,
            'km³': unitvalue_1 / 1e12,
            'cm³': unitvalue_1 * 1000,
            'gal': unitvalue_1 / 3.78541
        }

        # Dictionary to store conversions from 'm³' to other units
        m3_conversions = {
            'mL': unitvalue_1 * 1e6,
            'L': unitvalue_1 * 1000,
            'm³': unitvalue_1,
            'km³': unitvalue_1 / 1e9,
            'cm³': unitvalue_1 * 1e6,
            'gal': unitvalue_1 * 264.172
        }

        # Dictionary to store conversions from 'km³' to other units
        km3_conversions = {
            'mL': unitvalue_1 * 1e15,
            'L': unitvalue_1 * 1e12,
            'm³': unitvalue_1 * 1e9,
            'km³': unitvalue_1,
            'cm³': unitvalue_1 * 1e15,
            'gal': unitvalue_1 * 2.64172e11
        }

        # Dictionary to store conversions from 'cm³' to other units
        cm3_conversions = {
            'mL': unitvalue_1,
            'L': unitvalue_1 / 1000,
            'm³': unitvalue_1 / 1e6,
            'km³': unitvalue_1 / 1e15,
            'cm³': unitvalue_1,
            'gal': unitvalue_1 / 3785.41
        }

        # Dictionary to store conversions from 'gal' to other units
        gal_conversions = {
            'mL': unitvalue_1 * 3785.41,
            'L': unitvalue_1 * 3.78541,
            'm³': unitvalue_1 / 264.172,
            'km³': unitvalue_1 / 2.64172e11,
            'cm³': unitvalue_1 * 3785.41,
            'gal': unitvalue_1
        }
        # Dictionary to store conversions from 'cm²' to other units
        cm2_conversions = {
            'cm²': unitvalue_1,
            'm²': unitvalue_1 / 10000,
            'km²': unitvalue_1 / 1e10,
            'ha': unitvalue_1 / 1e8,
            'ac': unitvalue_1 / 40468564.224
        }

        # Dictionary to store conversions from 'm²' to other units
        m2_conversions = {
            'cm²': unitvalue_1 * 10000,
            'm²': unitvalue_1,
            'km²': unitvalue_1 / 1e6,
            'ha': unitvalue_1 / 10000,
            'ac': unitvalue_1 / 4046.856
        }

        # Dictionary to store conversions from 'km²' to other units
        km2_conversions = {
            'cm²': unitvalue_1 * 1e10,
            'm²': unitvalue_1 * 1e6,
            'km²': unitvalue_1,
            'ha': unitvalue_1 * 100,
            'ac': unitvalue_1 * 247.105
        }

        # Dictionary to store conversions from 'ha' (hectares) to other units
        ha_conversions = {
            'cm²': unitvalue_1 * 1e8,
            'm²': unitvalue_1 * 10000,
            'km²': unitvalue_1 / 100,
            'ha': unitvalue_1,
            'ac': unitvalue_1 * 2.47105
        }

        # Dictionary to store conversions from 'ac' (acres) to other units
        ac_conversions = {
            'cm²': unitvalue_1 * 40468564.224,
            'm²': unitvalue_1 * 4046.856,
            'km²': unitvalue_1 / 247.105,
            'ha': unitvalue_1 / 2.47105,
            'ac': unitvalue_1
        }
        # Dictionary to store conversions from 'cm' to other units
        cm_conversions = {
            'cm': unitvalue_1,
            'm': unitvalue_1 / 100,
            'km': unitvalue_1 / 100000,
            'yd': unitvalue_1 / 91.44,
            'ft': unitvalue_1 / 30.48,
            'in': unitvalue_1 / 2.54
        }

        # Dictionary to store conversions from 'm' to other units
        m_conversions = {
            'cm': unitvalue_1 * 100,
            'm': unitvalue_1,
            'km': unitvalue_1 / 1000,
            'yd': unitvalue_1 * 1.09361,
            'ft': unitvalue_1 * 3.28084,
            'in': unitvalue_1 * 39.3701
        }

        # Dictionary to store conversions from 'km' to other units
        km_conversions = {
            'cm': unitvalue_1 * 100000,
            'm': unitvalue_1 * 1000,
            'km': unitvalue_1,
            'yd': unitvalue_1 * 1093.61,
            'ft': unitvalue_1 * 3280.84,
            'in': unitvalue_1 * 39370.1
        }

        # Dictionary to store conversions from 'yd' to other units
        yd_conversions = {
            'cm': unitvalue_1 * 91.44,
            'm': unitvalue_1 / 1.09361,
            'km': unitvalue_1 / 1093.61,
            'yd': unitvalue_1,
            'ft': unitvalue_1 * 3,
            'in': unitvalue_1 * 36
        }

        # Dictionary to store conversions from 'ft' to other units
        ft_conversions = {
            'cm': unitvalue_1 * 30.48,
            'm': unitvalue_1 / 3.28084,
            'km': unitvalue_1 / 3280.84,
            'yd': unitvalue_1 / 3,
            'ft': unitvalue_1,
            'in': unitvalue_1 * 12
        }

        # Dictionary to store conversions from 'in' to other units
        in_conversions = {
            'cm': unitvalue_1 * 2.54,
            'm': unitvalue_1 / 39.3701,
            'km': unitvalue_1 / 39370.1,
            'yd': unitvalue_1 / 36,
            'ft': unitvalue_1 / 12,
            'in': unitvalue_1
        }
        # Dictionary to store conversions from 'K' (Kelvin) to other units
        K_conversions = {
            'K': unitvalue_1,
            '°C': unitvalue_1 - 273.15,
            '°F': (unitvalue_1 - 273.15) * 9/5 + 32,
            '°R': unitvalue_1 * 1.8
        }
        # Dictionary to store conversions from '°C' (Celsius) to other units
        C_conversions = {
            'K': unitvalue_1 + 273.15,
            '°C': unitvalue_1,
            '°F': unitvalue_1 * 9/5 + 32,
            '°R': (unitvalue_1 + 273.15) * 1.8
        }
        # Dictionary to store conversions from '°F' (Fahrenheit) to other units
        F_conversions = {
            'K': (unitvalue_1 - 32) * 5/9 + 273.15,
            '°C': (unitvalue_1 - 32) * 5/9,
            '°F': unitvalue_1,
            '°R': unitvalue_1 + 459.67
        }
        # Dictionary to store conversions from '°R' (Rankine) to other units
        R_conversions = {
            'K': unitvalue_1 / 1.8,
            '°C': (unitvalue_1 - 491.67) * 5/9,
            '°F': unitvalue_1 - 459.67,
            '°R': unitvalue_1
        }
        # Dictionary for unit conversion maps
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
    
        # Perform the conversion using the map
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

def get_currency_value(base_currency='USD', target_currencies=['bitcoin', 'BRL', 'EUR', 'JPY', 'GBP']):
    try:
        # URL to fetch the exchange rates
        url = 'https://www.exchangerate-api.com/v6/latest/USD'
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()
        
        # Extract the rates from the response
        rates = data.get('rates', {})
        
        # Initialize a dictionary to store the values
        values = {}
        
        for currency in target_currencies:
            if currency == 'bitcoin':
                # Fetch cryptocurrency values from CoinGecko or similar API
                btc_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
                btc_response = requests.get(btc_url)
                btc_response.raise_for_status()
                btc_data = btc_response.json()
                values['bitcoin'] = btc_data['bitcoin']['usd']
            else:
                # For fiat currencies
                value = rates.get(currency.upper(), 'Currency not found')
                values[currency] = value
                
        return values
    except Exception as e:
        print(f"Error fetching currency values: {str(e)}", flush=True)
        return None

def coin_conversion(coin1, coin2, coinvalue_1): 
    try:
        # Ensure coinvalue_1 is a valid number
        try:
            coinvalue_1 = float(coinvalue_1)
        except ValueError:
            return "Error: Invalid input for coin value. Please provide a valid number."
        
        # Fetch currency values
        currency_values = get_currency_value(base_currency='USD', target_currencies=[coin1, coin2])
        
        if not currency_values:
            return "Error: Currency values could not be fetched."
        
        # Check if coin1 and coin2 values are present
        if coin1 == 'bitcoin':
            coin1_value = currency_values.get('bitcoin')
        else:
            coin1_value = currency_values.get(coin1.upper())
        
        if coin2 == 'bitcoin':
            coin2_value = currency_values.get('bitcoin')
        else:
            coin2_value = currency_values.get(coin2.upper())
        
        if coin1_value is None or coin2_value is None:
            return "Error: One or both of the currencies are not available in the API response."
        
        # Convert coinvalue_1 from coin1 to USD, then from USD to coin2
        value_in_usd = coinvalue_1 / coin1_value
        converted_value = value_in_usd * coin2_value
        
        return round(converted_value, 2)
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
