# core/obs_controller.py
import obsws_python as obs

class OBSController:
    def __init__(self, host='localhost', port=4455, password=''):
        self.ws_client = obs.obsws(host=host, port=port, password=password)
        self.connected = False

    def connect(self):
        try:
            self.ws_client.connect()
            self.connected = True
            print("Successfully connected to OBS!")
        except Exception as e:
            print(f"Error connecting to OBS: {e}")
            self.connected = False

    def disconnect(self):
        if self.connected:
            self.ws_client.disconnect()
            self.connected = False
            print("Disconnected from OBS.")

    # ... (Future functions for scene switching, source control will go here) ...

if __name__ == '__main__':
    # Example usage for testing connection
    obs_controller = OBSController()
    obs_controller.connect()

    if obs_controller.connected:
        # Do something once connected (for now, just wait and disconnect)
        input("Press Enter to disconnect...")
        obs_controller.disconnect()
    else:
        print("Failed to connect. Check OBS Websocket settings and script.")
