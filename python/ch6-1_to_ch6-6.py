# gugu.py
def gugu(n):
    result=[]
    i=1
    while i<10:
        result.append(n*i)
        i+=1
    return result
print(gugu(2))

# add_multiple.py
result=0
for n in range(1, 100):
    if n%3==0 or n%5==0:
        result += n
print(result)

# paging.py
def get_total_page(m, n):
    if m%n==0:
        return m//n
    else:
        return m//n+1

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(30, 10))

# sub_dir_search.py
import os

def search(dirname):
	try:
		filenames=os.listdir(dirname)
		for filename in filenames:
			full_filename=os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
				search(full_filename)
			else:
				ext=os.path.splitext(full_filename)[-1]
				if ext=='.py':
					print(full_filename)
	except PermissionError:
		pass
search("c:\doit")

# oswalk.py
import os

for (path, dir, files) in os.walk("c:\doit"):
	for filename in files:
		ext=os.path.splitext(filename)[-1]
		if ext=='.py':
			print("%s/%s" %(path, filename))