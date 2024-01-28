# Мария Путкова, 12-я когорта — Финальный проект. Инженер по тестированию плюс
# Задание 1:
SELECT c.login, COUNT(o."inDelivery" = 't') AS "orders count"
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
GROUP BY c.login;

# Задание 2:
SELECT track,
CASE WHEN finished = 't' THEN '2'
WHEN cancelled  = 't' THEN '-1'
WHEN "inDelivery" = 't' THEN '1'
ELSE '0'
END AS status
FROM "Orders";