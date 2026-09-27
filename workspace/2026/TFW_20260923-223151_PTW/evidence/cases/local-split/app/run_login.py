from login import login
from register import register
print("trimmed login:", login("  READER@EXAMPLE.ORG  "))
print("unknown rejected:", not login("other@example.org"))
print("registration:", register("New@Example.org"))
