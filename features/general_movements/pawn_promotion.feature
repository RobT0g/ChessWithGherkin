Feature: Pawn gets promotted
    # Scenario Outline: Pawn reaches the last enemy row
    #     Given I have an empty chess board with dimensons '8' by '8'
    #     And I add a 'Pawn' in position <row> <column> with color <piece_color>
    #     And the <piece_color> 'Pawn' in position <row> <column> has already moved
    #     And it is <piece_color> turn to play
    #     And I have clicked on the <piece_color> 'Pawn' in position <row> <column>
    #     And I see the square <row> <column> highlighted in 'yellow'
    #     And I see all the squares in the list <green_squares> highlighted in 'green'

    #     When I click on the square <row_to_move> <column>

    #     Then I shold see the <piece_color> 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
    #     And there should not be any squares highlighted in any color
    #     And I should get prompted with an option to choose which piece to promote the <piece_color> 'Pawn' on square <row_to_move> <column> to

    #     Examples:
    #         | row | column | green_squares | row_to_move | piece_color |
    #         | 1   | 0      | (0, 0)        | 0           | White       |
    #         | 1   | 1      | (0, 1)        | 0           | White       |
    #         | 1   | 2      | (0, 2)        | 0           | White       |
    #         | 1   | 3      | (0, 3)        | 0           | White       |
    #         | 1   | 4      | (0, 4)        | 0           | White       |
    #         | 1   | 5      | (0, 5)        | 0           | White       |
    #         | 1   | 6      | (0, 6)        | 0           | White       |
    #         | 1   | 7      | (0, 7)        | 0           | White       |
    #         | 6   | 0      | (7, 0)        | 7           | Black       |
    #         | 6   | 1      | (7, 1)        | 7           | Black       |
    #         | 6   | 2      | (7, 2)        | 7           | Black       |
    #         | 6   | 3      | (7, 3)        | 7           | Black       |
    #         | 6   | 4      | (7, 4)        | 7           | Black       |
    #         | 6   | 5      | (7, 5)        | 7           | Black       |
    #         | 6   | 6      | (7, 6)        | 7           | Black       |
    #         | 6   | 7      | (7, 7)        | 7           | Black       |


    Scenario Outline: Picking a promotion piece
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Pawn' in position <row> <column> with color <piece_color>
        And the <piece_color> 'Pawn' in position <row> <column> has already moved
        And it is <piece_color> turn to play
        And I have clicked on the <piece_color> 'Pawn' in position <row> <column>
        And I click on the square <row_to_move> <column>
        And I see the <piece_color> 'Pawn' in position <row_to_move> <column>
        And I get prompted with an option to choose which piece to promote the <piece_color> 'Pawn' on square <row_to_move> <column> to

        When I choose to promote the pawn to a <promotion_piece>

        Then I should see a <piece_color> <promotion_piece> on the square <row_to_move> <column>
        And there should not be any squares highlighted in any color
        And it should no longer be <piece_color> turn to play

        Examples:
            | row | column | row_to_move | piece_color | promotion_piece |
            | 1   | 0      | 0           | White       | Queen           |
            | 1   | 0      | 0           | White       | Rook            |
            | 1   | 0      | 0           | White       | Bishop          |
            | 1   | 0      | 0           | White       | Knight          |
            | 6   | 0      | 7           | Black       | Queen           |
            | 6   | 1      | 7           | Black       | Rook            |
            | 6   | 2      | 7           | Black       | Bishop          |
            | 6   | 3      | 7           | Black       | Knight          |