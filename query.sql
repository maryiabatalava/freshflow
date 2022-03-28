select distinct stg.item_number, delivery_day, ordering_day,
       suggested_retail_price sales_price_suggestion,
       profit_margin, stg.purchase_price,
       item_categories, tags, extra_categories,
       case_content_quantity case_quantity,
       case_content_unit case_unit,
       ceil((sp.sales_quantity - i.inventory) / case_content_quantity) order_quantity,
       'CS' order_unit,
       inventory inventory_quantity,
       '' inventory_unit
from orderable_items stg
left join
(select item_number, day, max(sales_quantity) sales_quantity
 from sales_predictions
 group by item_number, day) sp
on stg.item_number = sp.item_number
and stg.delivery_day = date(sp.day)
left join inventory i
on stg.item_number = i.item_number
and stg.ordering_day = date(i.day)