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


def get_names():
    NAME_CHOICES = []
    with open("names.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            NAME_CHOICES.append(str(line))
    return NAME_CHOICES


def get_comments():
    with open('comments.txt', 'r') as f:
        comments = []
        for line in f:
            comments.append(line)
        
    return comments
        