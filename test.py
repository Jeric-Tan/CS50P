
def main():

    dict = {"name" : "john",
            "colours": "red",
            "numbers": 2}

    key = dict.keys()
    print(key)


    #keys[i] ={key : value} pair


if __name__ == "__main__":
    main()

CREATE TABLE purchase (purchase_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                       customer_id INTERGER NOT NULL,
                       time TIMESTAMP,
                       stock TEXT NOT NULL,
                       qty  INTEGER,
                       price INTEGER,
                       FOREIGN KEY (customer_id) REFERENCES users(id));

UPDATE users SET cash = 10000 WHERE username = "david";

SELECT stock, SUM(qty) FROM purchase WHERE customer_id = 4 GROUP BY stock

CREATE TABLE display (customer_id INTERGER NOT NULL,
                    stock TEXT NOT NULL,
                    qty INTEGER,
                    FOREIGN KEY (customer_id) REFERENCES users(id))

CREATE TABLE sell (sell_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                       customer_id INTERGER NOT NULL,
                       time TIMESTAMP,
                       stock TEXT NOT NULL,
                       qty  INTEGER,
                       price INTEGER,
                       FOREIGN KEY (customer_id) REFERENCES users(id));


SELECT purchase.customer_id, purchase.purchase_id, purchase.time, purchase.stock, purchase.qty, purchase.price FROM purchase
JOIN sell ON sell.customer_id = purchase.customer_id;


SELECT time, transaction_type, stock, qty FROM (SELECT 'purchase' AS transaction_type, purchase_id AS transaction_id, stock, customer_id, time, qty
FROM purchase
UNION ALL
SELECT 'sell' AS transaction_type, sell_id AS transaction_id, stock,customer_id, time, qty
FROM sell) WHERE customer_id = 5 ORDER BY time

