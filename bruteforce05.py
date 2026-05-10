import helper

# show all the options for password w 4 letters
email = str(input("enter your email please"))
for i in range(0, 10):  # thousands
    for j in range(0, 10):  # hundreds
        for f in range(0, 10):  # tens
            for h in range(0, 10):  # unity
                # it will return the password that every digit in them it smaller or equal to the one before her
                if (i >= j) and (j >= f) and (j >= h):
                    password = helper.get_password(i, j, f, h)
                    print(password)
                else:
                    continue
                # check what the password that correct
                if helper.check_password_correct(email, password):
                    print("the password is true", password)
                    # check if all the digits are equal
                    if h == f == j == i:
                        print("the power of the password is 50 its too low. We recommend you to replace password")
                    # check if the number is in ascending order
                    elif (h == f + 1 and f == j + 1 and j == i + 1) or (
                                h == f - 1 and f == j - 1 and j == i - 1):
                        print("the power of the password is 60 its too low. We recommend you to replace password")
                    # check if there are only two different digits
                    # 1000 include for example because 0 and 1 is the only different digits
                    elif (h == f or h == j or h == i or h != f or h != j or h != i) and (f == j or f == i or j == i):
                        print("the power of the password is 70. The power is fine")
                    else:  # the password fit the requirements
                        print("the power of the password is 100 . Excellent choice")
                    exit()
