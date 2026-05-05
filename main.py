import random
import time
import sys

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def detect_critical_issue(user_input):
    # Keywords for EV-specific emergencies
    trigger_words = [
        "broken", "stranded", "fire", "shock", "stuck", 
        "manager", "emergency", "not charging", "error"
    ]
    return any(word in user_input.lower() for word in trigger_words)

def start_chat():
    print("🚗 VoltMate: AI EV Charging Support (Type 'quit' to exit)")
    print("─" * 50)
    print("Bot: Hello! I am VoltMate. I can help you find stations,")
    print("      check pricing, or troubleshoot charging issues.")
    print("─" * 50)

    while True:
        user_input = input("👤 Driver: ")

        if user_input.lower() == 'quit':
            print("\n🚗 Bot: Safe travels! Goodbye.")
            break

        # Simulate thinking
        print("🚗 Bot scanning station data...", end="\r")
        time.sleep(0.5)
        print(" " * 30, end="\r")

        if detect_critical_issue(user_input):
            # ESCALATION LOGIC FOR EV ISSUES
            print("\n" + "┌" + "─" * 38 + "┐")
            print("│ 🔴 CRITICAL ISSUE DETECTED           │")
            print("└" + "─" * 38 + "┘")
            type_text("Bot: This sounds serious. I am alerting our engineering team.")
            print("┌" + "─" * 38 + "┐")
            print("│ 🎫 TICKET #EV-2026-99               │")
            print("│ STATUS: HUMAN ENGINEER ASSIGNED     │")
            print("│ LOCATION: Nearest Service Team      │")
            print("└" + "─" * 38 + "┘")
            break
        else:
            # NORMAL EV QUERIES
            responses = [
                "The nearest station is 2 miles away. 3 plugs available.",
                "Pricing is $0.35 per kWh. Happy charging!",
                "Make sure your charging cable is firmly clicked into place.",
                "Your session has started. Charging at 150kW."
            ]
            print(f"🚗 Bot: {random.choice(responses)}")
            print("─" * 50)

if __name__ == "__main__":
    start_chat()
