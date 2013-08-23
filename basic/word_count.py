def read_file(filename):
	return open(filename).read().split()
def word_count(file):
	d={}
	for i in file:
		d[i]=d.get(i,0)+1
	return d
import sys
def main(fileiname):
	d=word_count(read_file(sys.argv[1]))
	for x in sorted(d.keys(),key=lambda x:d[x],reverse=True):
		print x
if __name__ == '__main__':
	 main(sys.argv[1])

