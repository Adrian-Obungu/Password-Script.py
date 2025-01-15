import itertools 
def generate_passwords(file_path, chunk_size=1000000):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    total_passwords = 36**6 # Total possible combinations 
    count = 0
    with open(file_path, "w") as f: 
        # Generate combinations in batches 
        for password_batch in itertools.islice(itertools.product(characters, repeat=6), total_passwords ): 
            f.write(''.join(password_batch) + '\n') 
            count += 1 
            # Print progress after each chunk 
            if count % chunk_size == 0: 
                print(f"Generated and written {count} passwords so far...") 
    print(f"Password generation complete. Total passwords: {count}") 
# Run the function 
generate_passwords("password_list.txt")
