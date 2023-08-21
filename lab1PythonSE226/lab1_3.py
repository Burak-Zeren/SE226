txt=input("Please enter your name: ")
labGrade=input("Enter your lab grade: ")
midtermGrade=input("Enter your midterm grade: ")
finalGrade=input("Enter your final grade: ")
labGrade=int(labGrade)/4
midtermGrade=int(midtermGrade)*35/100
finalGrade=int(finalGrade)*4/10
lastScore=(labGrade+midtermGrade+finalGrade)/3
lastScore=round(lastScore,1)
print(f"Name: {txt}")
print(f"Lab: {labGrade}")
print(f"Midterm: {midtermGrade}")
print(f"Final: {finalGrade}")
print(f"Last Score: {lastScore}")
