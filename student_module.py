def need_money(stipend, costs):
    total_stipend = stipend * 10
    total_costs = 0
    current_costs = costs
    for _ in range(10):
        total_costs += current_costs
        current_costs *= 1.05
    return total_costs - total_stipend
