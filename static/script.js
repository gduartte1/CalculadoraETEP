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
