SELECT
    *
from `Order-Progress`
WHERE
    email = '{0}' and
    DATE_FORMAT(now(),'%Y-%M-%D') = DATE_FORMAT(date,'%Y-%M-%D')