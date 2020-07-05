SELECT
    op.*,
    round(p.price * op.quantity,2) as price
from `Order-Progress` as op
inner join Products p ON
	p.name = op.productName
WHERE
    userName = '{0}' and
    DATE_FORMAT(now(),'%Y-%M-%D') = DATE_FORMAT(date,'%Y-%M-%D')