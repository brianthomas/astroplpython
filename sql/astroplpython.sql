-- initialization SQL script for astroplpython
-- functions

-- we use python 3
create LANGUAGE plpython3u;

-- create measurement type P(f)
create type p_f as (power float8, frequency float8);

-- create measurement type X(t)
create type x_t as (value float8, time float8);

-- next two functions support creation of an
-- aggregate function to gather X(t) measurements
-- from a database table.
create function x_t_accum (t1 x_t[], t2 x_t)
returns x_t[] as
$$
  select array_append($1, $2)::x_t[];
$$ language SQL immutable;

CREATE AGGREGATE x_t_accum (x_t)
(
    sfunc = array_append,
    stype = x_t[],
    initcond = '{}'
);

-- the core "final function" which actually does the
-- calculation of the periodogram 
create or replace FUNCTION calc_lsp (data x_t[])
  RETURNS setof p_f
AS $$

  from astroplpython.data.Timeseries import x_t, strToXTArray
  from astroplpython.proc.LSPeriodogram import LSPeriodogram

  lsp = LSPeriodogram(strToXTArray(data))
  pgram = lsp.pgram()

  return pgram

$$ LANGUAGE plpython3u IMMUTABLE;

-- provides changing setof p_f into p_f[]
-- which is more convenient for bulk runs which
-- insert results from each run on a row in a 
-- results table
create function calc_lsp_arr_p_f(in x_t[])
  returns p_f[]
AS $$
  select array ( select calc_lsp($1) );
$$ language sql immutable;

-- And finally, the actual function for calculation of LSPeriodogram. 
-- in principle, we want an aggregate function.
-- but this is a bad idea, the finalfunc can only take 
-- a single argument, which is of stype
-- OTOH, we might use SD, GD arrays to provide
-- things like f_high, f_over parameters to functions
--
-- see http://www.postgresql.org/docs/9.2/interactive/plpython-sharing.html
-- 
-- which is workable, but 'feels' wrong. Certainly a 
-- violation of the 'functional' approach we want to take
CREATE AGGREGATE lsp (x_t)
(
    sfunc = x_t_accum,
    stype = x_t[],
    finalfunc = calc_lsp_arr_p_f,
    initcond = '{}'
);


