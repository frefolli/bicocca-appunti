# Transform Self Type Checks

## Pro

- Component behavior isolation
- Changes/additions/removal of behavior doesn't change user of such behaviors
- Behaviors share a common interface

## Cons

- Explosion of abstractions and classes
- Difficult to get a large picture of the behavior of the subsystem
- Manipulation of class instances is heavily bloated (huge number of instances and gc workload)

## Tips

- Explicit checks are not always a problem, it depends (show an example of untouchable code with switch), and can be tolerated / optimal when the number of places in which are done is low or the number of cases is fixed and low.
- In some circumstances abstractions are application killers (show OsDev print function paradox)
- Most of the time a monad is just what you wanted (show an image of code refactored for monads)
