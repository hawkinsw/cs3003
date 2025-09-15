#/bin/bash

function greet {
  echo ${what_to_say}
}

function spanish {
  local what_to_say
  what_to_say="hola"
  greet;
}

function french {
  local what_to_say
  what_to_say="bonjour"
  greet;
}

what_to_say="Hello"
function main {
  spanish;
  french;
  greet
}

main
