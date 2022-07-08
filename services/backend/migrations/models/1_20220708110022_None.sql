-- upgrade --
CREATE TABLE IF NOT EXISTS "orders" (
    "id" VARCHAR(35) NOT NULL  PRIMARY KEY,
    "date_opened" TIMESTAMPTZ NOT NULL,
    "date_closed" TIMESTAMPTZ NOT NULL,
    "total" INT NOT NULL,
    "cashier" VARCHAR(125) NOT NULL,
    "waiter" VARCHAR(125) NOT NULL,
    "zone" VARCHAR(63) NOT NULL,
    "table" INT NOT NULL,
    "diners" SMALLINT NOT NULL,
    "products" JSONB NOT NULL,
    "payments" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
