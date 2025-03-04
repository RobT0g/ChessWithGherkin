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

    Scenario Outline: Knight attacking another Knight
        Given I have an empty chess board with dimensons '8' by '8'
        And I add a 'Knight' in position <row> <column> with color <attacking>
        And I add a 'Knight' in position <att_row> <att_col> with color <attacked>
        And it is <attacking> turn to play
        And I have clicked on the <attacking> 'Knight' in position <row> <column>
        And I see the square <row> <column> highlighted in 'yellow'
        And I see all the squares in the list <green_squares> highlighted in 'green'
        And I see all the squares in the list <red_squares> highlighted in 'red'

        When I click on the square <att_row> <att_col>

        Then I shold see the <attacking> 'Knight' move from the square <row> <column> to the square <att_row> <att_col>
        And I shold see the <attacked> 'Knight' removed from the square <att_row> <att_col>
        And there should not be any squares highlighted in any color

        Examples:
            | row | column | attacking | att_row | att_col | attacked | green_squares                                          | red_squares |
            | 7   | 1      | White     | 5       | 0       | Black    | (5, 2), (6, 3)                                         | (5, 0)      |
            | 7   | 1      | White     | 5       | 2       | Black    | (5, 0), (6, 3)                                         | (5, 2)      |
            | 7   | 1      | White     | 6       | 3       | Black    | (5, 0), (5, 2)                                         | (6, 3)      |
            | 7   | 6      | White     | 5       | 5       | Black    | (5, 7), (6, 4)                                         | (5, 5)      |
            | 7   | 6      | White     | 5       | 7       | Black    | (5, 5), (6, 4)                                         | (5, 7)      |
            | 7   | 6      | White     | 6       | 4       | Black    | (5, 5), (5, 7)                                         | (6, 4)      |
            | 0   | 1      | Black     | 2       | 0       | White    | (2, 2), (1, 3)                                         | (2, 0)      |
            | 0   | 1      | Black     | 2       | 2       | White    | (2, 0), (1, 3)                                         | (2, 2)      |
            | 0   | 1      | Black     | 1       | 3       | White    | (2, 0), (2, 2)                                         | (1, 3)      |
            | 0   | 6      | Black     | 2       | 5       | White    | (2, 7), (1, 4)                                         | (2, 5)      |
            | 0   | 6      | Black     | 2       | 7       | White    | (2, 5), (1, 4)                                         | (2, 7)      |
            | 0   | 6      | Black     | 1       | 4       | White    | (2, 5), (2, 7)                                         | (1, 4)      |
            | 5   | 5      | White     | 3       | 4       | Black    | (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (3, 4)      |
            | 5   | 5      | White     | 3       | 6       | Black    | (3, 4), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (3, 6)      |
            | 5   | 5      | White     | 4       | 3       | Black    | (3, 4), (3, 6), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (4, 3)      |
            | 5   | 5      | White     | 4       | 7       | Black    | (3, 4), (3, 6), (4, 3), (6, 3), (6, 7), (7, 4), (7, 6) | (4, 7)      |
            | 5   | 5      | White     | 6       | 3       | Black    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 7), (7, 4), (7, 6) | (6, 3)      |
            | 5   | 5      | White     | 6       | 7       | Black    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (7, 4), (7, 6) | (6, 7)      |
            | 5   | 5      | White     | 7       | 4       | Black    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 6) | (7, 4)      |
            | 5   | 5      | White     | 7       | 6       | Black    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4) | (7, 6)      |
            | 5   | 5      | Black     | 3       | 4       | White    | (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (3, 4)      |
            | 5   | 5      | Black     | 3       | 6       | White    | (3, 4), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (3, 6)      |
            | 5   | 5      | Black     | 4       | 3       | White    | (3, 4), (3, 6), (4, 7), (6, 3), (6, 7), (7, 4), (7, 6) | (4, 3)      |
            | 5   | 5      | Black     | 4       | 7       | White    | (3, 4), (3, 6), (4, 3), (6, 3), (6, 7), (7, 4), (7, 6) | (4, 7)      |
            | 5   | 5      | Black     | 6       | 3       | White    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 7), (7, 4), (7, 6) | (6, 3)      |
            | 5   | 5      | Black     | 6       | 7       | White    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (7, 4), (7, 6) | (6, 7)      |
            | 5   | 5      | Black     | 7       | 4       | White    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 6) | (7, 4)      |
            | 5   | 5      | Black     | 7       | 6       | White    | (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 4) | (7, 6)      |


