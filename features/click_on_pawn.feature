Feature: Testing pawn movement by clicking on it
    Scenario: Highlighting Pawn first movement
        Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'

        When 'Pawn_Player' clicks on the 'Pawn' in position '6' '6'

        Then 'Pawn_Player' should see square '6' '5' highlighted in 'green'
        And 'Pawn_Player' should see square '6' '4' highlighted in 'green'