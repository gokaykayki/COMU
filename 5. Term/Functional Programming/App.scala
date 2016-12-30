import scala.collection.mutable.ListBuffer


object App extends App {
  var column:Int = 1
  var n:Int = 5
  
  var list = ListBuffer.fill(n)(ListBuffer.fill(n)(0))
  
  for( i <- 0 until n ){
    list.update(i, list(i).updated(column, 1))
    column += 2
    
    if( column >= n) column=0
  }
  
  list.foreach{
    x =>
      println(x)
  }
}