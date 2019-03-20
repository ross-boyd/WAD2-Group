def get_breeds():
    BREED_CHOICES = []
    with open("breeds.txt", "r") as f:
        counter = 1
        while True:
            line = f.readline().strip()
            if not line:
                break

            BREED_CHOICES.append((str(counter), str(line)))
            counter += 1
    return BREED_CHOICES

