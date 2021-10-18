BEGIN ;
DROP TABLE IF EXISTS film_actor                     ;
DROP TABLE IF EXISTS film_category                  ;
DROP TABLE IF EXISTS customer                       ;
DROP TABLE IF EXISTS actor                          ;
DROP TABLE IF EXISTS category                       ;
DROP TABLE IF EXISTS film                           ;
DROP TABLE IF EXISTS address                        ;
DROP TABLE IF EXISTS city                           ;
DROP TABLE IF EXISTS country                        ;
DROP TABLE IF EXISTS inventory                      ;
DROP TABLE IF EXISTS language                       ;
DROP TABLE IF EXISTS payment                        ;
DROP TABLE IF EXISTS rental                         ;
DROP TABLE IF EXISTS staff                          ;
DROP TABLE IF EXISTS store                          ;

DROP DOMAIN IF EXISTS year                          ;

DROP FUNCTION IF EXISTS film_in_stock               ;
DROP FUNCTION IF EXISTS film_not_in_stock           ;
DROP FUNCTION IF EXISTS get_customer_balance        ;
DROP FUNCTION IF EXISTS inventory_held_by_customer  ;
DROP FUNCTION IF EXISTS inventory_in_stock          ;
DROP FUNCTION IF EXISTS last_day                    ;
DROP FUNCTION IF EXISTS last_updated                ;
DROP FUNCTION IF EXISTS rewards_report              ;
DROP AGGREGATE IF EXISTS group_concat(text) CASCADE ;
DROP FUNCTION IF EXISTS _group_concat               ;

DROP SEQUENCE IF EXISTS customer_customer_id_seq    ;
DROP SEQUENCE IF EXISTS actor_actor_id_seq          ;
DROP SEQUENCE IF EXISTS category_category_id_seq    ;
DROP SEQUENCE IF EXISTS film_film_id_seq            ;
DROP SEQUENCE IF EXISTS address_address_id_seq      ;
DROP SEQUENCE IF EXISTS city_city_id_seq            ;
DROP SEQUENCE IF EXISTS country_country_id_seq      ;
DROP SEQUENCE IF EXISTS inventory_inventory_id_seq  ;
DROP SEQUENCE IF EXISTS language_language_id_seq    ;
DROP SEQUENCE IF EXISTS payment_payment_id_seq      ;
DROP SEQUENCE IF EXISTS rental_rental_id_seq        ;
DROP SEQUENCE IF EXISTS staff_staff_id_seq          ;
DROP SEQUENCE IF EXISTS store_store_id_seq          ;


DROP TYPE IF EXISTS mpaa_rating                     ;

COMMIT ;
