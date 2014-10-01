dataset_locations = {}
datacenters = {}
no_data_centers = int(raw_input())

for i in range(1, no_data_centers+1):
    datacenters[i] = {}
    line = raw_input().split()
    for data_set in line[1:]:
        dataset_locations[int(data_set)] = i
        datacenters[i][int(data_set)] = True

for data_centre in datacenters.keys():
    for data_set in range(1, 999999):
        if data_set in datacenters[data_centre]:
            continue
        if data_set in dataset_locations:
            print "%s %s %s" % (data_set, dataset_locations[data_set], data_centre)
print "done"
