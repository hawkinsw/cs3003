permutation([], []).
permutation(L, [X|Xs]) :- 
  append(LL, [X|LR], L),
  append(LL, LR, LWithoutX),
  permutation(LWithoutX, Xs).

% (a) permutation([1,2], L)
% Round 1:
% LL = [] <- (3)
% X = 1
% LR = [2]
% LWithoutX = [2]
% Now, the predicate being executed is
  % (b) permutation([2], Xs)
  % Round 1:
  % LL = [] <- (2)
  % X = 2
  % LR = []
  % LWithoutX = []
  % Now, the predicate being executed is
    % (c) permutation([], Xs)
    % Xs unifies with []
    % So, we jump back to (b)  <- (1)
  % Xs = []
  % [X|Xs] = [2]
  % So, we jump back to (a)
% Xs = [2]
% [X|Xs] = [1,2]
% Where is our most recent choice point?
% (1)
%     % (c) permutation([], Xs)
%     % Skip the basic rule. Hit the next one.
%     % permutation([], Xs).
%     % But we cannot do that append, so we fail!
% Now, where is our most recent choice point?
% (2)
%   LL = [2]
%   X = !!
%   LR = !!
%   So we fail!
% Now, where is our most recent choice point?
% (3)
% LL = [1]
% X = 2
% LR = []
% LWithoutX = [1]
%
% I stopped here ...
