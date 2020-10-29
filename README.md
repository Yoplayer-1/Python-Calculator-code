# Python-Calculator-code


So the first line import pyttsx3 (python text to speech don't know what x stands for and 3 for version 3) and math. But there is no use of math module so no nned of that but if you are extending the functions then you can use it.

So the first variable is engine which initializes the pyttsx3 module 

the next function is speak the text (which is the argument audio) so engine.say(audio) will speak the argument passed  then if we don't enter engine.runAndWait() the function cannot speak. To use it type speak("Hello World") and it will speak hello world

so the first function is addition I think you can understand it by seeing it and all the rest functions.


so next we created a variable named calc_on and set the value to 1 this will be used to quit the while loop 

next we create the function quit which is used to quit the app so it will just print Thanksfor using this app and also speak it then it makes the variable calc_on global and then sets it to 0 which in our case is off

then we create calc_run and it asks enter function and then prints and speaks you chose op (the variable which asks enter function) and the if staments use the add, subtract, multiply, divide, modulo or quit based on user input.

then we speak and print Do you want to add,subtract,multiply,divide, modulo or quit. 

Then we add the while loop the works when calc_on == 1 then run our function calc_run





THANK YOU
