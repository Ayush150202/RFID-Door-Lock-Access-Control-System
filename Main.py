import time

# Mock RFID reader module
class RFIDReader:
    def read_card(self):
        # Simulate reading an RFID card
        return "12345ABCD"  # Mock card ID

# Mock access control
class AccessControl:
    def __init__(self):
        # Predefined authorized cards
        self.authorized_cards = {"12345ABCD": "User1", "67890EFGH": "User2"}

    def is_authorized(self, card_id):
        return card_id in self.authorized_cards

    def get_user(self, card_id):
        return self.authorized_cards.get(card_id, "Unknown")

# Main program
def main():
    reader = RFIDReader()
    access_control = AccessControl()
    print("RFID Door Lock System Initialized. Waiting for card...")

    try:
        while True:
            card_id = reader.read_card()
            if card_id:
                print(f"Card detected: {card_id}")
                if access_control.is_authorized(card_id):
                    user = access_control.get_user(card_id)
                    print(f"Access granted. Welcome, {user}!")
                else:
                    print("Access denied. Unauthorized card.")
            time.sleep(2)  # Simulate delay
    except KeyboardInterrupt:
        print("System shutting down.")

if __name__ == "__main__":
    main()
