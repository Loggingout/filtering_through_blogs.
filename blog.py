# list of blogs.
import random
blog_post = ["Tech News For Breakfast.", 
             "Should we keep letting A.I control the things we use?", 
             "Why are so many Tech Companies laying off their workers.", 
             "Was the RP5 worth the wait?", 
             "Beginnners looking to stay motivated programmming?"
             ]
# display blog in random order.
mix = random.choice(blog_post)

blog_post_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
different_times_of_day = ["AM", "PM"]
time_switch = random.choice(different_times_of_day)
timed_blog = random.choice(blog_post_time)
print(mix, timed_blog, time_switch)

# create paragraph to read from.
p_1 = "The cause of not creating better non-access points in our business systems/networks is outrageous. I'm sure you've all heard about the lastest MGM Casino hack? If not let me tell you it was one of the biggest casino hacks over the last 12 years"
print(p_1)


p_2 = input("Is there anyone that would like to share their experience of just learning to code/program? ")
print(p_2)
result = input(" ")
share_result_1 = input(" ")

if result == True:
    print(share_result_1)
elif result == False:
    print("There seems too be someone shy that doesn't want to share how they got into programming, is there anyone else? ")
else:
    print("Nobody wants to share & that's okay.")



