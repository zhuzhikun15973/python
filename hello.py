
a = 1;
b = True;
# string
c = "{name} wants to eat {food}".format(name="Bob", food="lasagna");
d = "%s can be %s" % ("strings", "interpolated");

if b:
    print 'I love python'
print c
d = [x + 3 for x in range(6)]
print d

def f(a,L = [1,2]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
