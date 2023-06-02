# Scrie un program care preia suma principală, rata dobânzii și timpul (în ani) ca intrare.
# Calculează și afișează dobânda simplă folosind formula:
# dobândă = (suma principală * rată dobândă * timp) / 100.
sum = int(input("Please input your total sum of money: "))
interest_rate = int(input("Please input the interest rate: "))
time = int(input("Please input how many years will the money stay in the bank: "))
final_interest = (sum * interest_rate * time) / 100
print(f"Your simple interest will be: {final_interest}")