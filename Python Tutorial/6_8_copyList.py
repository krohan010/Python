# In this section, we will learn about how to copy one list to another :

pvt_courses = ["BCA", "MCA", "MSCIS", "PGDST", "MSTAT"]
ignou_courses = pvt_courses

# ignou_courses can not store actual value of pvt_course
# ignou_courses will only reference to a pvt_courses

print(ignou_courses)

# The changes made in pvt_courses will automatically also be made in ignou_courses
pvt_courses[0] = "BBA"
# ignou_courses[0] = "BA"

print(ignou_courses)
print(pvt_courses)
print(pvt_courses is ignou_courses)                 # return true because both object are stored in a same location

# copy and list method both are used to copy value from one list to another :
# du_courses = pvt_courses.copy()
# du_courses = list(pvt_courses)

# Slicer option are also used for copying data from one to another list :
du_courses = pvt_courses[:]

# print(du_courses)
du_courses[0] = "MBA"
print(du_courses)
print(pvt_courses)
print(pvt_courses is du_courses)                    # return false because both store in different location