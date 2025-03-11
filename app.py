from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your Full Name
    full_name = "suryanshi thappa"  # Replace with your actual name

    # System Username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Return formatted response
    return f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
