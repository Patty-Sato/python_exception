# python_exception
Exceptions in Python

This Python script is a simple Netflix movie management system. It allows the user to add movies and their information, and then displays all movies or only those of a specific genre (Adventure). 

Here’s what it does:

It declares a custom exception class NumNegativo for handling negative numbers.
It initializes the program with a title “My Favorite Netflix Movies”.
It creates an empty list colecao_principal to store movie information and sets a flag continuar to ‘s’ (yes).
As long as continuar is ‘s’, it enters a loop where it collects information about a movie from the user, including the title and genre.
It then attempts to get the number of times the movie has been watched from the user. If the user enters a non-numeric value, it catches a ValueError and prints a message. If the user enters a negative number, it raises a NumNegativo exception and prints a message. Any other exceptions are also caught and their messages are printed.
If no exceptions are raised, it adds the movie information to colecao_principal.
It then asks the user if they want to add another movie. If the user enters ‘s’, the loop continues. Otherwise, it exits the loop.
After the loop, it prints the colecao_principal list.
It then prints the title “Adventure Genre Movies” and initializes a counter contador_aventura to 0.
It loops through colecao_principal and for each movie whose genre is ‘Adventure’, it prints the movie’s title and number of times watched, and increments contador_aventura.
Finally, it prints the number of ‘Adventure’ genre movies and a separator line.
