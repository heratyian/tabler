import re
import sys

infile = sys.argv[1]
with open(infile) as f:
    content = f.readlines()


outfile = open(sys.argv[1] + ".html","wb")
	
for line in content:
	line = line.rstrip()
	if line.strip() == "=":
		outfile.write("<table border='1'>\n")
	elif line.strip() == "==":
		outfile.write("</table>\n")
	else:
		outfile.write("\t<tr>\n")
		cells = re.split(r'\t+',line)
		z = "\t\t"
		td_colspan = 0
		heading_colspan = 0
		for c in cells:
			for letter in c:
				if letter == "-":
					td_colspan = td_colspan + 1
				elif letter == "+":
					heading_colspan = heading_colspan + 1
				else:
					break
			if td_colspan > 1:
				z = z + "<td colspan=" + str(td_colspan) + ">" + c[td_colspan:] + "</td>"
			elif heading_colspan > 0:
				z = z + "<td colspan=" + str(heading_colspan) + "><h1>" + c[heading_colspan:] + "</h1></td>"
			else:
				z = z + "<td>" + c[td_colspan:] + "</td>"
			td_colspan = 0
			heading_colspan = 0
		outfile.write(z + "</tr>\n")
		
		