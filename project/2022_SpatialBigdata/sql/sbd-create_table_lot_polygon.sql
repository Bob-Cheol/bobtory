create table lot_polygon (
  no int,
  pnu varchar(19) primary key,
  address varchar,
  jimok varchar(1),
  created_at date,
  geometry public.geometry(geometry, 5179),
  uploaded_at timestamp default current_timestamp
);
create index index_lot_polygon_on_pnu on lot_polygon (pnu);
create index index_lot_polygon_on_geometry on lot_polygon using GIST(geometry);
