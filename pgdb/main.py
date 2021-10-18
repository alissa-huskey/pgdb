import importlib

def main():
    """CLI"""
    drivers = ("pg8000", "postgresql", "psycopg")

    while True:

        print("Choose a driver.\n")
        for i, driver in enumerate(drivers, 1):
            print(f"{i}. {driver}")
        print()

        while True:
            reply = input("> ").strip().lower()

            if reply == "q":
                quit()
            elif reply in drivers or \
                (reply.isnumeric() and int(reply) and int(reply) <= len(drivers)):
                break
            else:
                print("Please choose a valid driver.\n")

        if reply.isnumeric():
            reply = drivers[int(reply)-1]

        mod = importlib.import_module(f"db_{reply}", package="pgdb")
        print(f"\nUsing the {reply} driver.\n")
        mod.main()
        print()
        reply = input("Continue? [Y/n] ").strip().lower()
        if reply in ("n", "no", "q", "quit"):
            break
        else:
            print()

if __name__ == "__main__":
    main()
