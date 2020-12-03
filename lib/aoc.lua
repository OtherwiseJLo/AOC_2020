function aoc_input(filename)
  local input_vals = {}
  for val in io.open(filename, "r") do
    table.insert(input_vals, val)
  end
  return input_vals
end

