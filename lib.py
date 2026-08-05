def total_books(shelves):
    return sum(shelves)

def average_books(shelves):
    return sum(shelves) / len(shelves)

def max_shelf(shelves):
    return max(shelves)

if __name__ == "__main__":
    shelves = [12, 8, 15]
    print("Total:", total_books(shelves))