"""Restaurant rating lister."""

import sys

# Read the ratings from a file
file = open(sys.argv[1])

def get_restaurant_data(filename):
    """
    Iterate through the contents of a file object to store restaurant data elements
    as a key, value pair in a dictionary.

    :param filename: text file as a file data object
    :return: restaurant name, ratings data as a dictionary
    """
    # Initialize a dictionary
    all_restaurants = {}

    # Move pointer to first element of the file
    filename.seek(0)

    # Parse the file contents and store the restaurant, ratings in a dictionary
    for line in file:
        restaurant_info = line.strip().split(":")
        all_restaurants[restaurant_info[0]] = restaurant_info[1]
    
    return all_restaurants

def sort_restaurants(all_restaurants):
    """
    Sort a dictionary of restaurant name, rating in ascending alpha-sort order.

    :param all_restaurants: restaurant name, rating data as a dictionary
    :return: ascending alpha-sort restaurant name, rating as a list
    """

    # Call sorted() on the dictionary.items() and store results as a list variable
    sorted_restaurants = sorted(all_restaurants.items())

    return sorted_restaurants

def print_ratings(sorted_restaurants):
    """
    Prints out a message detailing restaurant name, ratings in ascending alpha-sort order.

    :param sorted_restaurants: restaurant name, ratings in ascending alpha-sort as a list.
    :return: None
    """

    for restaurant in sorted_restaurants:
        print(f"{restaurant[0]} is rated at {restaurant[1]}.")

def add_ratings(filename):
    """
    Allow the user to enter a restaurant name and restaurant rating.
    Store the new restaurant and rating in the dictionary.
    Print all the ratings in ascending alpha-sort order.
    """

    # Initialize a dictionary of restaurant data to add-to
    all_restaurants = get_restaurant_data(filename)

    # Get restaurant name from user
    restaurant_name = input("Enter a restaurant name: ")

    # Repeat until break
    while True:

        # Get restaurant rating from user
        restaurant_rating = int(input("Enter a restaurant rating: "))

        # Validate rating is between 1 and 5 (inclusive)
        if restaurant_rating >= 1 and restaurant_rating <= 5:
            all_restaurants[restaurant_name] = restaurant_rating
            break
        else:
            print("Please enter a rating between 1 and 5 (inclusive): ")

    sorted_restaurants = sort_restaurants(all_restaurants)

    print_ratings(sorted_restaurants)

# Function call
print(print_ratings(sort_restaurants(get_restaurant_data(file))))

# To help seprate function-call readability
print("# " * 35)

# Another function call
add_ratings(file)

# Close the file
file.close()