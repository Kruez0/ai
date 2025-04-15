# Chess using Alpha Beta Pruning
Built a turn-based chess with artificial Intelligence using minmax and alpha-beta pruning to optimize decision making, practiced  search algorithms and game strategy evaluation.
## Alpha Beta Pruning
Alpha-Beta pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes evaluated in the search tree by eliminating branches that cannot influence the final decision.The Chess AI uses a combination of Alpha-Beta pruning and the Negamax algorithm to efficiently search through possible moves and select the best one. Negamax Algorithm is a variant of Minimax optimized for zero-sum games like chess.

In this project,I tried to assign numbers for each pieces. 
```
rookScores = [
    [0.25, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.25],
    ....]
```

There should be a middle game evaluation and an end game evaluation. So, for example the positional scores for each pieces should be different according to what game evaluation is it in. I tried to find papers that holds any chess positional numbers but i didnt find any. That is why for this project I only did one evaluation of positional numbers for the whole game.
<img src="chess4.png" width="400"/>  

## Designs
### - First Design ( Can't differentiate the pawns )
<img src="chess1.png" width="400"/>  

<img src="chess2.png" width="400"/>     

### - Second Design 
<img src="chess3.png" width="600"/>  

<img src="chess3.5.png" width="400"/>    

### Final results
![alt text](<chez.gif>)

