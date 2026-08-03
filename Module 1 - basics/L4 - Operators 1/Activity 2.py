#step 1 : Take input from the user of how many candies they bought
#step 2 : take input from the user to see how many candies fit in 1 bag
#step 3 : find the number of bags they need to fit all the candy
#step 4 : how many candies are left over after packing

candies_bought = int(input("How many candies did you buy?"))
bag_capacity = int(input("How many candies fit in 1 bag?"))

bags_needed = candies_bought // bag_capacity
print(bags_needed)

candies_leftover = candies_bought % bag_capacity
print(candies_leftover)
