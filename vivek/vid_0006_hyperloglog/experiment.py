from manimlib.imports import *

class ThetaVsTAxes(Axes):
    CONFIG = {
        "number_line_config": {
            "color": "#EEEEEE",
            "stroke_width": 2,
            "include_tip": False,
        },
        "graph_style": {
            "stroke_color": GREEN,
            "stroke_width": 3,
            "fill_opacity": 0,
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_labels()

    def add_axes(self):
        self.axes = Axes(**self.axes_config)
        self.add(self.axes)

    def add_labels(self):
        x_axis = self.get_x_axis()
        y_axis = self.get_y_axis()

        t_label = self.t_label = TextMobject("\#flips")
        t_label.next_to(x_axis.get_right(), UP, MED_SMALL_BUFF)
        x_axis.label = t_label
        x_axis.add(t_label)
        theta_label = self.theta_label = TextMobject("E(max head streak)").scale(0.6)
        theta_label.next_to(y_axis.get_top(), UP, SMALL_BUFF)
        y_axis.label = theta_label
        y_axis.add(theta_label)

        self.y_axis_label = theta_label
        self.x_axis_label = t_label

        x_axis.add(self.get_x_axis_coordinates(x_axis))
        y_axis.add(self.get_y_axis_coordinates(y_axis))

    def get_y_axis_coordinates(self, y_axis):
        texs = [
            1, 2, 3, 4, 5
        ]
        labels = VGroup()
        values = np.arange(1, 5)
        for tex, value in zip(texs, values):
            if value > self.y_max or value < self.y_min:
                continue
            symbol = TexMobject(tex)
            symbol.scale(0.5)
            point = y_axis.number_to_point(value)
            symbol.next_to(point, LEFT, MED_SMALL_BUFF)
            labels.add(symbol)
        return labels

    def get_x_axis_coordinates(self, x_axis):
        texs = [
            i for i in range(self.x_max) if i % 1 == 0
        ]
        labels = VGroup()
        values = np.arange(0, self.x_max)
        for tex, value in zip(texs, values):
            if value > self.x_max or value < self.x_min:
                continue
            symbol = TexMobject(tex)
            symbol.scale(0.5)
            point = x_axis.number_to_point(value)
            symbol.next_to(point, DOWN, MED_SMALL_BUFF)
            labels.add(symbol)
        return labels

class Table(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header_objs = [TextMobject(heading) for heading in self.headings]
        self.header = VGroup(*self.header_objs).arrange(RIGHT)
        self.add(self.header)

        self.line = Line(self.header.get_left(), self.header.get_right())
        self.line.shift(DOWN)
        self.add(self.line)

        self.rows = []

    def add_row(self, items):
        row = []
        for idx, item in enumerate(items):
            obj = TextMobject(item)
            if not self.rows:
                obj.next_to(self.header_objs[idx], 2 * DOWN)
            else:
                obj.next_to(self.rows[-1][idx], DOWN)
            row.append(obj)
        self.rows.append(row)
        g = VGroup(*row)
        self.add(g)
        return g

class MyBrickWall(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width, self.height = 1, 5
        self.outer_rect = Rectangle(width=self.width, height=self.height)
        self.add(self.outer_rect)
        self.num_parts = 1
        self.depth = 1
        self.lines = []
        self.labels = {}
        self.max_streaks = {}

    def find_max_streak(self, x):
        if 'HHHH' in x:
            return 4
        if 'HHH' in x:
            return 3
        if 'HH' in x:
            return 2
        if 'H' in x:
            return 1
        return 0
 
    def draw_init_ht(self):
        orect = self.outer_rect
        top, bottom = orect.get_top(), orect.get_bottom()

        h = TextMobject("H")
        pos = top + (bottom - top) / 4
        h.move_to(pos)

        t = TextMobject("T")
        pos = top + 3 * (bottom - top) / 4
        t.move_to(pos)

        self.labels['H'] = h
        self.labels['T'] = t

        self.max_streaks['H'] = TextMobject("1")
        self.max_streaks['T'] = TextMobject("0")
        self.max_streaks['H'].next_to(self.labels['H'], RIGHT, buff=LARGE_BUFF)
        self.max_streaks['T'].next_to(self.labels['T'], RIGHT, buff=LARGE_BUFF)

        return h, t

    def split_step_draw_dashed_line(self):
        num_lines = self.num_parts
        orect = self.outer_rect
        top, bottom = orect.get_top(), orect.get_bottom()
        first_dist = (bottom - top) / (2 * num_lines)
        other_dist = (bottom - top) / num_lines
        dist = 0
        moves = []
        for i in range(num_lines):
            if i == 0:
                dist += first_dist
            else:
                dist += other_dist

            line = Line(LEFT,
                     RIGHT,
                     dash_length=0.2,
                     positive_space_ratio=0.7).scale(self.width / 2)
            pos = top + dist
            line.move_to(pos)
            self.add(line)
            self.lines.append(line)
            moves.append(Write(line))
        self.num_parts *= 2
        return moves

    def replicate_tosses(self):
        new_dict = {}
        new_streak_dict = {}
        for label, elem in self.labels.items():
            elem_new = elem.deepcopy()
            new_dict[label + 'H'] = elem
            new_dict[label + 'T'] = elem_new

            new_streak_dict[label + 'H'] = self.max_streaks[label]
            new_streak_dict[label + 'T'] = self.max_streaks[label].deepcopy()

        self.labels = new_dict
        self.max_streaks = new_streak_dict

        orect = self.outer_rect
        top, bottom = orect.get_top(), orect.get_bottom()
        dist = (bottom - top) / (4 * self.num_parts)

        moves = []
        for label, elem in self.labels.items():
            if len(label) == self.depth:
                continue
            elem.generate_target()
            streak_elem = self.max_streaks[label]
            streak_elem.generate_target()

            if label.endswith('H'):
                pos = (0, -dist[1], 0)
            else:
                pos = (0, dist[1], 0)

            elem.target.shift(pos)
            streak_elem.target.shift(pos)
            moves.append(MoveToTarget(elem))  
            moves.append(MoveToTarget(streak_elem))  

        return moves

    def add_new_toss(self):
        anims = []
        for label, elem in self.labels.items():
            new_elem = TextMobject(label)
            new_elem.move_to((elem.get_x(), elem.get_y(), 0))
            anims.append(Transform(elem, new_elem))
        for label, elem in self.max_streaks.items():
            new_elem = TextMobject(str(self.find_max_streak(label)))
            new_elem.move_to((elem.get_x(), elem.get_y(), 0))
            anims.append(Transform(elem, new_elem))
        return anims
                
class XYZ(Scene):
    CONFIG = {
        "theta_vs_t_axes_config": {
            "y_max": 5,
            "y_min": 0,
            "y_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.5,
                "tip_length": 0.3,
            },
            "x_max": 10,
            "x_min": 0,
            "x_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.5,
                "tip_length": 0.3,
            },
            "number_line_config": {
                "stroke_width": 2,
            }
        },
        "table": {
            "headings": ["Toss\\\\sequence", "probability\\\\of sequence", "max\\\\head streak"]
        }
    }
    def construct(self):
        #self.add_graph()
        rect = MyBrickWall()
        rect.to_edge(LEFT)
        self.play(Write(rect))

        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        h, t = rect.draw_init_ht()
        self.play(Write(h), Write(t))
        self.play(Write(rect.max_streaks['H']), Write(rect.max_streaks['T']))

        moves = rect.replicate_tosses()
        self.play(*moves)
        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        moves = rect.add_new_toss()
        self.play(*moves)

        moves = rect.replicate_tosses()
        self.play(*moves)
        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        moves = rect.add_new_toss()
        self.play(*moves)

    def add_graph(self):
        axes = self.axes = ThetaVsTAxes(**self.theta_vs_t_axes_config)
        axes.y_axis.label.next_to(axes.y_axis, UP, buff=0)
        axes.to_corner(DR)

        self.play(
            Write(axes)
        )

        self.wait(1.5)
