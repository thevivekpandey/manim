from manimlib.imports import *

class Pendulum(VGroup):
    CONFIG = {
        "top_point": 2 * UP,
        "omega": 0,
        "n_steps_per_frame": 100,
        "damping": 0.1,
        "gravity": 9.8,
        "length": 3,
        "rod_style": {
            "stroke_width": 3,
            "stroke_color": LIGHT_GREY,
            "sheen_direction": UP,
            "sheen_factor": 1,
        },
        "weight_style": {
            "stroke_width": 0,
            "fill_opacity": 1,
            "fill_color": GREY_BROWN,
            "sheen_direction": UL,
            "sheen_factor": 0.5,
            "background_stroke_color": BLACK,
            "background_stroke_width": 3,
            "background_stroke_opacity": 0.5,
        },
        "dashed_line_config": {
            "num_dashes": 25,
            "stroke_color": WHITE,
            "stroke_width": 2,
        },
        "angle_arc_config": {
            "radius": 1,
            "stroke_color": WHITE,
            "stroke_width": 2,
        },
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_fixed_point()
        self.create_rod()
        self.create_weight()
        self.rotating_group = VGroup(self.rod, self.weight)
        self.create_dashed_line()
        self.create_angle_arc()
        self.add_theta_label()
        self.set_theta(0.3)

    def create_rod(self):
        rod = self.rod = Line(UP, DOWN)
        rod.set_height(self.length)
        rod.set_style(**self.rod_style)
        rod.move_to(self.get_fixed_point(), UP)
        self.add(rod)

    def create_weight(self):
        weight = self.weight = Circle()
        weight.set_width(0.35)
        weight.set_style(**self.weight_style)
        weight.move_to(self.rod.get_end())
        self.add(weight)

    def create_fixed_point(self):
        self.fixed_point_tracker = VectorizedPoint(self.top_point)
        self.add(self.fixed_point_tracker)
        return self

    def create_dashed_line(self):
        line = self.dashed_line = DashedLine(
            self.get_fixed_point(),
            self.get_fixed_point() + self.length * DOWN,
            **self.dashed_line_config
        )
        #line.add_updater(
        #    lambda l: l.move_to(self.get_fixed_point(), UP)
        #)
        self.add_to_back(line)

    def create_angle_arc(self):
        self.angle_arc = Arc(
            arc_center = self.get_fixed_point(),
            start_angle = -90 * DEGREES,
            angle = self.get_theta(),
            **self.angle_arc_config,
        )
        self.add(self.angle_arc)

    def set_theta(self, theta):
        self.rotating_group.rotate(
            theta - self.get_theta()
        )
        self.rotating_group.shift(
            self.get_fixed_point() - self.rod.get_start(),
        )

    def get_theta(self):
        theta = self.rod.get_angle() - self.dashed_line.get_angle()
        theta = (theta + PI) % TAU - PI
        return theta

    def get_fixed_point(self):
        return self.fixed_point_tracker.get_location()

    def start_swinging(self):
        self.add_updater(Pendulum.update_by_gravity)

    def update_by_gravity(self, dt):
        theta = self.get_theta()
        omega = self.omega
        nspf = self.n_steps_per_frame
        for x in range(nspf):
            d_theta = omega * dt / nspf
            d_omega = op.add(
                -self.damping * omega,
                -(self.gravity / self.length) * np.sin(theta),
            ) * dt / nspf
            theta += d_theta
            omega += d_omega
        self.set_theta(theta)
        self.set_omega(omega)
        self.omega = omega

    def set_omega(self, omega):
        self.omega = omega
        return self

    def add_theta_label(self):
        #self.theta_label = always_redraw(self.get_label)
        self.theta_label = self.get_label()
        self.add(self.theta_label)

    def get_label(self):
        label = TexMobject("\\theta")
        top = self.get_fixed_point()
        label.move_to(top)
        return label

class IntroducePendulum(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        self.add_pendulum()
        self.label_pendulum()
        self.wait(8)

    def add_pendulum(self):
        pendulum = self.pendulum = Pendulum() 
        pendulum.start_swinging()
        frame = self.camera_frame
        frame.save_state()
        frame.scale(0.5)
        frame.move_to(pendulum.dashed_line)
        self.add(pendulum, frame)

    def label_pendulum(self):
        pendulum = self.pendulum
        label = pendulum.theta_label
        rect = SurroundingRectangle(label, buff=0.5 * SMALL_BUFF)
        #rect.add_updater(lambda r: r.move_to(label))
        self.play(ShowCreationThenFadeOut(rect))
