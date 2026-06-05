## Completed Chapter 06 Dictionaries.  
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/06-dictionaries-annotations.pdf)
### Key Insights and Progress Log.  
>In this chapter we learn about Python's dictionaries, which allow us to relate pieces of related information.
>A `dictionary` in Python is a collection of `key-value pairs`. Each `key` is connected to a `value` and we can use a key to access the value associated with the key, the keys' and values' value can be a number, a string, a list, a dictionary, infact any object we can create in Python can be a value in a dictionary (of key or value). In python a distionary is wrapped in brances ({}) with a series of key value pairs inside the braces in format `key: value` seperated by commas, e.g...
>```code
>dictionary = {key1: value1, key2: value2,..., keyn: valuen}
>```
>A `key-value pair` is a set of values associated with each other, when we provide a key python returns the value associated with it, to get the value associated with a key, we give the name of the dictionary and then place the key inside a set of square braces e.g... `dictionary[key2]` will return `value2` (know that we can have an infinite number of key-value pairs in a dictionary).
>Dictionaries are dynamic, we can `add new key-value pairs` at any time, to do so we just give the name of the dictionary followed by the new key in square brackets, along with the new value e.g... `dictionary[keyn+1] = valuen+1` will add a new key value pair as mentioned, also dictionaries retail the order in which they were defined so when we add new key-value pairs to a dictionary, they are added to the end of the dictionary and when we print a dictionary by `print(dictionary)` we get the elements in the same order they were added to the dictionary same for a for loop, so we will get `{key1: value1, key2: value2,..., keyn: valuen, keyn+1: valuen+1}` by the print call.
>Also we can `start with an empty dictionary` with just an empty set of braces. e.g... `dictionary_1 = {}`, this is an empty dictionary and we can start filling in key-value pairs as usual.
>We can `modify values in a dictionary' by giving the name of the dictionary with the key in square brackets and then the new value we want associated with the key. e.g... `dictionary[key1] = valuenew1` modifies the value of key1 in dictionary from value1 to valuenew1, so now dictionary[key1] returns valuenew1!
>`Removing key-value pairs` is child's play too, to do so we use the `del statement`, all `del` needs is the name of the dictionary and the key whose key-value pair you want to remove, so a simple `del dictionary[keyn+1]` will delete the key keyn+1 from dictionary dictionary, along with its value so now `print(dictionary)` returns `{key1: value1, key2: value2,..., keyn: valuen}`.
>We can use a dictionary to store different kinds of information about one object or to store one kind of informations about many objects, for the latter we can use the format of definition of the dictionary as:
>```code
>dictionary = {
>    key1: value1,
>    key2: calue2,
>    .
>    .
>    .
>    keyn: valuen,
>    }
>```
>If we try to access a key in a dictionary the normal way and it doesnt exist then we will get an error (a `KeyError`), a workaround for this is `using get() method to access values`, using this method we can set a default value that will be returned if the requested key doesnt exist. They get() method requires a key as a first argument and as a second optional argument, we can pass the value to be returned if the key doesnt exist (value `None` will be returned if left second argument is empty)
>so `dictionary.get(keya, 'No value assigned')` will return 'No value assigned' if there is no key named keya and will act normally if it does.
>
>Python lets us `loop through a dictionary`. Since dictionaries can be used to store information in a variety of ways, therefore, several different ways exist to loop through then. We can loop through all of a dictionary's key-value pairs, through its keys or through its values.
>To write a `for` `loop for a dictionary's key-value pairs`, we create names for the two variables that will hold the key and value in each key-value pair, e.g...
>```code
>for <key holding variable>, <value holding variable> in dictionary.items()
>    print(<key holding variable>)
>    print(<value holding variable>)
>```
>here in each loop the 2 variables holds all the key and value pairs' values one by one from start, so here we will get the result:
```code
key1
value1
key2
value2
.
.
.
keyn
valuen
```
>Notice that the second half of the for statement includes the name of the dictionary followed by the method `items()`, which returns a sequence of key-value pairs. The `for` loop then assigns each of these pairs to the 2 variables provided.  
>We can also `loop through all the keys in a dictionary` using the `keys()` method, so the statement `for <key holding variable> in dictionary.keys()` will do exactly what you're expecting, also looping through the keys is actually the default behavior when looping through a dictionary, so in the above statement even ommiting `.keys()` in the above statement yields the same effect. (as a bonus, know that inside a particular such loop we can also access the value of the `current key` easily by the basic way (ponder)). Finally we can also see if a particular object exists as a key in a dictionary by the `keys()` method, e.g... `<object> in dictionary.keys()` will return true if the specified object is a key in the dictionary and false if it is not, therefore this can also be used as a conditional statement in an if statement (since the keys() method is not just for looping but rather it returns a sequence of all keys in a dictionary).
>We can also `loop through a dictionary's keys in a particular order`, by default looping through a dictionary returns the items in the same order as they were inserted, but we can also use the `sorted()` function to sort the keys as they're returned in the `for` loop to get a copy of the keys in order. e.g...
>```code
>dictionary = {
>    key1: value1,
>    key2: calue2,
>    .
>    .
>    .
>    keyn: valuen,
>    }
>
>for <key holding variable> in sorted(dictionary.keys()):
>    print(f"One of the keys is {<key holding variable>}")
>```
>which will return
>```code
>One of the keys is key1
>One of the keys is key2
>.
>.
>.
>One of the keys is keyn
>```
>
>
