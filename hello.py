wtf = input("What's your Name")
score = input("Enter Score: ")
y = float(score)
mrf = input("What was total score")
m = float(mrf)
x = y / m 
v = x * 100
if x >= 0.9 : 
    print('A')
elif x >= 0.8 :
    print('B')
elif x >= 0.7 :
    print("C")
elif x >= 0.6 :
    print('D')
elif x < 0.6 :
    print('F')
else :
    print('Error')
print("Percentage" , v )
print("Thank you" , wtf )
#thanks for using this will update soon for fraction values
#PrasunPragya
