import math

REQUESTS_PER_HEAVY_PAGE = 66
REQUESTS_PER_OPTIMIZED_PAGE = 25
BYTES_PER_HEAVY_PAGE = 8600000.0
BYTES_PER_OPTIMIZED_PAGE = 1000000.0

def calculate_bandwidth_cost(first_page_loads, page_load_bytes, requests_per_page):
	total_gigabytes = math.ceil((first_page_loads * page_load_bytes) / 1000000000.0)
	total_requests = first_page_loads * requests_per_page
	requests_rate = 0.0075 # per 10K requests.
	bandwidth_rate = 0.12 # per GB
	total_cost = 0.0
	total_cost += math.ceil(total_requests / 10000.0) * requests_rate
	if total_gigabytes <= 10000.0: # 10TB
		total_cost += total_gigabytes * bandwidth_rate
	else:
		total_cost += 10000.0 * bandwidth_rate
		bandwidth_rate = 0.08 # per GB
		total_cost += (total_gigabytes - 10000.0) * bandwidth_rate
	return total_cost

result = {
	"first_page_loads": [],
	"heavy_cost": [],
	"optimized_cost": [],
}
for first_page_loads in xrange(0, 10000001, 1000000):
	heavy_cost = calculate_bandwidth_cost(first_page_loads, BYTES_PER_HEAVY_PAGE, REQUESTS_PER_HEAVY_PAGE)
	optimized_cost = calculate_bandwidth_cost(first_page_loads, BYTES_PER_OPTIMIZED_PAGE, REQUESTS_PER_OPTIMIZED_PAGE)

	result["first_page_loads"].append("%d" % first_page_loads)
	result["heavy_cost"].append("%0.2f" % heavy_cost)
	result["optimized_cost"].append("%0.2f" % optimized_cost)

print ",".join(result["first_page_loads"])
print ",".join(result["heavy_cost"])
print ",".join(result["optimized_cost"])
