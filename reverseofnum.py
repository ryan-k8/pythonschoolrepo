"""Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401."""

#---------my solution ----------------------
def reverse_number(number:int) -> int:
	num_lst = list(str(number))
	num_lst.reverse()
	out =''
	flag = False
	for j in num_lst:
		if (int(j) != 0):
			flag = True
		if flag:
			out += j
	print(out)

	#----- like this also----------
	rev_num_str = "".join(num_lst)
	return int(rev_num_str)


	#------------------------------

reverse_number(int(input()))




#-----------gfg solution (algorithm based - 0(Log(N))))-------------
def reverse(n :int) -> None:
	revNum = 0
	while n > 0:
		revNum = revNum*10 + n%10
		n = n//10
	print(revNum)

reverse(int(input()))






#------------gfg solution (string based) ---------------------
def reversDigits(num):
 
    # converting number to string
    string = str(num)
 
    # reversing the string
    string = list(string)
    string.reverse()
    string = ''.join(string)
 
    # converting string to integer
    num = int(string)
 
    # returning integer
    return num
 
# Driver code
if __name__ == "__main__":
 
    num = 10400
    print("Reverse of no. is ", reversDigits(num))