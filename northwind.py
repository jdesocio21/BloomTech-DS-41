expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""


avg_hire_age = """
SELECT avg(HireDate-BirthDate)
FROM Employee
"""


ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON Supplier.Id = Product.SupplierId
ORDER BY UnitPrice DESC
LIMIT 10
"""


largest_category = """
SELECT Category.CategoryName, COUNT(DISTINCT(Product.Id))
FROM Category
JOIN Product ON Category.Id = Product.CategoryId
GROUP BY 1
    ORDER BY 2 DESC
LIMIT 1
"""
