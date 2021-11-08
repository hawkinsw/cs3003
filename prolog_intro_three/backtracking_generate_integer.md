generate_integer(0). => Generate 0.
generate_integer(X) :- generate_integer(Y), X is Y + 1.
                       generate_integer(0) => Generate 0.
                     => Generate 1.
                       generate_integer(X) :- generate_integer(Y), X is Y + 1.
                                              generate_integer(0) => Generate 0
                                           => Generate 1
                     => Generate 2.
                                              generate_integer(X) :- generate_integer(Y), X is Y + 1.
                                                                     generate_integer(0). => Generate 0
                                                                  => Generate 1
                                           => Generate 2
                     => Generate 3.
                                                                     generate_integer(X) :- generate_integer(Y), X is Y + 1.
                                                                                            generate_integer(0). => Generate 0
                                                                                          => Generate 1
                                                                  => Generate 2
                                           => Generate 3
                     => Generate 4.

