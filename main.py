def count_batteries_by_health(present_capacities):
    # Rated capacity of the new battery
    rated_capacity= 120.0       
    soh_vals=[]
    for i in present_capacities:
        if i<0 or i>rated_capacity:
            continue
         # calculate SoH
        soh=  100 * (i/ rated_capacity)    
        soh_vals.append(soh)
    soh=soh_vals
    # Initialising the battery counts 
    health=0
    exchange=0
    fail=0
    # Classifying all the present capacities based on SoH values
    for i in soh:            
        if i>80.00 :                  
            health+=1
        elif i<=80.00 and i>=65.00:
            exchange+=1
        else:
            fail+=1
    return {
        "healthy": health,
        "exchange": exchange,
        "failed": fail
    }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77,-100,125]
  counts = count_batteries_by_health(present_capacities)
  # Assertions to check correctness
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
#   print(counts["healthy"])     --- healthy batteries count 
#   print(counts["exchange"])    --- exchange batteries count 
#   print(counts["failed"])      --- failed batteries count 
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
