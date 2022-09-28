create table expected_flooding_zone (
  zone_id int,
  level varchar(1),
  level_description varchar,
  geometry public.geometry(geometry, 5179),
  uploaded_at timestamp default current_timestamp
);
