local expense_report = io.open("input", "r")
local expenses = {}

for line in expense_report:lines() do
  table.insert(expenses, tonumber(line));
end


function Method1(Expenses)
  local total = 2020
  local complement = nil
  local history = {}
  local current = 0

  for _, expense in ipairs(Expenses)  do
    current = history[expense]

    if (current == nil) then
      complement = total - expense
      history[complement] = expense
    else
      return expense*current
    end

  end

end

print(Method1(expenses))
