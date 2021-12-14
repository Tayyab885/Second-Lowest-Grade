if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    grades = sorted(list(set([x[1] for x in records]))) 
    #X[1] To get the second index values means grades

    lowest_grades = grades[1] 
    #grades[1] To get second lowest grade after sorting

    # print(grades)
    # print(lowest_grades)
    second_lowest = []
    for j in records: #To check by comparing with all others
        if lowest_grades == j[1]:
            #Checking the grades j[1] if they grades are equal appending the name which is on previous index j[0]
            second_lowest.append(j[0])
    
    second_lowest = sorted(second_lowest)
    for student in second_lowest:
        print(student)