# Lists
techList = ["Apple", "Microsoft", "Samsung", "Dell", "HP"]
print(techList[0:2])
techList[0] = "Tesla"
print(techList)

techList.remove("Samsung")
print(techList)

techList.insert(3, "Tesla")
print(techList)

print(len(techList))
print("Microsoft" in techList)

# techList.clear()
# print(techList)

# Dictionary
fruits = {
	"banana": 0.49,
	"orange": 1.5,
	"apple": 1.09
}

fruits["banana"] = 2.6
print(fruits)