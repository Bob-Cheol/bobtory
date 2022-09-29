create table hexagon_unit (
  id varchar,
  geometry public.geometry(geometry,5179),
  uploaded_at timestamp default current_timestamp
);
CREATE INDEX index_hexagon_unit_geometry ON hexagon_unit using gist(geometry);
