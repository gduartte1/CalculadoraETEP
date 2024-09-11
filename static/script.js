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
