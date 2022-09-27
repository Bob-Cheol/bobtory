create table dem_point (
  id int,
  value numeric,
  geometry public.geometry(geometry,5174),
  uploaded_at timestamp default current_timestamp
);
create index index_dem_point_on_geometry on dem_point (geometry);
