from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace "Your Full Name" with your actual name.
    full_name = "Raunak"
    
    # Get the system username
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    # Get the current server time in IST
    ist_timezone = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the top command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode("utf-8")
    except Exception as e:
        top_output = f"Could not fetch top output: {str(e)}"
    
    # Format the output as HTML
    html_output = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> Raunak Parmar</p>
            <p><strong>Username:</strong> {system_username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return html_output

if __name__ == "__main__":
    # Run the app on public port 8080
    app.run(host="0.0.0.0", port=8080)
