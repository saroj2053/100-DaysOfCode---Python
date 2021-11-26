total_class_members = 90


def prob_swim(candidate, total):
    return candidate / total


result1 = prob_swim(candidate=20, total=total_class_members)


def prob_basketball(candidate, total ):
    return candidate / total


result2 = prob_basketball(candidate=15, total=total_class_members)


def prob_gym(candidate, total):
    return candidate / total


result3 = prob_gym(candidate=30, total=total_class_members)


def prob_tennis(candidate, total):
    return candidate / total


result4 = prob_tennis(candidate=25, total=total_class_members)

# Computing probabilities for muscular and fast


def prob_muscular(persons, total):
    return persons / total


muscular_prob = prob_muscular(persons=25, total=total_class_members)


def prob_fast(persons, total):
    return persons / total


fast_prob = prob_fast(persons=23, total=total_class_members)

# Computing Conditional Probabilities

# For Swimming
swim_members = 20
muscular_swim = 12 / swim_members # Probability of a person fit for swimming if he/she is muscular
fast_swim = 4 / swim_members

# For Basketball
basketball_members = 15
muscular_basketball = 2 / basketball_members
fast_basketball = 2 / basketball_members

# for Gymnastics

gym_members = 30
muscular_gym = 5 / gym_members
fast_gym = 3 / gym_members

# for tennis

tennis_members = 25
muscular_tennis = 6 / tennis_members
fast_tennis = 14 / tennis_members

# Computing Final Probability

# Probability of a person being recruited to swimming team if he/she is muscular and fast
value = (muscular_prob * fast_prob)
final_prob_swim = (muscular_swim * fast_swim * result1) / value
print(f"Probability of a swimming class {final_prob_swim}")

final_prob_basketball = (muscular_basketball * fast_basketball * result2) / value
print(f"Probability of a basketball class {final_prob_basketball}")

final_prob_gym = (muscular_gym * fast_gym * result3) / value
print(f"Probability of a Gymnastics class {final_prob_gym}")

final_prob_tennis = (muscular_tennis * fast_tennis * result4) / value
print(f"Probability of a Tennis class {final_prob_tennis}")

