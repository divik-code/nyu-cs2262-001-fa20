from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

# Define the route for the '/register' endpoint
@app.route('/register', methods=['PUT'])
def register():
    # Get JSON payload from request body
    json_data = request.get_json()
    host_name = json_data['hostname']
    ip = json_data['ip']
    as_ip = json_data['as_ip']
    as_port = json_data['as_port']

    # Construct registeration message in DNS-like format
    message = f"TYPE=A\nNAME={host_name}\nVALUE={ip}\nTTL=10\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send registeration message to AS
    sock.sendto(message.encode(), (as_ip, int(as_port)))

    return jsonify({'message': 'Hostname registered!'}), 201

# Define a route to calculate fibonacci number
@app.route('/fibonacci')
def fibonacci():
    num = request.args.get('number')
    if not num.isdigit() or int(num) < 0:
        return jsonify({'error': 'Bad input'}), 400
    
    fib_value = calculate_fibonacci(int(num))
    return jsonify({'Your fibonacci number': fib_value}), 200

# Recursive function to calculate Fibonacci number
def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

if __name__ == '__main__':
    app.run(port=9090)