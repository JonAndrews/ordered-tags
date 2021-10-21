# ordered-tags

This is an example of how an ordered set of tags could be compared to other ordered sets of tags.

# Methodology

## Tag Values

A set of tags is ordered by importance. In order to equate the importance of tags among different length sets, we can assign a value to each tag based on its position in the set.  
For example, consider `n` tags:

```
T₀, T₁, ..., Tₙ₋₁, where n >= 1.
```

In order to make sets of tags of diffent lengths comparable, the sum of their tag values should be one.  
A convenient number to help describe the value of a tag based on its position is the sum of integers up to and including `n`. Let's call this value `s`.

```
s = (n · (n + 1)) / 2.
```

Using `s`, and given a tag, `Tᵢ`, the positional value is:

```
vᵢ = (n - i) / s.
```

So for example, if there were four tags, `T₀`, `T₁`, `T₂`, and `T₃`, then their positional values would be calculated as follows:

```
n = 4.
s = (4 · (4 + 1)) / 2 = 10.
T₀  ->  v₀ = (4 - 0) / 10 = 0.4
T₁  ->  v₁ = (4 - 1) / 10 = 0.3
T₂  ->  v₂ = (4 - 2) / 10 = 0.2
T₃  ->  v₃ = (4 - 3) / 10 = 0.1
```

## Scoring

A score represents how related a given set of tags is to a target set. A score of `0` means that there is no relation. A score of `1` means that there is an exact match. There are three scalars that are multiplied in order to create this score.

1. Scoring matched tags.
   - For every tag that a given set has that is in the target set, the positional value of that tag in the target set is added to the scalar.
   - If there are no matched tags, the scalar is `0` and is returned.
2. Scoring extra tags.
   - For every tag that a given set has that is **not** in the target set, the positional value of that tag in the given set is subtracted from the scalar.
   - If there are no extra tags, the scalar is `1`.
3. Scoring tag order.
   - Of the tags in the given set that are found in the target set, each tag is assessed to determine if its following tags are correctly ordered (even if not adjacent in the target set).
   - If the tags are not correctly ordered, then there is a penalty of based on the number of matched tags, `m`: the scalar is multiplied by `(m² - 1) / m²`.
