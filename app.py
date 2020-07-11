hours = input("How many hours did you work this week? ")
rate = input("What is your hour wage? ")
hours_num = float(hours)
rate_num = float(rate)


def compute_pay (hours_num, rate_num):
    if hours_num > 40 :
        reg = hours_num * rate_num
        otp = (hours_num - 40) * (rate_num * 0.5)
        pay = reg + otp
    else:
        pay = hours_num * rate_num
    print(pay)


compute_pay(hours_num, rate_num)

