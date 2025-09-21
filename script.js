function predictNews() {
    const newsText = document.getElementById('newsText').value;

    fetch('http://localhost:5000/predict', {  // Make sure this matches your Flask URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: newsText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = "Prediction: " + data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('predictionResult').innerText = "Error making prediction.";
    });
}
