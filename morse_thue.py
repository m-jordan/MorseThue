def generate_morse_thue(digit_length):
    """
    Wiki Definition: In mathematics, the Thue–Morse sequence, or Prouhet–Thue–Morse sequence, is the binary sequence (an infinite sequence of 0s and 1s) obtained by starting with 0 and successively appending the Boolean complement of the sequence obtained thus far. The first few steps of this procedure yield the strings 0 then 01, 0110, 01101001, 0110100110010110, and so on, which are prefixes of the Thue–Morse sequence.
    :param digit_length: Length to limit the length of the infinite sequence.
    :return: Final iteration of Morse-Thue generation.
    """

    morse_thue = '0'

    while (len(morse_thue) < digit_length):
        # print(morse_thue)

        morse_thue_add = ''
        for num in morse_thue:
            if num == '0':
                morse_thue_add += '1'
            elif num == '1':
                morse_thue_add += '0'

        # print('MT :', morse_thue)
        # print("MTA:", morse_thue_add)
        # print()
        morse_thue += morse_thue_add

    return morse_thue

print(generate_morse_thue(9))