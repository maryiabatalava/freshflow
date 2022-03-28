# freshflow

problems occurred:

- sales_predictions table has multiple values for the (item_number, day) pair so decided to get only max
- haven't decided what to take as inventory_unit, confused where to use order_intake table
- some (item_number, day) combinations are not presented in sales_predictions or inventory tables -> None values in the
  output
  (so what should be used instead None?)

Test:

```
$ curl http://0.0.0.0:8000/
```