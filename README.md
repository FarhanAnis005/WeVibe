# Fun Vibration App

This is a fun application built using FastAPI, WebSockets, and ngrok. The app allows an admin to control a slider, and the client’s phone will vibrate according to the slider value. The app is hosted using ngrok for easy public access.

## Features
- Real-time slider control using WebSockets.
- Client-side phone vibration based on the slider value.
- Easy deployment using ngrok.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/FarhanAnis005/WeVibe.git
    cd WeVibe
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your ngrok authentication token:
    ```sh
    NGROK_AUTH_TOKEN=your-ngrok-auth-token
    ```

## Running the App

1. Start the FastAPI server:
    ```sh
    python main.py
    ```

2. Once the server is running, ngrok will provide a public URL. This URL will be printed in the terminal.

3. Open your browser and navigate to:
    - Admin page: `<public_url>/admin`
    - Client page: `<public_url>/`
  
## Enjoy pranking your friends
