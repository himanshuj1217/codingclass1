mathMarks=float(input("Enter math marks: ")) 
scienceMarks=float(input("Enter science marks: "))
englishMarks=float(input("Enter english marks: "))
totalMarks=float(mathMarks+scienceMarks+englishMarks)
averageMarks=float((totalMarks)/3)
print((f"""
Math Scores : {mathMarks}
Science Scores : {scienceMarks}
English Scores : { englishMarks}
Total Scores : {totalMarks}
Average Scores: {averageMarks}
"""
))
