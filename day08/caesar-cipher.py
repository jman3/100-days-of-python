from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(input_direction, input_text, shift_amount):
    final_output = ""

    # decode인 경우 index 값을 빼줘야하므로 -1을 곱해두면 반복문에서 encode, decode 모두 +로 처리할 수 있다
    if input_direction == "decode":
        shift_amount *= -1

    # 알파벳 개수 26으로 나눠주면 26보다 큰 수에 대해서도 IndexError를 방지할 수 있다
    for char in input_text:
        # 숫자나 특수문자 등 알파벳이 아닌 문자인지 체크한다
        if char in alphabet:
            idx = (alphabet.index(char) + shift_amount) % 26
            final_output += alphabet[idx]
        else:
            final_output += char

    print(final_output)


end_of_cipher = False
while not end_of_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again == "no":
        end_of_cipher = True
        print("Good bye.")
