val result = input.map(x => x * x) 
result.persist(StorageLevel.DISK_ONLY) 
println(result.count()) 
println(result.collect().mkString(","))