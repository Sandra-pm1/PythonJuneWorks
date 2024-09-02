mobiles=[
    {"id":100,"title":"s23 ultra","brand":"samsung","price":1250000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]


# print all mobile names

mobile_names=[mob.get("title") for mob in mobiles]
# print(mobile_names)

# print all brands

mobile_brands=[mob.get("brand") for mob in mobiles]
# print(set(mobile_brands))

# print samsung mobile names

samsung_mobiles=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
# print(samsung_mobiles)

# print all mobiles available in range of 23k to 40k

available_mobiles=[mob.get("title") for mob in mobiles if mob.get("price") in range (23000,40001)]
# print(available_mobiles)

# print mobile with highest price

def get_price(mob):
    return mob.get("price")
costly_mobile=max(mobiles,key=get_price)
# print(costly_mobile)

# print mobile with lowest price

cheapest_mobile=min(mobiles,key=get_price)
# print(cheapest_mobile)

# sort mobiles using their price

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
# print(sorted_mobiles)

# print the total price of all mobiles

total=sum([mob.get("price")for mob in mobiles])
# print(total)