-- set @number = 0; 
-- select repeat('* ', @number := @number + 1) 
--     from information_schema.tables
--     limit 20;
    
-- with recursive pattern as(
--         select 1 as row_num 
--         union all 
--         select row_num + 1 from pattern where row_num<20
-- ) 
-- select repeat('* ',row_num) as pattern_row from pattern;

with recursive pattern as (
    select 1 as row_num
    union all
    select row_num + 1 from pattern where row_num < 20
)
select * from pattern