num = raw_input("Number of: ")
obj = raw_input("Object: ")


if num=="1":
    print("Result: 1 "+obj)
elif obj.endswith("ife"):
    print("Result: "+num+" "+obj[:-3]+"ives")
elif obj.endswith("sh"):
    print("Result: "+num+" "+obj[:-2]+"shes")
elif obj.endswith("ch"):
    print("Result: "+num+" "+obj[:-2]+"ches")
elif obj.endswith("us"):
    print("Result: "+num+" "+obj[:-2]+"i")
else:
    print("Result: "+num+obj+"s")
