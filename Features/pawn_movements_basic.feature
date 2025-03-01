Feature: Testing pawn movement
    Scenario Outline: Highlighting Pawn first movement
        Given 'Pawn_Player_2' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player_2' adds a 'Pawn' in position <row> <column> with color 'White'

        When 'Pawn_Player_2' clicks on the 'Pawn' in position <row> <column>

        Then 'Pawn_Player_2' should see square <row> <column> highlighted in 'yellow'
        And 'Pawn_Player_2' should see square <row_move_1> <column> highlighted in 'green'
        And 'Pawn_Player_2' should see square <row_move_2> <column> highlighted in 'green'

    Examples:
        | row | column | row_move_1 | row_move_2 |
        | 6   | 6      | 5          | 4          |
        | 5   | 5      | 4          | 3          |
        | 7   | 3      | 6          | 5          |

    Scenario Outline: Pawn taking the first move
        Given 'Pawn_Player_2' has an empty chess board with dimensons '8' by '8'
        And 'Pawn_Player_2' adds a 'Pawn' in position <row> <column> with color 'White'
        And 'Pawn_Player_2' has clicked on the 'Pawn' in position <row> <column>
        And 'Pawn_Player_2' sees the square <row> <column> highlighted in 'yellow'
        And 'Pawn_Player_2' sees the square <row_move_1> <column> highlighted in 'green'
        And 'Pawn_Player_2' sees the square <row_move_2> <column> highlighted in 'green'

        When 'Pawn_Player_2' clicks on the highlighted square <row_to_move> <column>

        Then 'Pawn_Player_2' shold see 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
        And 'Pawn_Player_2' should see square <row> <column> no longer highlighted
        And 'Pawn_Player_2' should see square <row_move_1> <column> no longer highlighted
        And 'Pawn_Player_2' should see square <row_move_2> <column> no longer highlighted

    Examples:
        | row | column | row_move_1 | row_move_2 | row_to_move |
        | 6   | 6      | 5          | 4          | 5           |
        | 6   | 6      | 5          | 4          | 4           |
        | 5   | 5      | 4          | 3          | 4           |
        | 5   | 5      | 4          | 3          | 3           |
        | 7   | 3      | 6          | 5          | 6           |
        | 7   | 3      | 6          | 5          | 5           |

# Scenario: Pawn atacks another pawn
#     Given 'Pawn_Player_2' has an empty chess board with dimensons '8' by '8'
#     And 'Pawn_Player_2' adds a 'Pawn' in position '6' '6' with color 'White'
#     And 'Pawn_Player_2' adds a 'Pawn' in position '5' '5' with color 'Black'
#     And 'Pawn_Player_2' clicks on the 'Pawn' in position '6' '6'
#     And the square '5' '5' is highlighted in 'red'
#     And the square '6' '5' is highlighted in 'green'
#     And the square '6' '4' is highlighted in 'green'

#     When 'Pawn_Player_2' clicks on the highlighted square '5' '5'

#     Then 'BlackPawn' in position '5' '5' should be removed from the board
#     Then 'WhitePawn' should move from the square '6' '6' to the square '5' '5'
#     And square '5' '5' should no longer be highlighted

