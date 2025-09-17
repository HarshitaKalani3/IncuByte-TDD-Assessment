def add(numbers):
    if numbers == "":
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        l = numbers.split("\n",1)
        delimiter = l[0][2:]
        numbers = l[1]
    numbers = numbers.replace("\n",delimiter)
    items = numbers.split(delimiter)
    tot = 0
    neg = []
    for val in items:
        if val!="":
            n = int(val)
            if n<0:
                neg.append(n)
            else:
                tot+=n
    if neg:
        raise Exception("negative numbers not allowed "+ ",".join(map(str,neg)))
    return tot 