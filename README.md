# Farkle cli - Readme


# Game flow

The user has 10 rounds to beat a highscore
- User rolls dice
  - Game shows available rules that match
    - if no rules match, round is over and no points are added
  - User Selects rule
  - Dice applied in rule are frozen
  - User chooses to roll again or finish round
    - Round finish 
        - Tabulate points
        - Start over, increment round
    - Roll again
