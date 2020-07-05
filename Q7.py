count=int(0)
friends_list=[("Harry","Porter","none"),("Paul","Christian","none"),("Peter","Hooks","none")]
for a,b,c in friends_list:
	if c=="none":
		count=count+1
	else:
		pass
size=(len(friends_list)-count)
