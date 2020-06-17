# Play FizzBuzz from one to a hundred.
# Rules: If the number is divisable by 3 then replace it with Fizz, if by 5 then Buzz, and if both Fizz Buzz

# Dictionary of replacements
rep_dic = {
    3: 'Fizz',
    5: 'Buzz',
    7: 'Spam',
    11: 'Eggs',
    13: 'Ham'
}

# For loop from 1 to 100
for num in range(1, 101):
    # Make a replacement string to hold the Fizz Buzz strings
    fb_str = ''
    for key in rep_dic:
        # If the number is completely divisable by the key then add the replacement string to the end of fb_str
        if num % key == 0:
            fb_str += rep_dic[key]
    # If the fb_str is empty and therefore false print the number
    if fb_str:
        print(fb_str)
    # Otherwise just print the fb_str
    else:
        print(num)
