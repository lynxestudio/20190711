# Understanding OOP Inheritance with Python

<p>
One of the most common goals for the OOP is code reusability. Characteristics such as inheritance contributes to achieving this goal.
</p>
<h3>Inheritance</h3>
<p align="justify">
Inheritance is the most used mechanism to optimise the coding, since it allows to reuse methods defined in superclasses, to define new subclasses. The following example uses the class Person as its superclass.
</p>
Fig 1. Inheritance in a UML Class diagram
<div>
<p>
<img src="images/fig1.png">
</p>
</div>
<p>
We know that a person also can be an employee in addition to talking, and Employee can show its earnings so we will declare a class called Employee.
Who inherits the talk() method of the Person class to implement inheritance in this example:
</p>
<p>
You will notice how the "John" object, which is now an instance of Employee continues to behave as an instance of Person because it has inherited its methods.
</p>
Run the example with the following command
<pre>
py Sample1OOP.py
</pre>
Fig 2. Running the example.
<div>
<p>
<img src="images/fig2.png">
</p>
</div>
