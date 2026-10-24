import subprocess

pname='VanessaTriangle.py'
# Define multiple sets of 3 integers
test_sets = [(3, 4, 5), (3, 0, 0), (3, 8, 3), (6, 7, 8), (2, 7, -5)]

for i, (a, b, c) in enumerate(test_sets, 1):
  # Prepare the inputs separated by newlines (just like pressing Enter)
  input_data = f'{a}\n{b}\n{c}\n'

  result = subprocess.run(['/usr/bin/python3', '/Users/apple/Desktop/python.py/VanessaTriangle.py'],
      input=input_data,
      text=True,
      capture_output=True,)
      
  

  print(f'--- Test Set {i} (Inputs: {a}, {b}, {c}) ---')
  print(result.stdout.strip())
  
  a =int(input('請輸入邊長 a：'))
b =int(input('請輸入邊長 b：'))
c =int(input('請輸入邊長 c：'))
side= sorted([a , b , c])
a= side[0]
b= side[1]
c= side[2]

if a +b<=3:
     print('不能成為三角形')
else: 
    if a **2 +b**2  ==c**2:
      print('可成為三角形')
      print('為直角三角形')
    else:
        print('可成為三角形，但不是直角三角形')