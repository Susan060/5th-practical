import string
import itertools
target_password = input("Enter the password you want to crack:")
def brute_force_password(target):
    chars = string.ascii_lowercase
    for length in range(1, len(target) + 1):
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            print(f"Trying: {guess}")
            if guess == target:
                return guess
    return None


cracked_password = brute_force_password(target_password)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password could not be cracked.")
