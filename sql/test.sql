
-- hello function for testing import and performance
CREATE or replace FUNCTION hello (name varchar)
  RETURNS varchar
AS $$
  from astroplpython.Greeting import Greeting
  return Greeting.hello(name)
$$ LANGUAGE plpython3u;

-- hello function for testing import and performance
-- test "inline" from 10 tests or so of each 
-- it appears to be on average 0.01 upto 0.02 ms 
-- faster than the import approach
CREATE or replace FUNCTION helloi (name varchar)
  RETURNS varchar
AS $$

  ''' module-level function '''
  def hello (name):
      return "Hello "+name

  return hello(name)
$$ LANGUAGE plpython3u;

-- testing array functionality with special
-- data type, matched by python data class
CREATE or replace FUNCTION pyarrtoarr (a my_type[])
  RETURNS setof my_type
AS $$
  class my_type:

    def __init__ (self, v):
       v = v.replace("(","")
       v = v.replace(")","")
       inv = v.split(",")
       self.val1 = inv[0]
       self.val2 = inv[1] 

  ret = []
  for v in a: 
     ret.append(my_type(v))
  return ret
$$ LANGUAGE plpython3u;


