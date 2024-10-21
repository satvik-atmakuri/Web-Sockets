import asyncio
from flask import Flask, render_template, jsonify
from websockets.sync.client import connect
import threading

app = Flask(__name__)

# Global variables for tracking progress and responses
progress = 0
total_requests = 10000
responses = []
all_responses = []  # Store all responses

def run_websocket_client():
    global progress, responses, all_responses
    progress = 0
    responses = []
    all_responses = []
    sample_limit = 20  # Show only first 20 messages in sample

    try:
        with connect("ws://localhost:8765") as websocket:
            for i in range(1, total_requests + 1):
                message = f"Request [{i}] Hello world!"
                websocket.send(message)
                response = websocket.recv()  # Receive modified message from server
                
                # Save sample responses
                if i <= sample_limit:
                    responses.append(response)
                
                # Store all responses
                all_responses.append(response)
                
                progress = i  # Update progress

    except Exception as e:
        responses.append(f"Error: {e}")
        all_responses.append(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_client')
def start_client():
    thread = threading.Thread(target=run_websocket_client)
    thread.start()
    return jsonify({"status": "started"})

@app.route('/progress')
def get_progress():
    return jsonify({"progress": progress, "total": total_requests, "responses": responses})

@app.route('/all_responses')
def get_all_responses():
    return jsonify({"all_responses": all_responses})

if __name__ == '__main__':
    app.run(debug=True)
