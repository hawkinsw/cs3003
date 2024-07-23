Object subclass: #Rootable
       instanceVariableNames: ''
       classVariableNames: ''
       poolDictionaries:''
       category: 'This is a category!'
!

!Rootable class methodsFor:'determining whether a number is a root of a number'!

is: aRoot rootOf: aNumber
	^ aRoot * aRoot == aNumber
! !

(Rootable is: 5 rootOf: 25) printNl!
(Rootable class methodDictionary) do: [ :value | (value methodCategory) printNl. ]!
