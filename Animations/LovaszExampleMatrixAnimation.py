from manim import *

config.background_color = WHITE
config.transparent = True
config.pixel_width = 1920
config.frame_width = 16
config.pixel_height = 1440
config.frame_height = 12

M_example = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 01
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 02
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 03
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 04
             [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 05
             [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 06
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 07
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 08
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 09
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 10
             [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 11
             [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # 12
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 13
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 14
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 15
             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 16
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 17
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # 18
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 19
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 20
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # 21
             ]

M_columns = [["f_1", "f_2", "f_3", "f_4", "f_5", "f_6", "f_7", "f_8", "f_9", "f_{10}"]]
Column_Lables = Matrix(M_columns, left_bracket="|", right_bracket="|")
Column_Lables.set_color(GREY_D)
Column_Lables.get_brackets()[0].set_color(WHITE)
Column_Lables.get_brackets()[1].set_color(WHITE)
Column_Lables.get_brackets()[0].set_fill(WHITE, opacity=0)
Column_Lables.get_brackets()[1].set_fill(WHITE, opacity=0)
Column_Lables.get_brackets()[0].set_stroke(PINK, opacity=0)
Column_Lables.get_brackets()[1].set_stroke(PINK, opacity=0)

M_rows = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
          [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21]
          ]
# M_rows_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Row_Labels = Matrix(M_rows, left_bracket="|", right_bracket="|")
Row_Labels.set_color(GREY_D)
Row_Labels.get_brackets()[0].set_color(WHITE)
Row_Labels.get_brackets()[1].set_color(WHITE)
Row_Labels.get_brackets()[0].set_fill(WHITE, opacity=0)
Row_Labels.get_brackets()[1].set_fill(WHITE, opacity=0)
Row_Labels.get_brackets()[0].set_stroke(PINK, opacity=0)
Row_Labels.get_brackets()[1].set_stroke(PINK, opacity=0)

M_simplified_estr = [[1, "", "", "", 1, "", "", "", "", ""],  # 01
                     [1, "", "", "", 1, "", "", "", "", ""],  # 02
                     [1, "", "", "", 1, "", "", "", "", ""],  # 03
                     [1, 1, "", "", "", "", "", "", "", ""],  # 04
                     ["", 1, "", "", 1, "", "", "", "", ""],  # 05
                     ["", 1, 1, "", "", "", "", "", "", ""],  # 06
                     ["", "", "", "", 1, "", "", "", "", ""],  # 07
                     ["", "", 1, 1, "", "", "", "", "", ""],  # 08
                     ["", "", 1, 1, "", "", "", "", "", ""],  # 09
                     ["", "", "", "", 1, "", "", "", "", ""],  # 10
                     ["", "", "", 1, "", 1, "", "", "", ""],  # 11
                     ["", "", 1, "", 1, "", 1, 1, "", ""],  # 12
                     ["", "", "", "", "", 1, "", 1, "", ""],  # 13
                     ["", "", "", "", "", 1, "", "", "", ""],  # 14
                     ["", "", "", "", "", 1, "", 1, "", ""],  # 15
                     ["", "", "", "", "", 1, "", "", 1, ""],  # 16
                     ["", "", "", "", "", "", "", 1, "", ""],  # 17
                     ["", "", "", "", "", "", "", 1, 1, 1],  # 18
                     ["", "", "", "", "", "", "", "", "", 1],  # 19
                     ["", "", "", "", "", "", "", "", "", 1],  # 20
                     ["", "", "", "", "", "", 1, "", "", 1],  # 21
                     ]

M_simplified = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 01
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 02
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 03
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 04
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 05
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 06
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 07
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 08
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 09
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 10
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 11
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # 12
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 13
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 14
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 15
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 16
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 17
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # 18
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 19
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 20
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # 21
                ]

M = Matrix(M_simplified, left_bracket="|", right_bracket="|", v_buff=.8)
M.set_color(BLACK)

scene_scale = .5


def white_zeros(A):
    for i in range(len(M_example)):
        for j in range(len(M_example[0])):
            if M_example[i][j] == 0:
                A.get_columns()[j][i].set_color(WHITE)
                A.get_columns()[j][i].set_fill(WHITE, opacity=0)


class ExampleMatrix(Scene):
    def construct(self):
        white_zeros(M)
        covering = [4, 5, 9, 2, 0, 3, 7]
        k = 7       # include the first k edges in the render
        M.scale(scene_scale)
        Row_Labels.scale(scene_scale)
        Column_Lables.scale(scene_scale)
        Row_Labels.to_corner(LEFT + DOWN)
        M.next_to(Row_Labels, RIGHT)
        Column_Lables.next_to(M, UP)
        for c in covering[:k]:
            mark_row_label(get_covered_rows(c))
            mark_column_label(c)
            self.add(Column_Lables)
            self.add(Row_Labels)
        mark_column(covering[k - 1])
        mark_column(covering[k - 2])
        mark_column(covering[k - 3])
        graph_image = ImageMobject("../Presentation/Images/Matheson/Matheson_16.png")
        graph_image.scale(.725)
        graph_image.to_edge(RIGHT, buff=.7)
        self.add(graph_image)
        self.add(M)


def get_covered_rows(column):
    marked = list()
    for i in range(len(M_example)):
        if M_example[i][column] == 1:
            marked.append(i)
    return marked


def mark_row_label(rows):
    for i in rows:
        Row_Labels.add(SurroundingRectangle(Row_Labels.get_rows()[i],
                                            color=DARK_BLUE,
                                            stroke_opacity=0,
                                            fill_opacity=.4,
                                            corner_radius=.1,
                                            buff=.1))


def mark_column_label(i):
    Column_Lables.add(SurroundingRectangle(Column_Lables.get_columns()[i],
                                           color=DARK_BLUE,
                                           stroke_opacity=0,
                                           fill_opacity=.4,
                                           corner_radius=.1,
                                           buff=.1))


def mark_column(i):
    M.add(SurroundingRectangle(M.get_columns()[i],
                               color=DARK_BLUE,
                               stroke_opacity=0,
                               fill_opacity=.4,
                               corner_radius=.1,
                               buff=.1))
