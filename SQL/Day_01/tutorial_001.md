
### **Exercice Sheet on Intro to SQL **

**Scenario:**
You are managing the `Products` table for Takealot. The table has the following columns:
*   `product_id` (INTEGER)
*   `product_name` (VARCHAR(128))
*   `price` (DECIMAL(10, 2)) -- e.g., 999.99
*   `category` (VARCHAR(128))
*   `stock_count` (INTEGER)

**Task 1: The Setup**
Write the SQL command to `CREATE` this `Products` table.

**Task 2: Stocking the Shelves**
`INSERT` the following products into your new table:
*   A Samsung 55" TV, costing R12,999.99, in the 'Electronics' category, with 25 in stock.
*   A Nike Air Max running shoe, costing R1,899.99, in the 'Clothing & Shoes' category, with 50 in stock.
*   A Python programming book, costing R455.50, in the 'Books' category, with 100 in stock.
*   A Philips blender, costing R699.00, in the 'Home & Kitchen' category, with 15 in stock.

**Task 3: Reading the Data**
1.  Write a query to show all data for all products.
2.  Write a query to show only the names and prices of all products.
3.  Write a query to find all products in the 'Electronics' category.
4.  Write a query to find the most expensive product (hint: `ORDER BY price DESC` and `LIMIT 1`).

**Task 4: Updating Information**
1.  The Philips blender goes on sale! Update its price to R599.00.
2.  You just sold 10 pairs of the Nike shoes. Update the `stock_count` to reflect this.
3.  You realize the book's category should just be 'Books & Media'. Update it.

**Task 5: Deleting a Product**
The Philips blender has been discontinued and must be removed from the website. Write the command to delete it from the `Products` table.

---