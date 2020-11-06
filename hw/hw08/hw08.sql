CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size from dogs as a, sizes as b where a.height > b.min 
        and a.height <= b.max ;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name from dogs as a, parents as b, dogs as c 
        where a.name = b.child and b.parent = c.name ORDER BY c.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as senior, b.child as junior from parents as a, 
                                                           parents as b                                 
         where a.parent = b.parent and a.child < b.child ORDER BY senior ASC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT senior || " and " || junior || " are " || a.size || " siblings" from siblings, 
         size_of_dogs as a, size_of_dogs as b where a.size = b.size and a.name = senior and b.name = junior;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper (dogs, stack_height, last_height, n);
  -- Add your INSERT INTOs here
   INSERT INTO stacks_helper SELECT name, height, height, 1 from dogs;
   INSERT INTO stacks_helper SELECT dogs || ", " || name, stack_height + height, height, n + 1 from stacks_helper, dogs where height > last_height;
   INSERT INTO stacks_helper SELECT dogs || ", " || name, stack_height + height, height, n + 1 from stacks_helper, dogs where height > last_height;
   INSERT INTO stacks_helper SELECT dogs || ", " || name, stack_height + height, height, n + 1 from stacks_helper, dogs where height > last_height;
   

CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper where stack_height >= 170 ORDER BY stack_height;

