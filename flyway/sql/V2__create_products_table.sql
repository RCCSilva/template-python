CREATE TABLE template.products (
    id          bigint                  auto_increment      primary key,
    name        varchar(32)             not null,
    base_price  decimal(15,2)           not null
)