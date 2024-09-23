import time

def main():
    start_time = None
    elapsed_time = 0
    is_running = False
    is_on_break = False

    while True:
        command = input("Enter a command (start, break, stop, quit): ").strip().lower()

        if command == "start":
            if not is_running:
                start_time = time.time() - elapsed_time  # Resume from where left off if paused
                is_running = True
                is_on_break = False
                print("Study session started.")
            else:
                print("Session is already running.")

        elif command == "break":
            if is_running and not is_on_break:
                elapsed_time = time.time() - start_time  # Store the time elapsed before break
                is_running = False
                is_on_break = True
                print(f"You are on a break. You studied for {round(elapsed_time, 2)} seconds so far.")
            elif is_on_break:
                print("You are already on a break.")
            else:
                print("You need to start a session first.")

        elif command == "stop":
            if is_running or is_on_break:
                if is_running:
                    elapsed_time = time.time() - start_time
                print(f"Session stopped! You studied for {round(elapsed_time, 2)} seconds.")
                is_running = False
                is_on_break = False
                elapsed_time = 0  # Reset timer
                start_time = None
            else:
                print("No session is running.")

        elif command == "quit":
            if is_running or is_on_break:
                print(f"Exiting. Total study time was {round(elapsed_time, 2)} seconds.")
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please enter 'start', 'break', 'stop', or 'quit'.")

if __name__ == "__main__":
    main()