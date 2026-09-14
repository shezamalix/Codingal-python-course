# we have a tuple which contains only 0s and 1s
#0 represents sunny weather , 1 represents rainy weather
#our goal is to predict whether its more likely to rain tomorrow or not

weather = (0, 0, 1, 1, 0, 1, 0, 1, 1, 1 )

sunny = weather.count(0)
rainy = weather.count(1)

#if sunny > rainy :
  #  print("Sunny")
#else:
#    print("Rainy")

sunny = 0
rainy = 0

for i in weather:
    if i == 0 :
        sunny +=1
    else:
        rainy += 1

if sunny > rainy :
    print("Sunny")
else:
    print("Rainy")

