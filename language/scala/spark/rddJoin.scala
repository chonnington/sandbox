
case class Store(isbn: String)

val storeAddress = {
    (Store("Ritual"), "1026 Valencia St"), 
    (Store("Philz"), "748 Van Ness Ave"), 
    (Store("Philz"), "3101 24th St"), 
    (Store("Starbucks"), "Seattle")}

val storeRating = {
    (Store("Ritual"), 4.9), 
    (Store("Philz"), 4.8))}

val storeAddress.join(storeRating) == { 
    (Store("Ritual"), ("1026 Valencia St", 4.9)), 
    (Store("Philz"), ("748 Van Ness Ave", 4.8)), 
    (Store("Philz"), ("3101 24th St", 4.8))}

val storeAddress.leftOuterJoin(storeRating) == {
    (Store("Ritual"), ("1026 Valencia St",Some(4.9))),
    (Store("Starbucks"), ("Seattle",None)), 
    (Store("Philz"), ("748 Van Ness Ave",Some(4.8))), 
    (Store("Philz"), ("3101 24th St",Some(4.8)))}

val storeAddress.rightOuterJoin(storeRating) == {
    (Store("Ritual"), (Some("1026 Valencia St"),4.9)), 
    (Store("Philz"), (Some("748 Van Ness Ave"),4.8)),
    (Store("Philz"), (Some("3101 24th St"),4.8))}