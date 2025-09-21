from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    news_text = data.get('text', '')
    if not news_text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Vectorize input text
    vect_text = vectorizer.transform([news_text])
    
    # Predict label
    pred = model.predict(vect_text)[0]
    
    # Map label to text
    label_map = {0: 'Real', 1: 'Fake'}
    prediction = label_map.get(pred, 'Unknown')
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
