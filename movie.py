movie_1="border"
movie_2 = "dhurandar"
movie_3 = "Pushpa 2"

choose_movie= input(f"movie available are: \n1.{movie_1} \n 2.{movie_2} \n 3.{movie_3}")
price = 0
if choose_movie == 1:
    price ="200 rs"
    print(f"The price of movie ticket is{price}")
    
elif choose_movie==2:
    price = "230 rs"
    print(f"The price of movie ticket is {price}")

else:
  price = "100 rs"
  print(f"the price of movie ticket is {price}")  
    