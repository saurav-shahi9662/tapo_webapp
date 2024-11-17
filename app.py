from flask import Flask, jsonify, request
from tapo import ApiClient
import os
import asyncio

app = Flask(__name__)

# Replace with your Tapo credentials and bulb IP
TAPO_USERNAME = "nepalicool46@gmail.com"
TAPO_PASSWORD = "Saurav@123"
DEVICE_IP = "192.168.1.105"

# Initialize the Tapo client
client = ApiClient(TAPO_USERNAME, TAPO_PASSWORD)

# Define a route to turn the light on (asynchronous)
@app.route('/turn_on', methods=['POST'])
async def turn_on():
    try:
        # Connect to the bulb and turn it on
        device = await client.l535(DEVICE_IP)  # Ensure to await the coroutine here
        await device.on()  # Await the asynchronous .on() method
        return jsonify({"status": "success", "message": "Light turned on"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Define a route to turn the light off (asynchronous)
@app.route('/turn_off', methods=['POST'])
async def turn_off():
    try:
        # Connect to the bulb and turn it off
        device = await client.l535(DEVICE_IP)  # Ensure to await the coroutine here
        await device.off()  # Await the asynchronous .off() method
        return jsonify({"status": "success", "message": "Light turned off"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
