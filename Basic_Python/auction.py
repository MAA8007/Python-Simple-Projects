bidders= {}
morebids ="yes"
highest = 0
highname = ""
while morebids == "yes":
    name = input('enter name')
    bid = int(input('enter bid'))
    bidders[name] = bid
    more = input('more?')
    if more != "yes":
        morebids = "no"

for key, value in bidders.items():
    if value> highest:
        highname = key
        highest = value
print(highname)
print(highest)


