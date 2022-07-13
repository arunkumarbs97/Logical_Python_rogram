import random

class Coupon:
    def generate_coupon(self, lower, upper, number):

        coupon_numbers = set([])
        for i in range(number):
            coupon = random.randint(lower, upper)
            print(coupon)
            coupon_numbers.add(coupon)

        return coupon_numbers


if __name__ == "__main__":
    coupon = Coupon()
    lower_range = int(input("Enter lower value: "))
    upper_range = int(input("Enter upper value: "))
    number = int(input("Enter number of unique coupon numbers to generate: "))
    list = coupon.generate_coupon(lower_range, upper_range, number)
    print(list)