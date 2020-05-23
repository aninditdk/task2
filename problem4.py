#Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.

sample={
'physics':88,'maths':75,'chemistry':72,'Basic electrical':89
}
g=min(list(sample.values()))
key=list(sample.keys())
value=list(sample.values())
print(key[value.index(g)])
