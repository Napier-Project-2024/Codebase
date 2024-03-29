document.addEventListener("DOMContentLoaded", function() {
    // Fetch data from the API
    fetch('http://192.168.1.224:5000/returnVals')
    .then(response => response.json())
    .then(data => {
        // Display the values
        displayValues(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});

function displayValues(data) {
    const container = document.getElementById('values-container');

    // Iterate through the values and create elements to display them
    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            const value = data[key];
            const valueElement = document.createElement('div');
            valueElement.textContent = `${key}: ${value}`;
            container.appendChild(valueElement);
        }
    }
}
