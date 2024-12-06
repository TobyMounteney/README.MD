from moduleinput import calculate

from modulecalculations import add,subtract,multiply,divide

from moduleoutput import plus,minus,x,div

calculate()
add()
subtract()
multiply()
divide()

output = ""
with open "results.txt", "w") as file:
    file.write(output)
