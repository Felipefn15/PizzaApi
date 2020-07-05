SELECT
    *
from `Order-Progress`
WHERE
    userName = '{0}' and
    DATE_FORMAT(now(),'%Y-%M-%D') = DATE_FORMAT(date,'%Y-%M-%D')