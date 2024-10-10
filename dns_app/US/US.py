from flask import Flask, request, jsonify
import requests
import socket

app = Flask(__name__)

# Define the route for the '/fibonacci' endpoint
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    try:
        # Extract query parameters from the request URL
        host_name = request.args.get('hostname')
        fs_port = request.args.get('fs_port')
        number = request.args.get('number')
        as_ip = request.args.get('as_ip')
        as_port = request.args.get('as_port')

        # Check if any required parameters are missing
        if not host_name or not fs_port or not number or not as_ip or not as_port:
            return jsonify({'error': 'Bad Request'}), 400

        # Construct query message to send to the AS fro DNS resolution
        query = f'TYPE=A\nNAME={host_name}\n'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send DNS request to AS
        sock.sendto(query.encode(), (as_ip, int(as_port)))

        # Response from AS containing ip address of hostname
        data, _ = sock.recvfrom(2048)
        # Extract ip address
        ip_address = data.decode().split('\n')[2].split('=')[1].strip()

        # Call fibonacci service
        response = requests.get(f'http://{ip_address}:{fs_port}/fibonacci?number={number}')
        return response.text, 200

    except Exception as e:
        # Return 500 if any error occurs
        return jsonify({'Error occurred! Status code is ': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080)