create table building_floor (
  pnu varchar(19),
  building_pk varchar(33),
  address varchar,
  road_address varchar,
  building_name varchar,
  dong_name varchar,
  floor_type_code varchar,
  floor_type_name varchar,
  floor_no numeric,
  floor_no_name varchar,
  structure_code varchar(2),
  structure_name varchar,
  structure_detail varchar,
  use_code varchar(5),
  use_name varchar,
  use_detail varchar,
  area numeric,
  main_sub_type varchar,
  is_excepted_area boolean,
  created_date varchar(8),
  uploaded_at timestamp default current_timestamp
);
create index index_building_floor_on_pnu on building_floor (pnu);
create index index_building_floor_on_use_code on building_floor (use_code);
