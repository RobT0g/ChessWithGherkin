Feature: Testing pawn movement by clicking on it
    Scenario: Highlighting Pawn first movement
        Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'

        When 'Pawn_Player' clicks on the 'Pawn' in position '6' '6'

        Then 'Pawn_Player' should see square '6' '6' highlighted in 'yellow'
        And 'Pawn_Player' should see square '5' '6' highlighted in 'green'
        And 'Pawn_Player' should see square '4' '6' highlighted in 'green'

    Scenario: Pawn first movement to first square
        Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'
        And 'Pawn_Player' has clicked on the 'Pawn' in position '6' '6'
        And 'Pawn_Player' sees the square '6' '6' highlighted in 'yellow'
        And 'Pawn_Player' sees the square '5' '6' highlighted in 'green'
        And 'Pawn_Player' sees the square '4' '6' highlighted in 'green'

        When 'Pawn_Player' clicks on the highlighted square '5' '6'

        Then 'Pawn_Player' shold see 'Pawn' move from the square '6' '6' to the square '5' '6'
        And 'Pawn_Player' should see square '5' '6' no longer highlighted
        And 'Pawn_Player' should see square '5' '6' no longer highlighted
        And 'Pawn_Player' should see square '4' '6' no longer highlighted
