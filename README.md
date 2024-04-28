# python_exception
### Exceptions in Python

This Python script is a simple Netflix movie management system. It allows the user to add movies and their information, and then displays all movies or only those of a specific genre: Adventure. 

Custom Exception: Defines a custom exception class called NumNegativo to handle negative numbers.

Initialization: Sets up the program with a title "My Favorite Netflix Movies" and initializes an empty list colecao_principal to store movie information. Also, sets a flag continuar to 's' (yes).

Data Collection Loop: Enters a loop where it collects information about a movie from the user, including the title and genre. It then attempts to get the number of times the movie has been watched from the user.

Exception Handling:
- Catches ValueError if the user enters a non-numeric value when providing the number of times the movie has been watched.
- Raises NumNegativo exception and prints a message if the user enters a negative number.
- Catches any other exceptions and prints their messages.
  
Adding Movie Information: If no exceptions are raised, it adds the movie information to colecao_principal.

Continuation Prompt: Asks the user if they want to add another movie. If 's' (yes) is entered, the loop continues. Otherwise, it exits the loop.

Printing Movie List: After the loop, it prints the colecao_principal list.

Genre-Specific Counting: Prints the title "Adventure Genre Movies" and initializes a counter contador_aventura to 0. Then, loops through colecao_principal, printing the title and number of times watched for each movie whose genre is 'Adventure'. Increments contador_aventura for each movie.

Printing Count: Finally, prints the number of 'Adventure' genre movies.

- Performed for the Database Application & Data Science course.
- Code made in the PyCharm IDE.
  
