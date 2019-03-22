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
    COMMENTS = []
    with open('comments.txt', 'r') as f:
        for line in f:
            COMMENTS.append(line)

    return COMMENTS


def get_valid_breeds(Dog):
    BREED_CHOICES = []
    BREED_CHOICES.append((str(1), "Any"))
    with open("breeds.txt", "r") as f:
        counter = 1
        while True:
            line = f.readline().strip()
            if not line:
                break
            if Dog.objects.all().filter(breed=counter).count() != 0:
                BREED_CHOICES.append((str(counter), str(line)))
            counter += 1

    return BREED_CHOICES
