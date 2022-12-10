import os
import re

#[xmin, ymin, xmax, ymax]
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return round(x, 6), round(y, 6), round(w, 6), round(h, 6)

#labels directory "XML file location"
path = "C:/Users/THOTA/Documents/helmetDataset/annotations/"
files = os.listdir(path)
for file in files:
	with open(path + "{}".format(file), 'r+') as f:
		content = f.read()
		name = file.split(".")[0]
		#desired location to save .txt file
		txt = open('C:/Users/THOTA/Documents/helmetDataset/labels/' + '{}.txt'.format(name), 'w')
		if "<width>" in content:
			size = []
			box = []
			labels=[]
			content = content.split("\n")
			for indx, val in enumerate(content):
				if "<width>" in val:
					width = re.findall("[0-9]", val)
					width = "".join(width)
					size.append(width)
				elif "<height>" in val:
					height = re.findall("[0-9]", val)
					height = "".join(height)
					size.append(height)
				elif "<xmin>" in val:
					xmin = re.findall("[0-9]", val)
					xmin = "".join(xmin)
					box.append(xmin)
				elif "<ymin>" in val:
					ymin = re.findall("[0-9]", val)
					ymin = "".join(ymin)
					box.append(ymin)
				elif "<xmax>" in val:
					xmax = re.findall("[0-9]", val)
					xmax = "".join(xmax)
					box.append(xmax)
				elif "<ymax>" in val:
					ymax = re.findall("[0-9]", val)
					ymax = "".join(ymax)
					box.append(ymax)
				elif "<name>" in val:
					lab = re.findall("[a-zA-Z]", val)
					lab="".join(lab)[4:-4]
					labels.append(lab)

				else:
					pass
			#print(size)
			#print(box)
			box = [int(i) for i in box]
			size = [int(i) for i in size]
			num = 0
			j=0
			print(labels)
			for i in range(0, len(box)):
				if num < i:
					num = num+4
					val = box[num-4:num]
					val1, val2, val3, val4 = convert(size, val)
					print(val1, val2, val3, val4)
					if labels[j]=='WithoutHelmet':
						txt.write("1" + " "+ str(val1) + " "+ str(val2) + " "+ str(val3) + " "+ str(val4) + "\n")
					else:
						txt.write("0" + " "+ str(val1) + " "+ str(val2) + " "+ str(val3) + " "+ str(val4) + "\n")
					j+=1
		else:	
			print("No content in file for annotation.")
	