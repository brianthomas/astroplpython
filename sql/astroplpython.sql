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
-- This function is for accumulation after first 
-- measurement is gathered and x_t[] is started
create or replace function x_t_accum (t1 x_t[], t2 x_t)
returns x_t[] as
$$
  select array_append($1, $2)::x_t[];
$$ language SQL immutable;

-- this gets things started for accumulation of x_t[]
CREATE AGGREGATE x_t_accum (x_t)
(
    sfunc = array_append,
    stype = x_t[],
    initcond = '{}'
);

create or replace function p_f_accum (t1 p_f[], t2 p_f)
returns p_f[] as
$$
  select array_append($1, $2)::p_f[];
$$ language SQL immutable;

-- this gets things started for accumulation of p_f[]
CREATE AGGREGATE p_f_accum (p_f)
(
    sfunc = array_append,
    stype = p_f[],
    initcond = '{}'
);

-- the core "final function" which actually does the
-- calculation of the periodogram 
create or replace FUNCTION calc_lsp (data x_t[], f_low numeric, f_high numeric, f_bins integer)
  RETURNS setof p_f
AS $$

  from astroplpython.data.TimeMeasurement import x_t
  from astroplpython.function.signal.LSPeriodogram import LSPeriodogram
  from astroplpython.exception.ListException import EmptyListException

  # debugging?
  import logging
  import sys
  logging.basicConfig(stream=sys.stderr)
  log = logging.getLogger( "astroplpython.function.signal")
  log.setLevel(logging.DEBUG)

  # calculate based on passed parameters
  pgram = []
  try:
      pgram = LSPeriodogram.calculate(x_t.dbStrToArray(data), f_low, f_high, f_bins)
  except EmptyListException as el:
      log.warn ("calc_lsp was passed an empty list, ignoring");
  except ZeroDivisionError as ze:
      log.warn ("calc_lsp got division by zero, ignoring");
  except ValueError as ve:
      log.warn ("calc_lsp got ValueError, ignoring");

  return pgram

$$ LANGUAGE plpython3u IMMUTABLE;


-- Find the maximum power in a list of p_f[]
--
create or replace FUNCTION max_power (data p_f[])
  RETURNS setof p_f
AS $$

  from astroplpython.data.PowerFrequencyMeasurement import p_f
  from astroplpython.function.statistic.Maximum import Maximum

  import logging
  import sys
  logging.basicConfig(stream=sys.stderr)
  log = logging.getLogger( "astroplpython.function.statistic")

  p_f_list = []
  # calculate based on passed parameters
  try:
     max = Maximum.calculate(p_f.dbStrToArray(data))
     # postgres requires return of an 'iterable object' 
     p_f_list.append(max)
  except ValueError as ve:
     log.warn ("max_power got ValueError, ignoring");
     p_f_list.append(p_f("-1", "-1"))

  return p_f_list

$$ LANGUAGE plpython3u IMMUTABLE;

--
-- EXAMPLE sql using these functions:
--

-- LSP calc
-- select calc_lsp(x_t_accum((mag,hjd)::x_t), 0.4, 0.6, 100) from test where objid = 1;

-- max frequency calc
-- select max_power (p_f_accum(result.p_f)) from (select calc_lsp(x_t_accum((mag,hjd)::x_t), 0.4, 0.6, 100) as p_f from test where objid = 1) as result;

--
--
-- EXPERIMENTAL FUNCTIONS
-- {try to make it more efficient)
--

-- to try to improve the interface for doing multi-argument
-- aggregate functions create special type for collecting function
-- params
create type lsp_input as (
   data x_t,
   f_low numeric,
   f_high numeric,
   f_bins integer
);

-- provides changing setof p_f into p_f[]
-- which is more convenient for bulk runs which
-- insert results from each run on a row in a 
-- results table
create or replace function calc_lsp_arr_p_f(in lsp_input[])
  returns p_f[]
AS $$
  DEFINE
  vals x_t[];
  BEGIN
    for data in $1 
    select array ( select calc_lsp(vals, $2, $3, $4) );
  END;
$$ language sql immutable;

-- next two functions support creation of an
-- aggregate function to gather lsp_input(s)
create or replace function lsp_accum (t1 lsp_input[], t2 lsp_input)
returns lsp_input as
$$
  select array_append($1, $2)::lsp_input[];
$$ language SQL immutable;

-- provides changing setof p_f into p_f[]
-- which is more convenient for bulk runs which
-- insert results from each run on a row in a 
-- results table
create or replace function calc_lsp_arr_p_f(in lsp_input[])
  returns p_f[]
AS $$
  DEFINE
  vals x_t[];
  BEGIN
    for data in $1
    select array ( select calc_lsp(vals, $2, $3, $4) );
  END;
$$ language sql immutable;

-- And finally, the actual function for calculation of LSPeriodogram. 
-- in principle, we want an aggregate function.
-- but this is a bad idea, the finalfunc can only take 
-- a single argument, which is of stype
-- OTOH, we might use SD, GD arrays to provide
-- things like f_high, f_over parameters to functions
--
-- see http://www.postgresql.org/docs/9.3/interactive/plpython-sharing.html
-- 
-- which is workable, but 'feels' wrong. Certainly a 
-- violation of the 'functional' approach we want to take
CREATE AGGREGATE lsp (x_t, numeric, numeric, integer)
(
    sfunc = lsp_accum,
    stype = lsp_input,
    finalfunc = calc_lsp_arr_p_f,
    initcond = '{}'
);


