def check_result(sub1, sub2, sub3):
    # Calculate performance metrics
    total = sub1 + sub2 + sub3
    average = total / 3
    pass_criterion = 50

    # Display calculated outputs
    print(f"Subject Marks: {sub1}, {sub2}, {sub3}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")

    # Evaluate criteria
    if average >= pass_criterion:
        print("Status: PASS")
    else:
        print("Status: FAIL")


if __name__ == "__main__":
    # Test with sample marks
    check_result(78, 85, 62)