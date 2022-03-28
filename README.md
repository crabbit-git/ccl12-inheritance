# What's this then?

This is the 12th "lab" exercise assigned by a software development course I'm doing at the moment. The point of this one was to familiarise us with inheritance in Python. You can see the instructions we were given in `task.md`.

# What does it actually do?

It isn't really an application or anything, just a collection of class definitions which involve inheritence of attributes and functions from superclasses. I initially structured this as a bunch of unit tests and class modules because we've been doing that a lot lately and I figured that was probably what was wanted here as well, but the instructions actually specify that we've just to use print statements instead, so I restructured it to do that.

With `animals.py`, I primarily focused on functions: I didn't really bother with attributes so there are no uninherited attributes, both animal classes (Cat and Chicken) just have a "name" attribute inherited from the Animal class and that's it. As such, there is no need to call `super().__init__()`, and I instead use `super()` to modify functions.

With `musicians.py`, I did the exact opposite: I had Singer, Guitarist, and Drummer inhert _only_ attributes from Musician, and kept the functions global for Musician with no subclass functions to override them. I did include an extra wee function to let any musician learn additional instruments, but it's very basic and isn't very flexible for the time being.

Because I'm also working a day job as I do this course, I ran out of time (had to start work) around the time I got to `boats.py`, which I wasn't that sad about because I know bugger all about boats and would really have to think hard to work out something I could write that would be applicable to that context and also demonstrate something about my understanding of classes/inheritance. This also meant I didn't get to writing a `doctors.py` yet either. I'll revisit later if I can identify an opportune moment to do so.
