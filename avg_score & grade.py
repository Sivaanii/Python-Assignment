def grades(avg_score):
    if avg_score>=90:
        return "A"
    elif avg_score>=80:
        return "B"
    elif avg_score>=60:
        return "C"
    elif avg_score>=50:
        return "D"
    elif avg_score>=30:
        return "E"
    else:
        return "F"

def main():
    name=input("enter the student's name:")
    subjects={}

    for i in range(int(input("enter the number of subjects:"))):
      subject=input("enter the subject:")
      score=float(input(f"enter the score of {subject}:"))
      subjects[subject]=score

    avg_score=sum(subjects.values())/len(subjects)
    grade=grades(avg_score)

    print(f"\nstudent:{name}")
    print("scores:",subjects)
    print(f"average score:{avg_score:.2f}")
    print(f"grade:{grade}")

main()
    
