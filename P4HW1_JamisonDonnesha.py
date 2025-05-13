#Donnesha Jamison
#04/30/25
#Looping



def collect_scores():
    
    number_of_scores = int(input("How many scores would you like to enter? "))
    scores = []  

    
    for i in range(number_of_scores):
        while True:  
            try:
                score = float(input(f"Enter score {i + 1} (between 0 and 100): "))
                if 0 <= score <= 100:  
                    scores.append(score)  
                    break  
                else:
                    print("Invalid score. Please enter a score between 0 and 100.")  
            except ValueError:
                print("Please enter a valid number.")

    return scores  

def calculate_statistics(grades):
    
    min_grade = min(grades)
    max_grade = max(grades)
    sum_of_grades = sum(grades)
    average = sum_of_grades / len(grades)

    
    print("------ Results -------")
    print(f"Lowest grade: {min_grade}")
    print(f"Highest grade: {max_grade}")
    print(f"Sum of grades: {sum_of_grades}")
    print(f"Average: {average:.2f}")

def main():
    scores = collect_scores()  
    calculate_statistics(scores)  


main()
