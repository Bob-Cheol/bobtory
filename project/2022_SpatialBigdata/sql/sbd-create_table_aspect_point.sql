create table aspect_point (
  id int,
  value numeric,
  geometry public.geometry(geometry, 5179),
  uploaded_at timestamp default current_timestamp
);
create index index_aspect_point_on_geometry on aspect_point (geometry);
