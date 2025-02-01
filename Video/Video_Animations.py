from manim import *
from Manim_Functions import set_defaults

config.background_color = "#d9cdb6"

# DARKER: #1993C8 #A28F02 #627E26 #7C2927 #8C4103
# BLUE: #5BC0EB YELLOW: #FEE20B GREEN: #9BC53D RED: #C3423F ORANGE: #F17105
# LIGHTER: #B6E3F6 #FEED72 #C6DE91 #D88483 #FCA65F

# New Color Scheme
# DARK BLUE: #1B264F
# BLUE: #007991
# LIGHT BLUE: #0E9594
# RED: #D62828
# BLACK #21201E


class Animation1TitleMotivation(Scene):
    def construct(self):
        b_plane = set_defaults()
        title = Text("Gradient Boosted TrEEGs", font_size=60, t2c={'EEG': "#D62828"})
        title_border = SurroundingRectangle(title, buff=1.3, stroke_width=10, fill_opacity=0.5)
        by_text = Text("Created by Lauren Yu, Jonathan Mak, Ian Rundle, and Ben Allen", font_size=45) \
            .next_to(title, 11 * DOWN).scale(0.60)
        datathon_text = Text("Rice Datathon 2025").next_to(title, 11 * UP)
        vertices = [1,2,3,4,5,6]
        edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]
        dec_graph = Graph(vertices, edges, layout="shell", layout_scale=3,
                          vertex_config={"fill_color": "#007991", "color": "#1B264F", "stroke_opacity": 1,
                                         "stroke_width": 3},
                          edge_config={"stroke_opacity": 0.25, "color": "#21201E", "stroke_width": 5})
        dec_graph2 = dec_graph.copy().next_to(dec_graph, LEFT, buff=-0.15)
        dec_graph3 = dec_graph.copy().next_to(dec_graph, RIGHT, buff=-0.15)
        self.add(b_plane, dec_graph, dec_graph2, dec_graph3, title_border, title, by_text, datathon_text)
        self.play(DrawBorderThenFill(b_plane), DrawBorderThenFill(dec_graph), DrawBorderThenFill(dec_graph2),
                  DrawBorderThenFill(dec_graph3),
                  AnimationGroup(Write(title), DrawBorderThenFill(title_border), Write(datathon_text), Write(by_text),
                                 lag_ratio=0.4))
        self.wait(1)
        self.play(AnimationGroup(FadeOut(dec_graph, shift=DOWN), FadeOut(dec_graph, shift=DOWN),
                                 FadeOut(dec_graph, shift=DOWN), lag_ratio=0.4),
                  Unwrite(title), FadeOut(by_text, shift=DOWN))

        # Motivation



class Animation3Objective(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Potentially bring up both objectives and the results here


class Animation4DataDescription(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Include basic size and column descriptors, but it would be cool to include a nice visual description of
        # where each EEG column is and demonstrate what PSD and COH are visually (will try using a graph for this)
        # Basic Description
        title = Text("Data Description", font_size=50).shift(2.5*UP)
        title_border = SurroundingRectangle(title, buff=0.25, stroke_width=10, fill_opacity=0.5)
        data_desc_para = Paragraph("-- 945 patients with 1148 attributes",
                                   "-- Columns covering age, sex, IQ, and education level",
                                   "-- Power spectral density (PSD) and Coherence readings",
                                   t2c={"945": "#1B264F", "1148": "#1B264F",
                                        "age": "#1B264F", "sex": "#1B264F", "IQ": "#1B264F",
                                        "education level": "#1B264F",
                                        "Power spectral density (PSD)": "#D62828", "Coherence": "#D62828"},
                                   font_size=40)
        psd_text = Text("Power spectral density (PSD)")
        self.add(b_plane)
        """self.play(DrawBorderThenFill(title_border), Write(title), Write(data_desc_para, run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(data_desc_para, psd_text))
        self.wait(1)"""

        # Visual EEG Explanation
        brain = Ellipse(width=3, height=4)
        eeg_graph = Graph(vertices=["Fp1", "Fp2", "Fz", "Cz", "Pz", "F3", "C3", "P3", "O1", "F4", "C4", "P4", "02",
                                    "F7", "T3", "T5", "F8", "T4", "T6", "A1", "A2"],
                          edges=[("Fp1", "Fp2")],
                          labels=True)
        nasion_text = Text("Nasion", font_size=30)
        inion_text = Text("Inion", font_size=30)
        self.add(brain, eeg_graph)
        self.wait(1)


class Animation5DataCleaning(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Dropped rows with missing data, normalization, etc.


class Animation6FeatureEngineering(Scene):
    def construct(self):
        b_plane = set_defaults()
        # SMOTE, PCA, etc. (can include mathematical/visual descriptions of these methods


class Animation7Modeling(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Similar to last year, although it may make more sense to have a horizontal pipeline (also include images on
        # boxes)


class Animation8Evaluation(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Describe how model was evaluated (can be skipped for time) and how the model did (accuracy, precision, recall,
        # and most importantly confusion matrix)


class Animation9Insights(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Include any cool visualizations here can move these up if they help explain any of the preprocessing or
        # modeling steps we took


class Animation10Conclusion(Scene):
    def construct(self):
        b_plane = set_defaults()
        # Standard conclusion side with key takeaways and a thank you (mention organizers and neurotech specifically

