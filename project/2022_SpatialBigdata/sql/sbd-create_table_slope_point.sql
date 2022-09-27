create table slope_point (
  id int,
  value numeric,
  geometry public.geometry(geometry, 5179),
  uploaded_at timestamp default current_timestamp
);
create index index_slope_point_on_geometry on slope_point (geometry);
