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
