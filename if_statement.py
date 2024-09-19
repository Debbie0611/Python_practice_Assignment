is_female = True
is_beautiful = True

if is_female and is_beautiful:
    print("Your are a beautiful female")
elif is_female and not(is_beautiful):
    print("You are an ugly female")
elif not(is_female) and is_beautiful:
    print("you are not a female but you are beautiful")
else:
    print("you are neither a female nor beautiful")