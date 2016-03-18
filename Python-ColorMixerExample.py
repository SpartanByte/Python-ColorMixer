# Brian Wardwell
# Python - Color Mixer
# This program asks the user to enter two primary colors to mix.
# The program then either displays the secondary color or an error
# message if anything but the three primary colors "red", "yellow",
# "blue" are entered.

def main():
    # Get two primary colors
    color1 = input('Enter a color: red, yellow, or blue: ')
    color2 = input('Enter a different color: red, yellow or blue: ')

    # Determine the color.
    # Determine secondary color based on combination of primary colors.
    if color1 == ('red') and color2 == ('blue'):
        print('purple')
    else:
        if color1 == ('blue') and color2 == ('red'):
            print('The color becomes purple')
        else:
            # Determine if orange.
            if color1 == ('red') and color2 == ('yellow'):
                print('The color becomes orange')
            else:
                if color1 == ('yellow') and color2 == ('red'):
                    print('The color becomes orange')
                else:
                    # Determine if green.
                    if color1 == ('blue') and color2 == ('yellow'):
                        print('The color becomes green')
                    else:
                        if color1 == ('yellow') and color2 == ('blue'):
                            print('The color becomes green')
                        else:
                            # Determine if there is an error
                            if color1 != ('red', 'blue', 'yellow') and color2 != ('red', 'blue', 'yellow'):
                                print('ERROR: a non-primary color was chosen. Try again.')

# Call the main function
main()

"""
Brian Wardwell
Run 1:
Enter a color: red, yellow, or blue: red
Enter a different color: red, yellow or blue: yellow
The color becomes orange
Run 2:
Enter a color: red, yellow, or blue: black
Enter a different color: red, yellow or blue: blue
ERROR: a non-primary color was chosen. Try again.
Run 3:
Enter a color: red, yellow, or blue: blue
Enter a different color: red, yellow or blue: pink
ERROR: a non-primary color was chosen. Try again.
Run 4:
Enter a color: red, yellow, or blue: red
Enter a different color: red, yellow or blue: blue
purple
"""
