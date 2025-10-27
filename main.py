import asyncio
import random as rand
from Maths.Math import Multiply
from Maths.Math import Add
from Maths.Math import Sub
from Maths.Math import Divide
from Messages.Messages import createFileSync
from Time.TimerSet import createSleep

num1 = rand.randint(1, 5) * 2
num2 = rand.randint(1, 5) * 2

question = input("Enter Type of Multiplcation Table: ")

mMath = Multiply(int, num1, num2)
aMath = Add(int, num1, num2)
sMath = Sub(int, num1, num2)
dMath = Divide(int, num1, num2)


async def runnable():

    createSleep(9)

    if question == "x":

        print(f"What is: {mMath.get_num1()} x {mMath.get_num2()}")
        answer = int(input("Enter Answer: "))

        if answer == mMath.calculate_numbers():
            print("Correct")
        else:
            print("Not Correct")

    if question == "+":

        print(f"What is: {aMath.get_num1()} + {aMath.get_num2()}")
        answer = int(input("Enter Answer: "))

        if answer == aMath.calculate_numbers():
            print("Correct")
        else:
            print("Not Correct")

    if question == "-":

        print(f"What is: {sMath.get_num1()} - {sMath.get_num2()}")
        answer = int(input("Enter Answer: "))

        if answer == sMath.calculate_numbers():
            print("Correct")
        else:
            print("Not Correct")

    if question == "/":

        print(f"What is: {dMath.get_num1()} / {dMath.get_num2()}")
        answer = int(input("Enter Answer: "))

        if answer == dMath.calculate_numbers():
            print("Correct")
        else:
            print("Not Correct")


try:
    asyncio.run(runnable())
except Exception:
    print("")
