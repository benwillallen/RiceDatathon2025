from manim import *
import numpy as np


def create_cross_out(vmobject, col="#ff5555", stroke_width=10):
    cross_out1 = Line(start=vmobject.get_corner(UP + LEFT),
                      end=vmobject.get_corner(DOWN + RIGHT), color=col, stroke_width=stroke_width)
    cross_out2 = Line(start=vmobject.get_corner(UP + RIGHT),
                      end=vmobject.get_corner(DOWN + LEFT), color=col, stroke_width=stroke_width)
    return VGroup(cross_out1, cross_out2)


def set_defaults(plane=True):
    Text.set_default(font='Bahnschrift', color="#21201e")
    Paragraph.set_default(font='Bahnschrift', color="#21201e", line_spacing=1)
    SurroundingRectangle.set_default(color="#007991", stroke_width=7, fill_color=WHITE, fill_opacity=0.1, buff=0.2)
    MathTex.set_default(color="#21201e")
    Arrow.set_default(color="#F17105", buff=0.2, max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.3)
    DoubleArrow.set_default(color="#F17105")
    CurvedArrow.set_default(color="#F17105", angle=PI/3)
    CurvedDoubleArrow.set_default(color="#F17105", angle=PI/3)
    Line.set_default(color="#21201e")
    DashedLine.set_default(color="#21201e")
    ArcBetweenPoints.set_default(color="#F17105", angle=PI/3)
    if plane:
        num_background = NumberPlane(x_range=[-10, 20, 1.5], y_range=[-10, 10, 1.5],
                                     background_line_style={"stroke_color": "#21201e", "stroke_width": 10,
                                                            "stroke_opacity": 0.1}).shift(4.5 * UP + 7 * LEFT)
    else:
        num_background = None
    return num_background


def create_tree_diagram(width, height, nodes_list, line_color, stroke_width):
    """
    :param width: total manim width
    :param height: total manim height
    :param nodes_list: list of the number of nodes for each section
    :param line_color: color of lines in diagram
    :param stroke_width: width of lines in diagram
    :return: A manim VGroup of a tree diagram made up of lines
    """
    # Calculate x-values
    x_values = np.linspace(start=width, stop=0, num=len(nodes_list)+1)
    # Calculate y-values
    y_values = []
    last_node_y = np.linspace(start=0, stop=height, num=int(np.prod(nodes_list)))
    y_values.append(last_node_y)
    for node_iter in range(len(nodes_list)-2, -1, -1):
        print("Iteration: ", node_iter)
        window_size = nodes_list[node_iter + 1]
        print("Window Size: ", window_size)
        new_node_y = []
        # Calculate median values for next iteration
        for value in range(int(len(last_node_y)/window_size)):
            print((value+1)*window_size-window_size, ", ", (value+1)*window_size)
            median = np.median(last_node_y[(value+1)*window_size-window_size:(value+1)*window_size])
            print("Median:", median)
            new_node_y.append(median)
        y_values.append(new_node_y)
        last_node_y = new_node_y
    y_values.append([np.median(last_node_y)])
    print(x_values, y_values)
    print(y_values[1])
    # Create lines
    tree_diagram = VGroup()
    for node_iter in range(len(nodes_list)):
        print("Iteration: ", node_iter)
        window_size = nodes_list[-1*node_iter-1]
        print("Window Size: ", window_size)
        column = VGroup()
        for line_num in range(len(y_values[node_iter])):
            print("Line Number: ", line_num)
            start_x = x_values[node_iter+1]
            end_x = x_values[node_iter]
            start_y = y_values[node_iter+1][line_num//window_size]
            end_y = y_values[node_iter][line_num]
            print("Start: ", start_x, start_y, "End: ", end_x, end_y)
            new_line = Line(start=start_x*RIGHT+start_y*UP, end=end_x*RIGHT+end_y*UP, color=line_color,
                            stroke_width=stroke_width)
            column.add(new_line)
        tree_diagram.add(column)
    return tree_diagram