Feature: Testing Rook movements
    Scenario Outline: Rook Movements
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Rook' in position <row> <column> with color <piece_color>
        And it is <piece_color> turn to play
        And I have clicked on the <piece_color> 'Rook' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column_to_move>

        Then I shold see the <piece_color> 'Rook' move from the square <row> <column> to the square <row_to_move> <column_to_move>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | piece_color | row_to_move | column_to_move | green_squares                |