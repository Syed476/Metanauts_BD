package com.test.scala

import com.test.scala.Scala_Occurrences.elemnt_occurrences

import scala.io.Source

object MainObject{
  def main(args:Array[String]){


    val filename = "Shakespeare.txt"
    val fileSource = Source.fromFile(filename)

    for(line<-fileSource.getLines){
      println(line)
    }

    fileSource.close()
  }
}