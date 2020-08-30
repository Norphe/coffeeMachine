user_input = input("Enter cells: ")
user_list = list(user_input)
print("---------")
print("|", user_list[0], user_list[1], user_list[2], "|")
print("|", user_list[3], user_list[4], user_list[5], "|")
print("|", user_list[6], user_list[7], user_list[8], "|")
print("---------")

game = [[user_list[0], user_list[1], user_list[2]],
        [user_list[3], user_list[4], user_list[5]],
        [user_list[6], user_list[7], user_list[8]]]
