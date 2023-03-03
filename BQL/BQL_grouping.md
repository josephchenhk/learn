# BQL Grouping

## group().avg() v.s. groupavg()

Pay attention to the difference between the following two:

### group(grouping_item).avg()

This will yield something in groups:

|groups  |values |
|--------|-------|
|group 1 |avg1   |
|group 2 |avg2   |

### groupavg(grouping_item)

This will yield something in individual members with grouping results:

|security |groups  |values |
|---------|--------|-------|
|sec1     |group 1 |avg1   |
|sec2     |group 1 |avg1   |
|sec3     |group 2 |avg2   |
|sec4     |group 3 |avg3   |

## Multiple levels of grouping

```shell
group([group_item_1, group_item_2]).sum()
```

## Groupby
Use the keyword `by` to specify the category:

```python
group(bq.data.A, by=bq.data.B)
```

## Customized func applied to group

basically, `ungroup(func(group(` is a customized `groupfunc`, the function could be defined by the user.
For example, `ungroup(avg(group(` is the same as `groupavg` in BQL.

Below is a more advance example of customized `groupfunc`

```python
def issuer_default_prob(bond_default_prob_lst: bql.om.bql_item.BqlItem) -> float:
    """Probability that at least one of the bonds issued defaults.
    
    Example: issuer_default_prob = 1-(1-0.2)*(1-0.3)*(1-0.5) = 0.72
    >>> bond_default_prob_lst = [0.2, 0.3, 0.5]
    >>> issuer_default_prob(bond_default_prob_lst
    0.72
    """
    return 1 - bq.func.product(1 - bond_default_prob_lst)

ungroup(
    issuer_default_prob(
        group(bq.data.probability_of_default(), by=bq.data.issuer_ticker())
    )
)
```