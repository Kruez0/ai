# Chess AI using Alpha-Beta Pruning

Built a turn-based chess game with artificial intelligence using **Minimax** and **Alpha-Beta Pruning** to optimize decision-making. Gained hands-on experience with adversarial search, game state evaluation, and strategic gameplay development.



## AI Algorithm

The Chess AI uses a combination of **Alpha-Beta Pruning** and the **Negamax Algorithm**, an optimization of Minimax for zero-sum games like chess.

- **Alpha-Beta Pruning** reduces the number of nodes evaluated in the search tree by eliminating branches that cannot influence the final decision.
- **Negamax** simplifies Minimax by assuming the opponent’s best outcome is the negative of your best outcome.


## Evaluation Function

To evaluate board positions, I assigned numeric values to pieces and created a basic positional score table. Example:

```python
rookScores = [
    [0.25, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.25],
    ...
]
```
Professional engines often use different evaluation criteria for the mid-game and end-game. I attempted to implement that, but due to limited research material on positional scores, this version uses a single evaluation approach for the entire game.
<img src="chess4.png" width="400"/>  

## Designs
### - First Design ( Can't differentiate the pawns )
<img src="chess1.png" width="400"/>  

<img src="chess2.png" width="400"/>     

### - Second Design 
<img src="chess3.png" width="600"/>  

<img src="chess3.5.png" width="400"/>    

## Final Chess UI

![alt text](<chez.gif>)

