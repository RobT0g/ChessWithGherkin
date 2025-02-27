Feature: Testing pawn movement
    Scenario Outline: Pawn first movement to first square
        Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'
        And 'Pawn_Player' has clicked on the 'Pawn' in position '6' '6'
        And 'Pawn_Player' sees the square '5' '6' highlighted in 'green'
        And 'Pawn_Player' sees the square '4' '6' highlighted in 'green'

        When 'Pawn_Player' clicks on the highlighted square '5' '6'

        Then 'Pawn_Player' shold see 'Pawn' move from the square '6' '6' to the square '5' '6'
        And 'Pawn_Player' should see square '5' '6' no longer highlighted
        And 'Pawn_Player' should see square '4' '6' no longer highlighted

    # Scenario Outline: Pawn first movement to second square
    #     Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
    #     And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'
    #     And 'Pawn_Player' clicks on the 'Pawn' in position '6' '6'
    #     And the square '6' '5' is highlighted in 'green'
    #     And the square '6' '4' is highlighted in 'green'

    #     When 'Pawn_Player' clicks on the highlighted square '6' '4'

    #     Then 'Pawn' should move from the square '6' '6' to the square '6' '4'
    #     And square '6' '4' should no longer be highlighted

    # Scenario Outline: Pawn atacks another pawn diagonaly to the left
    #     Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
    #     And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'
    #     And 'Pawn_Player' adds a 'Pawn' in position '5' '5' with color 'Black'
    #     And 'Pawn_Player' clicks on the 'Pawn' in position '6' '6'
    #     And the square '5' '5' is highlighted in 'red'
    #     And the square '6' '5' is highlighted in 'green'
    #     And the square '6' '4' is highlighted in 'green'

    #     When 'Pawn_Player' clicks on the highlighted square '5' '5'

    #     Then 'BlackPawn' in position '5' '5' should be removed from the board
    #     Then 'WhitePawn' should move from the square '6' '6' to the square '5' '5'
    #     And square '5' '5' should no longer be highlighted

    # Scenario Outline: Pawn atacks another pawn diagonaly to the right
    #     Given 'Pawn_Player' has an empty chess board with dimensons '8' by '8'
    #     And 'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'
    #     And 'Pawn_Player' adds a 'Pawn' in position '7' '5' with color 'Black'
    #     And 'Pawn_Player' clicks on the 'Pawn' in position '6' '6'
    #     And the square '7' '5' is highlighted in 'red'
    #     And the square '6' '5' is highlighted in 'green'
    #     And the square '6' '4' is highlighted in 'green'

    #     When 'Pawn_Player' clicks on the highlighted square '7' '5'

    #     Then 'BlackPawn' in position '7' '5' should be removed from the board
    #     Then 'WhitePawn' should move from the square '6' '6' to the square '7' '5'
    #     And square '7' '5' should no longer be highlighted
