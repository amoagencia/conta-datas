from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/merz', methods=['POST'])
def merz():
    """

    Returns:
        A JSON response containing the calculated difference.
    """
    # Data alvo
    target_date = datetime(2024, 1, 16, 8, 2, 0)
    # Data atual
    current_date = datetime.now()
    # Calcula a diferença
    difference = target_date - current_date
    # Formata a diferença em dias, horas, minutos e segundos
    days, seconds = difference.days, difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    response_text = f"A diferença entre a data de hoje e 2024-01-16T08:02:00 é de {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos."
    
    return jsonify({
        "response_type": "in_channel",
        "text": response_text
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
