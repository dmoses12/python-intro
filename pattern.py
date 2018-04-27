def pattern(number):
    """Function to generate a pattern
    syntax: pattern(number)
    input: number
    output: symetrical pattern of _ and * according to number provided
    return: 0 when complete
    """
    print "Pattern for number: %s" % number
    # complete this function

    max_stars = 2 * number - 1 # max number of stars to print
    num_ulines = number - 1; # number underscores for first line
    # print to max_stars and fill with _
    for i in range(1, max_stars, 2):
        print "_ " * num_ulines + "* " * i + "_ " * num_ulines
        num_ulines -= 1  # decrease underscores as we increase stars
    # complete and reverse pattern
    for i in range(max_stars, 0, -2):
        print "_ " * num_ulines + "* " * i + "_ " * num_ulines
        num_ulines += 1 # increase underscores as we decrease stars
    return 0

if __name__ == "__main__":
    pattern(1)
    pattern(2)
    pattern(3)
    pattern(4)
