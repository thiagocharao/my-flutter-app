import random
from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the GET request
@app.route('/api/data', methods=['GET'])
def get_data():
    # Return a mock JSON response with a random ID and message
    return jsonify({
        'id': str(random.randint(0, 100)),
        'message': 'Hello World: ' + str(random.randint(0, 100))
    })
    
# Run the server only if this file is run directly
if __name__ == '__main__':
    #app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'), debug=True)
    app.run(debug=True)
