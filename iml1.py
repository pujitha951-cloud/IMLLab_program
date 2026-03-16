import csv

def finds_algorithm(data):
    hypothesis = ['0'] * (len(data[0]) - 1)

    for example in data:
        attributes, label = example[:-1], example[-1]
        if label.lower() == 'yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = attributes[i]
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = '?'
    return hypothesis

def load_csv(filename):
    """Load dataset from a CSV file"""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# 🔹 Usage
filename = "EjoySport(2).csv"   # replace with your CSV file name
dataset = load_csv(filename)

final_hypothesis = finds_algorithm(dataset)

print("Training Data:")
for row in dataset:
    print(row)

print("\nFinal Hypothesis:", final_hypothesis)
