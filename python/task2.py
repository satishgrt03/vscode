import re
story = "my name is satish, and i work in hallmark at kakinada city, kakinada is a city in andhra pradesh, its famous for a sweet called kaja, kaja is sold at same street as hallmark."
m = {
    "name" : "satish",
    "company" : "hallmark",
    "city" : "kakinada",
    "favorite" : "kaja",
    
}
# m.update({"state" : "andhra pradesh",}) #using update method
# print(m)
# print(m["name"]) 
# print(m.get("state")) #using get method
# print(m.values()) #using values method
# print(m.keys()) #using keys method
# print(m.items()) #using items method

final_list = []
search_list = m.values()

for x in search_list:
    for y in re.finditer(x,story):
        start_index = story.find(x)
        end_index = start_index + (len(x)-1)
        list = [x,start_index,end_index]
        final_list.append(list)
print(final_list)