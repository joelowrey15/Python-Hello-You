"""
This program ask a user for their name and says "Hello, name!"
Joseph Lowrey - September 2025
"""

# This is a single line comment
def main() -> None:
    name: str="Joseph"
    print("Hello,", name,"!")
    print("Hello, "+ name + "!")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()