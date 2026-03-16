import csv

def load_dataset(filename):
    dataset = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            attributes = row[:-1]
            label = row[-1].strip().lower()
            dataset.append((attributes, label))
    return dataset


def find_s(dataset):
    hypothesis = None

    for attributes, label in dataset:
        if label == "yes":
            if hypothesis is None:
                hypothesis = attributes.copy()
            else:
                for i in range(len(hypothesis)):
                    if hypothesis[i] != attributes[i]:
                        hypothesis[i] = "?"
    return hypothesis


# MAIN PROGRAM
if __name__ == "__main__":
    data = load_dataset("enjoyy.csv")

    print("\n--- ENJOYSPORT DATASET ---")
    for attributes, label in data:
        print(attributes, "=>", label)

    hypothesis = find_s(data)

    print("\n--- FINAL HYPOTHESIS (Find-S) ---")
    print(hypothesis)
