package main

import "fmt"

type Readable interface {
  Read()
}

type Book struct {
  title string
}

func (book Book) Read() {
  fmt.Printf("Reading the book %v\n", book.title)
}

type Internet struct {
  url string
}

func (internet Internet) Read() {
  fmt.Printf("Reading the page %v\n", internet.url)
}

type Vinyl struct {
  album string
}

func WhatAreYouReading(r Readable) {
  r.Read()
}

func main() {
  fmt.Println("Hello, World.")
  internet := Internet{url: "http://google.com"}
  book := Book{title: "Infinite Jest"}
  //album := Vinyl{album: "Gordon"}

  WhatAreYouReading(internet)
  WhatAreYouReading(book)
  //WhatAreYouReading(album)
}

