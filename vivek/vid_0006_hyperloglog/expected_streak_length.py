from manimlib.imports import *
import math

class EStreakVsFlip(Axes):
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
        theta_label = self.theta_label = TextMobject("E(longest\\\\head streak)").scale(0.6)
        theta_label.next_to(y_axis.get_top(), RIGHT, SMALL_BUFF)
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
        steps = self.x_axis_config['tick_frequency']
        texs = [
            i for i in range(self.x_max) if i % steps == 0
        ]
        labels = VGroup()
        values = np.arange(0, self.x_max, steps)
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
        self.FORMULA_SCALE = 0.6
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

        self.max_streaks['H'] = TextMobject(str(self.find_max_streak("H")))
        self.max_streaks['T'] = TextMobject(str(self.find_max_streak("T")))
        self.max_streaks['H'].next_to(self.labels['H'], RIGHT, buff=LARGE_BUFF)
        self.max_streaks['T'].next_to(self.labels['T'], RIGHT, buff=LARGE_BUFF)

        self.add(h, t, self.max_streaks['H'], self.max_streaks['T'])
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
            self.add(elem_new)
            new_dict[label + 'H'] = elem
            new_dict[label + 'T'] = elem_new

            new_streak_dict[label + 'H'] = self.max_streaks[label]
            new_streak_dict[label + 'T'] = self.max_streaks[label].deepcopy()
            self.add(new_streak_dict[label + 'T'])

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
            self.add(new_elem)
            new_elem.move_to((elem.get_x(), elem.get_y(), 0))
            anims.append(Transform(elem, new_elem))
        for label, elem in self.max_streaks.items():
            self.add(new_elem)
            new_elem = TextMobject(str(self.find_max_streak(label)))
            new_elem.move_to((elem.get_x(), elem.get_y(), 0))
            anims.append(Transform(elem, new_elem))

        new_brace_num_text = TextMobject(str(self.num_parts)).scale(0.7)
        new_brace_num_text.next_to(self.brace, LEFT)
        anims.append(Transform(self.brace_text_num, new_brace_num_text))
        return anims

    def init_left_brace(self):
        self.brace = Brace(self.outer_rect, LEFT)
        self.brace_text_num = TextMobject("2").scale(0.7)
        self.brace_text = TextMobject("cases").scale(0.7)
        self.brace_text_num.next_to(self.brace, LEFT)
        self.brace_text.next_to(self.brace_text_num, DOWN)
        self.add(self.brace, self.brace_text, self.brace_text_num)
        return [Write(self.brace), Write(self.brace_text_num), Write(self.brace_text)]

    def create_formula_1(self):
        def fms(idx):
            #fms => find_max_streak
            return str(self.find_max_streak(keys[idx]))

        keys = list(self.max_streaks.keys())
        elems = [fms(0) + " "] + ["+ " + fms(i) for i in range(1, len(keys))]
        texs = [TextMobject(elem).scale(self.FORMULA_SCALE) for elem in elems]
        self.num = VGroup(*texs).arrange(RIGHT, buff=0.5*SMALL_BUFF)
        self.num.next_to(self.outer_rect, DOWN)
        l = self.num.get_right()[0] - self.num.get_left()[0]
        self.frac = Line(LEFT, RIGHT).scale(l / 2)
        self.frac.next_to(self.num, DOWN)
        self.den = TexMobject(str(self.num_parts)).scale(self.FORMULA_SCALE)
        self.den.next_to(self.frac, DOWN)
        anims = []
        for idx, key in enumerate(keys):
            anims.append(TransformFromCopy(self.max_streaks[key], texs[idx]))
        anims.append(Write(self.frac))
        anims.append(TransformFromCopy(self.brace_text_num, self.den))
        self.add(self.num, self.frac, self.den)
        return anims

    def create_formula_2(self, val):
        self.equal = TextMobject("=").scale(self.FORMULA_SCALE)
        self.equal.next_to(self.frac, RIGHT)
        self.expectation = TexMobject(str(val)).scale(self.FORMULA_SCALE)
        self.expectation.next_to(self.equal, RIGHT)
        self.add(self.equal, self.expectation)
        return [Write(self.equal), Write(self.expectation)]

    def erase_formula(self):
        elems = [self.num, self.frac, self.den, self.equal, self.expectation]
        return [FadeOut(e) for e in elems]

class Towers():
    def __init__(self, **kwargs):
        self.TEXT_SCALE = 0.4
        self.towers, self.rects = [], []
        self.init_towers()
        self.ellipsis = TextMobject("...")

    def get_tower(self, seq):
        elems = [TextMobject(t).scale(self.TEXT_SCALE) for t in [*seq]]
        tower = VGroup(*elems).arrange(DOWN, buff=0.09)
        tower.elems = elems
        self.tower_group = tower
        return tower

    def init_towers(self):
        twenty_seq = [
            'HHHTTTTHTHHTHTTTHTHT',
            'THTHHTTHHTHHTTHHHHTH',
            'HHTHTHTTHTTTTHHTTHHT',
            'HTHHTHTHTHTTHHHTHHTT'
        ]

        for i in range(4):
            tower = self.get_tower(twenty_seq[i])
            self.towers.append(tower)

    def get_rect(self, i):
        start_and_nums = [(0, 3), (14, 4), (13, 2), (12, 3)]
        s, n = start_and_nums[i]
        tower = self.towers[i]
        rect = SurroundingRectangle(Group(*self.towers[i].elems[s:s+n]))
        self.rects.append(rect)
        return rect

    def get_brace(self):
        self.brace = Brace(Group(self.towers[0], self.towers[3]), UP, buff=0.1)
        self.brace_text = TextMobject("10000 experiments").scale(self.TEXT_SCALE)
        self.brace_text.next_to(self.brace, UP, buff=0.1)
        return self.brace, self.brace_text

    def create_formula(self):
        unit_length = 0.25
        formula_rects = []
        heights = [3, 4, 2, 3]
        for i in range(4):
            rect = Rectangle(width=unit_length, 
                             height=heights[i]*unit_length, 
                             color=YELLOW)
            formula_rects.append(rect)
        fr = formula_rects
        ellipsis = TextMobject("...")

        ps = [TextMobject("+") for _ in range(4)]
        num = VGroup(fr[0], ps[0], fr[1], ps[1], fr[2], ps[2], ellipsis, ps[3], fr[3]).arrange(RIGHT, buff=SMALL_BUFF)
        num.next_to(self.tower_group, DOWN)
        num.shift(RIGHT)

        x, y = fr[0].get_left()[0], fr[3].get_right()[0]
        line = Line(LEFT,RIGHT).scale((y - x) / 2)
        line.next_to(num, DOWN)

        den = TextMobject("10000")
        den.next_to(line, DOWN)

        equals = TextMobject("=")
        equals.next_to(line)

        self.right = Rectangle(width=unit_length, 
                          height=2.77*unit_length,
                          color=YELLOW)
        self.right.next_to(equals)

        #return num, line, den, equals, right
        return [
             Transform(self.rects[0], fr[0]),
             Transform(self.rects[1], fr[1]),
             Transform(self.rects[2], fr[2]),
             Transform(self.rects[3], fr[3]),
             Write(ps[0]), Write(ps[1]), Write(ps[2]), Write(ps[3]),
             Write(line), 
             TransformFromCopy(self.brace_text, den),
             Write(ellipsis),
             Write(equals), Write(self.right)
        ]

class ExpectedStreakLength(Scene):
    CONFIG = {
        "estreak_vs_flip_config": {
            "y_max": 4,
            "y_min": 0,
            "y_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.7,
                "tip_length": 0.3,
            },
            "x_max": 20,
            "x_min": 0,
            "x_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.35,
                "tip_length": 0.3,
            },
            "number_line_config": {
                "stroke_width": 2,
            }
        },
        "estreak_vs_flip_config_bigger": {
            "y_max": 4,
            "y_min": 0,
            "y_axis_config": {
                "tick_frequency": 1,
                "unit_size": 0.7,
                "tip_length": 0.3,
            },
            "x_max": 200,
            "x_min": 0,
            "x_axis_config": {
                "tick_frequency": 10,
                "unit_size": 0.035,
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
    def first_few_iterations(self, rect):
        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        h, t = rect.draw_init_ht()
        self.play(Write(h), Write(t))
        self.play(Write(rect.max_streaks['H']), Write(rect.max_streaks['T']))

        moves = rect.init_left_brace()
        self.play(*moves)
        moves = rect.create_formula_1()
        self.play(*moves)
        moves = rect.create_formula_2(0.5)
        self.play(*moves)
        self.add_bar(rect.expectation, 0.5, 1)
        moves = rect.erase_formula()
        self.play(*moves)

        # 2nd bar
        moves = rect.replicate_tosses()
        self.play(*moves)
        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        moves = rect.add_new_toss()
        self.play(*moves)
        moves = rect.create_formula_1()
        self.play(*moves)
        moves = rect.create_formula_2(1)
        self.play(*moves)
        self.add_bar(rect.expectation, 1, 2)
        moves = rect.erase_formula()
        self.play(*moves)

        # 3rd bar
        moves = rect.replicate_tosses()
        self.play(*moves)
        moves = rect.split_step_draw_dashed_line()
        self.play(*moves)
        moves = rect.add_new_toss()
        self.play(*moves)
        moves = rect.create_formula_1()
        self.play(*moves)
        moves = rect.create_formula_2(11/8)
        self.play(*moves)
        self.add_bar(rect.expectation, 11/8, 3)

    def add_graph(self):
        axes = self.axes = EStreakVsFlip(**self.estreak_vs_flip_config)
        axes.to_corner(UR, buff=0.5 * SMALL_BUFF)
        axes.shift(2 * DOWN)

        self.play(
            Write(axes)
        )

        self.wait(1.5)

    def add_bar(self, expectation_obj, expectation_val, number):
        x_unit_size = self.estreak_vs_flip_config['x_axis_config']['unit_size']
        y_unit_size = self.estreak_vs_flip_config['y_axis_config']['unit_size']

        length = expectation_val * y_unit_size
        rect = Rectangle(width=x_unit_size / 4, height=length, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        rect.next_to(self.axes.x_axis.number_to_point(number), UP, buff=0)

        self.graph_group.add(rect)
        self.play(TransformFromCopy(expectation_obj, rect))

    def get_bar(self, x_unit_size, y_unit_size, yval):
        length = yval * y_unit_size
        rect = Rectangle(width=x_unit_size / 4, height=length, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        return rect
        
    def add_bar_no_transform(self, expectation_val, number):
        x_unit_size = self.estreak_vs_flip_config['x_axis_config']['unit_size']
        y_unit_size = self.estreak_vs_flip_config['y_axis_config']['unit_size']

        rect = self.get_bar(x_unit_size, y_unit_size, expectation_val)
        rect.next_to(self.axes.x_axis.number_to_point(number), UP, buff=0)

        self.graph_group.add(rect)
        self.play(Write(rect))

    def add_graph_bigger(self):
        bigger_axes = EStreakVsFlip(**self.estreak_vs_flip_config_bigger)
        self.bigger_axes = bigger_axes
        bigger_axes.to_corner(UR, buff=0.5 * SMALL_BUFF)
        bigger_axes.shift(2 * DOWN)
        self.bigger_graph_group.add(bigger_axes)

        config = self.estreak_vs_flip_config_bigger
        x_unit_size = config['x_axis_config']['unit_size']
        y_unit_size = config['y_axis_config']['unit_size']

        for number, expectation_val in enumerate(self.estreaks):
            if number == 0:
                continue
            rect = self.get_bar(x_unit_size, y_unit_size, expectation_val)
            rect.next_to(self.bigger_axes.x_axis.number_to_point(number), UP, buff=0)
            self.bigger_graph_group.add(rect)

    def add_ln_graph(self):
        coords = [(i, math.log2(i + 1)) for i in range(1, 20)]
        points = []
        for coord in coords:
            points.append(self.axes.coords_to_point(*coord))

        self.ln_graph = VMobject()
        self.ln_graph.set_points_smoothly(points)
        self.play(Write(self.ln_graph))

        self.ln_graph_text = TexMobject("\\ln(n) ")
        self.ln_graph_text.next_to(self.ln_graph, UP, buff=0)

        self.add(self.ln_graph, self.ln_graph_text)
        self.play(Write(self.ln_graph_text))

        self.ln_graph_text_suffix = DecimalNumber(0, include_sign=True)
        self.ln_graph_text_suffix.next_to(self.ln_graph_text, RIGHT)
        self.add(self.ln_graph_text_suffix)
        self.play(Write(self.ln_graph_text_suffix))
        self.graph_group.add(self.ln_graph, self.ln_graph_text, self.ln_graph_text_suffix)

    def play_ln_graph_part1(self, mult):
        coords = [(i, mult * math.log(i)) for i in range(1, 20)]
        points = []
        for coord in coords:
            points.append(self.axes.coords_to_point(*coord))

        self.ln_graph_new = VMobject()
        self.ln_graph_new.set_points_smoothly(points)
        self.play(Transform(self.ln_graph, self.ln_graph_new))

    def add_log_2_graph(self):
        coords = [(i, math.log2(i)) for i in range(1, 20)]
        points = []
        for coord in coords:
            points.append(self.axes.coords_to_point(*coord))

        self.log_graph = VMobject(color=RED)
        self.log_graph.set_points_smoothly(points)
        self.play(Write(self.log_graph))

        self.graph_group.add(self.log_graph)

    def play_ln_graph_part2(self):
        self.ln_graph_text_suffix.add_updater(lambda d: d.set_value(self.ln_graph.get_y() - 0.68))
        self.play(
             self.ln_graph.shift, 0.43 *DOWN, run_time=2
        )

    def draw_towers(self, towers):
        towers.towers[0].to_corner(UL)
        towers.towers[0].shift(0.5 * DOWN)
        towers.towers[1].next_to(towers.towers[0])
        towers.towers[2].next_to(towers.towers[1])
        towers.ellipsis.next_to(towers.towers[2])
        towers.towers[3].next_to(towers.ellipsis)

        self.play(Write(towers.towers[0]))
        self.play(Write(towers.get_rect(0)))

        self.play(Write(towers.towers[1]))
        self.play(Write(towers.get_rect(1)))

        self.play(Write(towers.towers[2]))
        self.play(Write(towers.get_rect(2)))

        self.play(Write(towers.ellipsis))

        self.play(Write(towers.towers[3]))
        self.play(Write(towers.get_rect(3)))

    def construct(self):
        rect = MyBrickWall()
        rect.to_edge(LEFT, buff=1.5*LARGE_BUFF)
        rect.shift(UP)
        self.play(Write(rect))

        self.graph_group = Group()
        self.add_graph()
        self.graph_group.add(self.axes)
        self.first_few_iterations(rect)

        self.play(FadeOut(rect))
        self.estreaks = [0, 0.5, 1.0, 1.38, 1.6875, 1.9375, 2.15, 2.34, 2.51, 2.66, 2.8, 2.92, 3.04, 3.15, 3.25, 3.34, 3.43, 3.51, 3.59, 3.66]
        for i in range(3, 20):
            self.add_bar_no_transform(self.estreaks[i], i)

        self.bigger_graph_group = Group()
        self.add_graph_bigger()

        self.play(Transform(self.graph_group, self.bigger_graph_group))
        towers = Towers()
        self.draw_towers(towers)
        brace, brace_text = towers.get_brace()
        self.play(Write(brace), Write(brace_text))

        anims = towers.create_formula()
        self.play(*anims)

        
        #TransformFromCopy(towers.right, 
        #num, line, den, equals, right = towers.create_formula()
        #self.play(Write(num), Write(line), Write(den), Write(equals), Write(right))

        #self.add_ln_graph()
        #for x in [1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.44]:
        #    self.play_ln_graph_part1(x)
        #self.add_log_2_graph()
        #self.play_ln_graph_part2()
        #self.move_graph_up()

