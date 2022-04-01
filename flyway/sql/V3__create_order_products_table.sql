create table template.order_products (
    id          bigint                  auto_increment primary key,
    order_id    bigint                  not null,
    product_id  bigint                  not null,
    price       decimal(15,2)           not null,

    constraint order_product_order_id_fk
        foreign key (order_id) references template.orders(id),

    constraint order_product_product_id_fk
        foreign key (product_id) references template.products(id)
)