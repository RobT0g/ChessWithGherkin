Feature: Testing Knight movements
    Scenario Outline: Knight Movements
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Knight' in position <row> <column> with color <piece_color>
        And it is <piece_color> turn to play
        And I have clicked on the <piece_color> 'Knight' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'

        When I click on the square <row_to_move> <column_to_move>

        Then I shold see the <piece_color> 'Knight' move from the square <row> <column> to the square <row_to_move> <column_to_move>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | piece_color | green_squares                                                  | row_to_move | column_to_move |
            | 7   | 1      | White       | (5, 0), (5, 2), (6, 3)                                         | 5           | 0              |
            | 7   | 1      | White       | (5, 0), (5, 2), (6, 3)                                         | 5           | 2              |
            | 7   | 1      | White       | (5, 0), (5, 2), (6, 3)                                         | 6           | 3              |
            | 7   | 6      | White       | (5, 5), (5, 7), (6, 4)                                         | 5           | 5              |
            | 7   | 6      | White       | (5, 5), (5, 7), (6, 4)                                         | 5           | 7              |
            | 7   | 6      | White       | (5, 5), (5, 7), (6, 4)                                         | 6           | 4              |
            | 0   | 1      | Black       | (2, 0), (2, 2), (1, 3)                                         | 2           | 0              |
            | 0   | 1      | Black       | (2, 0), (2, 2), (1, 3)                                         | 2           | 2              |
            | 0   | 1      | Black       | (2, 0), (2, 2), (1, 3)                                         | 1           | 3              |
            | 0   | 6      | Black       | (2, 5), (2, 7), (1, 4)                                         | 2           | 5              |
            | 0   | 6      | Black       | (2, 5), (2, 7), (1, 4)                                         | 2           | 7              |
            | 0   | 6      | Black       | (2, 5), (2, 7), (1, 4)                                         | 1           | 4              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 3           | 4              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 3           | 6              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 4           | 3              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 4           | 7              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 6           | 3              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 6           | 7              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 7           | 4              |
            | 5   | 5      | White       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 7           | 6              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 3           | 4              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 3           | 6              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 4           | 3              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 4           | 7              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 6           | 3              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 6           | 7              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 7           | 4              |
            | 5   | 5      | Black       | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | 7           | 6              |
