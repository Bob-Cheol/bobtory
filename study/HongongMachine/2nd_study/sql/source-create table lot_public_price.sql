create table lot_public_price (
  year varchar(4),
  stdmt varchar(2),
  pnu varchar(19),
  land_seqno numeric,
  sgg_cd varchar(5),
  land_loc_cd varchar(5),
  land_gbn varchar(1),
  bobn varchar(4),
  bubn varchar(4),
  adm_umd_cd varchar(3),
  pnilp numeric,
  jimok varchar(2),
  parea numeric,
  spfc1 varchar(2),
  spfc2 varchar(2),
  land_use varchar(3),
  geo_hl varchar(2),
  geo_form varchar(2),
  road_side varchar(2),
  upload_at timestamp default current_timestamp
) partition by list (substr(pnu,1,2));
create index index_lot_public_price_on_pnu on lot_public_price (pnu);
create table lot_public_price_00 partition of lot_public_price default;
create table lot_public_price_11 partition of lot_public_price for values in ('11');
create table lot_public_price_26 partition of lot_public_price for values in ('26');
create table lot_public_price_27 partition of lot_public_price for values in ('27');
create table lot_public_price_28 partition of lot_public_price for values in ('28');
create table lot_public_price_29 partition of lot_public_price for values in ('29');
create table lot_public_price_30 partition of lot_public_price for values in ('30');
create table lot_public_price_31 partition of lot_public_price for values in ('31');
create table lot_public_price_36 partition of lot_public_price for values in ('36');
create table lot_public_price_41 partition of lot_public_price for values in ('41');
create table lot_public_price_42 partition of lot_public_price for values in ('42');
create table lot_public_price_43 partition of lot_public_price for values in ('43');
create table lot_public_price_44 partition of lot_public_price for values in ('44');
create table lot_public_price_45 partition of lot_public_price for values in ('45');
create table lot_public_price_46 partition of lot_public_price for values in ('46');
create table lot_public_price_47 partition of lot_public_price for values in ('47');
create table lot_public_price_48 partition of lot_public_price for values in ('48');
create table lot_public_price_50 partition of lot_public_price for values in ('50');
