# Define the original string
original_string = "hello"

# Reverse the original string using the reversed() function
# and join the characters back together into a new string

reversed_string = ''.join(reversed(original_string))

# Print the reversed string
print(reversed_string)
# ''.join(…) takes the output from reversed(original_string) and combines all those characters into a new string.
# The '' before .join() means there’s nothing in between the characters, so they will be joined directly together
# programmers prefer to use ''.join().
def reverse_string(word):
    return ''.join(reversed(word))
def test_reverse_string():
    input_string = "TripleTen"
    reversed_str = reverse_string(input_string)
    assert reversed_str == "neTelpirT"
    print("Test Passed! " + input_string + "'s reverse is " + reversed_str)

    # Function that reverses a string


def reverse_string(word):
    return ''.join(reversed(word))

    # Test. Verification of reverse_string function


def test_reverse_string():
    input_str = "TripleTen"

    # Perform the reverse operation
    reversed_str = reverse_string(input_str)

    # Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)