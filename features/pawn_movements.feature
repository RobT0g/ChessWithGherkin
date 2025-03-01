Feature: Testing pawn movements
    Scenario Outline: White Pawn taking the first move
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Pawn' in position <row> <column> with color 'White'
        And it is 'White' turn to play
        And I have clicked on the 'White' 'Pawn' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column>

        Then I shold see the 'White' 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | green_squares  | row_to_move |
            | 6   | 6      | (5, 6), (4, 6) | 5           |
            | 6   | 6      | (5, 6), (4, 6) | 4           |
            | 5   | 5      | (4, 5), (3, 5) | 4           |
            | 5   | 5      | (4, 5), (3, 5) | 3           |
            | 7   | 3      | (6, 3), (5, 3) | 6           |
            | 7   | 3      | (6, 3), (5, 3) | 5           |

    Scenario Outline: White Pawn taking the second move
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Pawn' in position <row> <column> with color 'White'
        And the 'White' 'Pawn' in position <row> <column> has already moved
        And it is 'White' turn to play
        And I have clicked on the 'White' 'Pawn' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column>

        Then I shold see the 'White' 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | green_squares | row_to_move |
            | 6   | 6      | (5, 6)        | 5           |
            | 5   | 5      | (4, 5)        | 4           |
            | 7   | 3      | (6, 3)        | 6           |

    Scenario Outline: Black Pawn taking the first move
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Pawn' in position <row> <column> with color 'Black'
        And it is 'Black' turn to play
        And I have clicked on the 'Black' 'Pawn' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column>

        Then I shold see the 'Black' 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | green_squares  | row_to_move |
            | 2   | 6      | (3, 6), (4, 6) | 3           |
            | 2   | 6      | (3, 6), (4, 6) | 4           |
            | 3   | 5      | (4, 5), (5, 5) | 4           |
            | 3   | 5      | (4, 5), (5, 5) | 5           |
            | 1   | 3      | (2, 3), (3, 3) | 2           |
            | 1   | 3      | (2, 3), (3, 3) | 3           |

    Scenario Outline: Black Pawn taking the second move
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Pawn' in position <row> <column> with color 'Black'
        And the 'Black' 'Pawn' in position <row> <column> has already moved
        And it is 'Black' turn to play
        And I have clicked on the 'Black' 'Pawn' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column>

        Then I shold see the 'Black' 'Pawn' move from the square <row> <column> to the square <row_to_move> <column>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | green_squares | row_to_move |
            | 2   | 6      | (3, 6)        | 3           |
            | 3   | 5      | (4, 5)        | 4           |
            | 1   | 3      | (2, 3)        | 2           |