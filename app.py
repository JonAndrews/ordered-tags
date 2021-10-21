import random
import string
import itertools


def random_generation_example(num=10000, show=50):
    print("Running Randomly Generated Tags Example")

    target = generate_tags(5)
    print(f"Example target tags are {target}.")

    projects = generate_projects(num)
    print(f"Generated {len(projects)} unique projects; showing top {show}.")

    for project in projects:
        project["score"] = score_tags(target, project["tags"])

    projects.sort(key=lambda p: p["score"], reverse=True)

    for project in projects[:show]:
        if project['score'] <= 0:
            break
        print(f"{project['id']}\t{round(project['score'], 4)}\t{project['tags']}")

    print("Done.")


def subset_permutations_example():
    "Running Subset Permutations Example"

    target = ['A', 'B', 'C', 'D']
    print(f"Example target tags are {target}.")

    subsets = generate_subset_permutations(target)

    projects = [{"tags": s} for s in subsets]
    print(f"Generated {len(projects)} projects.")

    for project in projects:
        project["score"] = score_tags(target, project["tags"])

    projects.sort(key=lambda p: p["score"], reverse=True)

    for project in projects:
        if project['score'] <= 0:
            break
        print(f"{round(project['score'], 4)}\t{project['tags']}")

    print("Done.")


def generate_tags(n):
    return list({random.choice(string.ascii_uppercase) for _ in range(n)})


def generate_projects(n):
    current_tags = []
    for i in range(n):
        new_tags = generate_tags(i % 5 + 1)
        if new_tags not in current_tags:
            current_tags.append(new_tags)
    return [{"id": i, "tags": current_tags[i]} for i in range(len(current_tags))]
    # return [{"id": i, "tags": generate_tags(i % 5 + 1)} for i in range(n)]


def generate_subset_permutations(target):
    n = len(target)
    subsets = []
    for i in range(n):
        subsets.extend(list(itertools.combinations(target, i+1)))
    return subsets


def value_tags(tags):
    n = len(tags)
    s = (n*(n+1))/2
    return [(n-g)/s for g in range(n)]


def score_tags(target, given):
    scalar_1 = 0
    scalar_2 = 1
    scalar_3 = 1

    if not target or not given:
        return 0

    n = len(target)
    gn = len(given)

    target_values = value_tags(target)
    given_values = value_tags(given)

    # Step 1
    # Add to scalar_1 the values of matched tags.
    for i in range(n):
        if target[i] in given:
            scalar_1 += target_values[i]

    # If there is only one tag in given, the next checks will not modify the score at all.
    if gn <= 1:
        return scalar_1

    # Step 2
    # Sum value of alien tags in given, and subtract from scalar_2.
    for i in range(gn):
        if given[i] not in target:
            scalar_2 -= given_values[i]

    # If there is only one tag in target, the next check will not modify the score at all.
    if n <= 1:
        return scalar_1 * scalar_2

    # Step 3
    # Collect matched tags and assess order.
    matched_tags = [g for g in given if g in target]
    mn = len(matched_tags)
    if mn > 1:
        wrong_order_factor = ((mn**2)-1)/(mn**2)
        target_to_following = {t: target[target.index(t)+1:] for t in target[:-1]}

        for i in range(mn - 1):
            t = matched_tags[i]
            t_next = matched_tags[i+1]
            if t not in target_to_following or t_next not in target_to_following[t]:
                scalar_3 *= wrong_order_factor

    return scalar_1 * scalar_2 * scalar_3


if __name__ == '__main__':
    random_generation_example()
    subset_permutations_example()
