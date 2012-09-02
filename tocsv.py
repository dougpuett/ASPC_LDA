import os

raw = open(os.getcwd() + "/model-final.theta").read()
rawrows = raw.split("\n")
output = ""
for row in rawrows:
	row  = row.replace(" ", ",")
	output += row[:-1] + "\n"

output1 = open(os.getcwd() + "/lda.csv", "w")

output1.write(output)

output1.close()