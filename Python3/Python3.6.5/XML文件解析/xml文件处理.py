#!/usr/bin/python3
#coding:utf-8

from xml.dom.minidom import parse
import xml.dom.minidom
Root = xml.dom.minidom.parse('开机提醒.xml')
# print(dir(DOMTree))
task = Root.documentElement
# print(dir())
for line in task.childNodes:
	# print('line.nodeName:',line.nodeName,'line.nodeType:',line.nodeType,'line.nodeValue:',line.nodeValue,'line.normalize:',line.normalize)
	# print(len(line))
	# print(line)
	if 3 == line.nodeType:
		continue
	if 'Actions' == line.nodeName:

		for tmp in line.childNodes:
			# print(tmp)
			if 3 == tmp.nodeType:
				continue
			# print(tmp)
			for tmp1 in tmp.childNodes:
				if 3 == tmp1.nodeType:
					continue	 
				for tmp2 in tmp1.childNodes:
					# print(tmp2)
					# if 3 == tmp2.nodeType:
					# 	continue
					print(tmp2.nodeValue)
	# for line1 in line.childNodes:
	# 	if 3 == line1.nodeType:
	# 		continue
	# 	# print(line1.nodeName)
	# 	# print(dir(line1))

	# 	for line2 in line1.childNodes:
	# 		if 3 == line2.nodeType:
	# 			continue
			# print(line2.nodeValue)
			# print(line2.data)