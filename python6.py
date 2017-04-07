x = "there are %d people" % 10
a = "binary"
b = "don't"
y = "those who know %s and those who %s" % (a,b)

print x
print y

print "i said : %r." % x
print "i also said: '%s'" % y

hill = False
joke = "isn't that joke so funny? %r"

print joke % hill

w = "left side...."
e = "right side string"

print w + e