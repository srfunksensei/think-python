def how_old():
    """Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”"""
    my_age = 12
    moms_age = 21

    num_mathes_during_life = 8
    count = 0
    for i in range(my_age, 100):
        moms_new_age = moms_age + (i - my_age)
        if str(i) == str(moms_new_age)[::-1]:
            count += 1
            if count == num_mathes_during_life:
                print(my_age)


how_old()

