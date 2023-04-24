# Understanding OOP Inheritance with Python

One of the most common goals for the OOP is code reusability. Characteristics such as inheritance contributes to achieving this goal.

Inheritance
Inheritance is the most used mechanism to optimise the coding, since it allows to reuse methods defined in superclasses, to define new subclasses. The following example uses the class Person as its superclass.

Fig 1. Inheritance

Fig 2. Person Class

We know that a person also can be an employee in addition to talking, and Employee can show its earnings so we will declare a class called Employee.

Fig 3. Employee Class

Who inherits the talk() method of the Person class to implement inheritance in this example:

Fig 4. Main program

You will notice how the "John" object, which is now an instance of Employee continues to behave as an instance of Person because it has inherited its methods.

Fig 4. Run the example
$ py Sample1OOP.py

Download example source code.
