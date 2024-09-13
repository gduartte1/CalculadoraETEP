function performCalculation() {
    const number_1 = document.getElementById('number_1').value;
    const operation = document.getElementById('operation').value;
    const number_2 = document.getElementById('number_2').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            number_1: number_1,
            operation: operation,
            number_2: number_2,
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `${number_1} ${operation} ${number_2} = ${data.result}`;
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: Invalid input';
    });
}
document.getElementById("icon_unit").addEventListener("click", function() {
        const calculator = document.getElementById("calculator");
        const unitConversor = document.getElementById("unit-conversor")
        const coinConversor = document.getElementById("coin-conversor")
        const unitIcon = document.getElementById("icon_unit")
        const coinIcon = document.getElementById("icon_coin")
        const calcIcon = document.getElementById("icon_calc")
        unitIcon.style.border = "3px solid #000000";
        coinIcon.style.border = "0px solid #000000";
        calcIcon.style.border = "0px solid #000000";
        if (unitConversor.style.display == "block") {
            calculator.style.display = "none"
            coinConversor.style.display = "none"
        } else {    
            unitConversor.style.display = "block";
            calculator.style.display = "none"
            coinConversor.style.display = "none";
        };
})
document.getElementById("icon_calc").addEventListener("click", function() {
    const calculator = document.getElementById("calculator");
    const unitConversor = document.getElementById("unit-conversor")
    const coinConversor = document.getElementById("coin-conversor")
    const unitIcon = document.getElementById("icon_unit")
    const coinIcon = document.getElementById("icon_coin")
    const calcIcon = document.getElementById("icon_calc")
    unitIcon.style.border = "0px solid #000000";
    coinIcon.style.border = "0px solid #000000";
    calcIcon.style.border = "3px solid #000000";
    if (calculator.style.display == "block") {
        unitConversor.style.display = "none"
        coinConversor.style.display = "none"
    } else {    
        calculator.style.display = "block";
        unitConversor.style.display = "none"
        coinConversor.style.display = "none";
    };
})
document.getElementById("icon_coin").addEventListener("click", function() {
    const calculator = document.getElementById("calculator");
    const unitConversor = document.getElementById("unit-conversor")
    const coinConversor = document.getElementById("coin-conversor")
    const unitIcon = document.getElementById("icon_unit")
    const coinIcon = document.getElementById("icon_coin")
    const calcIcon = document.getElementById("icon_calc")
    unitIcon.style.border = "0px solid #000000";
    coinIcon.style.border = "3px solid #000000";
    calcIcon.style.border = "0px solid #000000";
    if (coinConversor.style.display == "block") {
        unitConversor.style.display = "none"
        calculator.style.display = "none"
    } else {    
        coinConversor.style.display = "block";
        unitConversor.style.display = "none"
        calculator.style.display = "none";
    };
})

function UnitConversion() {
    const unit1 = document.getElementById('unit1').value;
    const unit2 = document.getElementById('unit2').value;
    const unitvalue_1 = document.getElementById('unitvalue_1').value;

    fetch('/unitConversion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            unit1: unit1,
            unit2: unit2,
            unitvalue_1: unitvalue_1,
        }),
    })
    .then(response => response.json())  
    .then(data => {
        console.log(data)
        document.getElementById('unitResult').innerText = `${unitvalue_1}${unit1} é o equivalente à ${data.unitResult}${unit2}`;
    })
    .catch(error => {
        document.getElementById('unitResult').innerText = 'Error: Invalid input';
    });
}

document.getElementById('conversionType').addEventListener('change', function() {
    const conversionType = this.value;
    const unit1 = document.getElementById('unit1');
    const unit2 = document.getElementById('unit2');
    
    // Clear the existing options in the second select
    unit1.innerHTML = '';
    unit2.innerHTML = '';
    
    // Define options based on the selected value of the first select
    let unit1options = [];
    let unit2options = [];
    if (conversionType == 'peso') {
        unit1options = [
            { value: 'g', text: 'g (grama)' },
            { value: 'kg', text: 'kg (kilograma)' },
            { value: 'ton', text: 'ton (tonelada)' },
            { value: 'lbs', text: 'lbs (Libras)' },
            { value: 'oz', text: 'oz (Onças)' }
        ];
        unit2options = [
            { value: 'g', text: 'g (grama)' },
            { value: 'kg', text: 'kg (kilograma)' },
            { value: 'ton', text: 'ton (tonelada)' },
            { value: 'lbs', text: 'lbs (Libras)' },
            { value: 'oz', text: 'oz (Onças)' }
        ];
    } else if (conversionType == 'velocidade') {
        unit1options = [
            { value: 'm/s', text: 'm/s (Metros por Segundo)' },
            { value: 'km/h', text: 'km/h (Kilometro por Hora)' },
            { value: 'mi/s', text: 'mi/s (Milhas por Segundo)' },
            { value: 'mi/h', text: 'mi/h (Milhas por Hora)' },
            { value: 'ft/s', text: 'ft/s (Pés por segundo)' },
            { value: 'ft/h', text: 'ft/h (Pés por Hora)' },
            { value: 'yd/s', text: 'yd/s (Jardas por segundo)' },
            { value: 'yd/h', text: 'yd/h (Jardas por Hora)' }
        ];
        unit2options = [
            { value: 'm/s', text: 'm/s (Metros por Segundo)' },
            { value: 'km/h', text: 'km/h (Kilometro por Hora)' },
            { value: 'mi/s', text: 'mi/s (Milhas por Segundo)' },
            { value: 'mi/h', text: 'mi/h (Milhas por Hora)' },
            { value: 'ft/s', text: 'ft/s (Pés por segundo)' },
            { value: 'ft/h', text: 'ft/h (Pés por Hora)' },
            { value: 'yd/s', text: 'yd/s (Jardas por segundo)' },
            { value: 'yd/h', text: 'yd/h (Jardas por Hora)' }
        ];
    } else if (conversionType == 'volume') {
        unit1options = [
            { value: 'mL', text: 'mL (Mililitro)' },
            { value: 'L', text: 'L (Litro)' },
            { value: 'm³', text: 'm³ (Metro cúbico)' },
            { value: 'km³', text: 'km³ (Kilometro cúbico)' },
            { value: 'cm³', text: 'cm³ (Centímetro cúbico)' },
            { value: 'gal', text: 'gal (Galão - EUA)' }
        ];
        unit2options = [
            { value: 'mL', text: 'mL (Mililitro)' },
            { value: 'L', text: 'L (Litro)' },
            { value: 'm³', text: 'm³ (Metro cúbico)' },
            { value: 'km³', text: 'km³ (Kilometro cúbico)' },
            { value: 'cm³', text: 'cm³ (Centímetro cúbico)' },
            { value: 'gal', text: 'gal (Galão - EUA)' }
        ];
    } else if (conversionType == 'area') {
        unit1options = [
            { value: 'cm²', text: 'cm² (Centímetro Quadrado)' },
            { value: 'm²', text: 'm² (Metro Quadrado)' },
            { value: 'km²', text: 'km² (Kilometro Quadrado)' },
            { value: 'ha', text: 'ha (Hectare)' },
            { value: 'ac', text: 'ac (Acre)' }
        ];
        unit2options = [
            { value: 'cm²', text: 'cm² (Centímetro Quadrado)' },
            { value: 'm²', text: 'm² (Metro Quadrado)' },
            { value: 'km²', text: 'km² (Kilometro Quadrado)' },
            { value: 'ha', text: 'ha (Hectare)' },
            { value: 'ac', text: 'ac (Acre)' }
        ];
    } else if (conversionType == 'distancia') {
        unit1options = [
            { value: 'cm', text: 'cm (Centímetro)' },
            { value: 'm', text: 'm (Metro)' },
            { value: 'km', text: 'km (Kilometro)' },
            { value: 'yd', text: 'ys (Jarda)' },
            { value: 'ft', text: 'ft (Pés)' },
            { value: 'in', text: 'in (Polegadas)' }
        ];
        unit2options = [
            { value: 'cm', text: 'cm (Centímetro)' },
            { value: 'm', text: 'm (Metro)' },
            { value: 'km', text: 'km (Kilometro)' },
            { value: 'yd', text: 'ys (Jarda)' },
            { value: 'ft', text: 'ft (Pés)' },
            { value: 'in', text: 'in (Polegadas)' }
        ];
    }
    else if (conversionType == 'temperatura') {
        unit1options = [
            { value: 'K', text: 'K (Kelvin)' },
            { value: '°C', text: '°C (Celsius)' },
            { value: '°F', text: '°F (Fahrenheit)' },
            { value: '°R', text: '°R (Rankine)' }
        ];
        unit2options = [
            { value: 'K', text: 'K (Kelvin)' },
            { value: '°C', text: '°C (Celsius)' },
            { value: '°F', text: '°F (Fahrenheit)' },
            { value: '°R', text: '°R (Rankine)' }
        ];
    }
    

    // Populate the second select with new options
    unit1options.forEach(option  => {
        const newOption1 = document.createElement('option');
        newOption1.value = option.value;
        newOption1.text = option.text;
        unit1.appendChild(newOption1);
    });
    unit2options.forEach(option  => {
        const newOption2 = document.createElement('option');
        newOption2.value = option.value;
        newOption2.text = option.text;
        unit2.appendChild(newOption2);
    });
});

function coinConvertion() {
    const coin1 = document.getElementById('coin1').value;
    const coinvalue_1 = document.getElementById('coinvalue_1').value;
    const coin2 = document.getElementById('coin2').value;

    fetch('/coin_conversion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            coin1: coin1,
            coinvalue_1: coinvalue_1,
            coin2: coin2,
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('coinResult').innerText = `${coinvalue_1}${coin1} é o equivalente à ${data.coinResult}${coin2}`;
    })
    .catch(error => {
        document.getElementById('coinResult').innerText = 'Error: Invalid input';
    });
}