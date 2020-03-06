# html 읽어오기
def fileRead():
	f = open("input.txt", "r")
	htmlList = f.read().split('\n')
	f.close()
	
	return htmlList

# 변수화
def fileWrite(varName, htmlList):
	f = open("output.txt", "w")

	f.write('let ' + varName + ' = \'\';')
	f.write("\n")
	for html in htmlList:
		if html is not None:
			f.write(varName + ' +=\'' + html + '\';')
			f.write("\n")
	f.close()

def main():
	varName = 'html'
	htmlList = fileRead()
	fileWrite(varName, htmlList)

main()